#!/usr/bin/env python3
"""model_run: the model-assisted stages through the Claude API, one request per item, only what changed.

The readers of the first runs were agents; this script asks the same questions of the same prompts
through the API, so that a rebuild can run unattended (GitHub Actions, scripts/rebuild.sh). Every
stage keeps a manifest next to its output folder, `<out>.manifest.json`, with the hash of each
item's input: an item is sent again only when its input changed, or with --force. Legacy answers
written by the agents are adopted into the manifest once (--adopt, --adopt-all) and never re-sent
unless forced.

Stages (prompt in stage2/, output as the merge scripts read it):
  decompose  --units <stage-1 units> --out stage2/out_v2|out_cda          decompose_prompt.md -> <out>/proc-<id>.json
  errcat     --units units/troubleshooting --out stage2/errcat-out --devtools <clone>
                                                                          errcat_prompt.md -> <out>/auto-<date>.json
  issues     --threads <folder of thread lists> --out stage2/issues-out    issues_prompt.md -> <out>/auto-<date>.json
  issues-qa  --threads <folder> --digests stage2/issues-out --out stage2/issues-qa
                                                                          issues_qa_prompt.md -> <out>/auto-<date>.json

Options: --model (claude-haiku-5-5) --effort low|medium|high --limit N --force --batch (Message Batches API)
         --concurrency 6 --dry-run (list what is due, no request) --adopt / --adopt-all (record existing
         answers, no request). ANTHROPIC_API_KEY must be set for a run; MODEL_RUN_LOG=<file> appends one
         summary line per run (the rebuild workflow puts it into the pull request).

An answer replaces the older answer of the same item in any file of the output folder, so a file an
agent wrote stays until every item in it has been answered again. A thread the model does not keep
is recorded as kept=false and its older digest, if any, is removed.
"""
import argparse
import concurrent.futures as cf
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
STAGE2 = ROOT / "stage2"
MODEL = "claude-haiku-5-5"
MAX_TOKENS = 16000
EFFORT = {"decompose": "medium", "errcat": "medium", "issues": "medium", "issues-qa": "medium"}
# The cut the first readers' batches had: the body, the first comments, each comment (characters).
BODY_CHARS, COMMENT_CHARS, MAX_COMMENTS = 4000, 1500, 8
CONTEXT_LINES = 60            # source lines before and after a message's trigger, for errcat
CANONICAL = ["rule-no-fabrication", "rule-tone-and-style", "rule-portability", "rule-no-install", "rule-user-confirmation"]
TOOLS = ["pyocd", "csolution", "cbuild", "cpackget", "packchk", "svdconv", "cmsis-debugger", "cmsis-solution",
         "cmsis-core", "cmsis-rtx", "cmsis-view", "gdb", "other"]
ENTITY_TOOLS = ["csolution", "cbuild", "cpackget", "packchk", "svdconv", "pyocd", "west", "vcpkg", "vela", "gdb",
                "cmsis-debugger", "cmsis-solution"]   # the tool entities of build_index.py
RESOLUTIONS = ["fixed-in-release", "workaround", "user-error", "not-a-bug", "configuration"]
CONFIDENCE = ["high", "medium", "low"]
# Haiku 5.5 list prices per million tokens, for the summary line only.
PRICE = {"input": 0.10, "output": 0.50, "cache_read": 0.01, "cache_write": 0.125}


def strs(enum=None):
    return {"type": "array", "items": {"type": "string", **({"enum": enum} if enum else {})}}


def obj(props, required=None):
    return {"type": "object", "additionalProperties": False, "required": required or list(props), "properties": props}


ISSUE_ENTRY = obj({
    "issue": {"type": "string"}, "tool": {"type": "string", "enum": TOOLS}, "title": {"type": "string"},
    "symptoms": strs(), "cause": {"type": "string"}, "fix": {"type": "string"},
    "applies_to": obj({k: strs() for k in ("tool", "family", "device", "board", "core", "component", "toolchain", "compiler", "pack")}),
    "versions": {"type": "string"}, "resolution": {"type": "string", "enum": RESOLUTIONS + [""]},
    "confidence": {"type": "string", "enum": CONFIDENCE},
})
SCHEMAS = {
    "issues": obj({"kept": {"type": "boolean"}, "skip_reason": {"type": "string"}, "entry": ISSUE_ENTRY}),
    "issues-qa": obj({
        "issue": {"type": "string"}, "verdict": {"type": "string", "enum": ["supported", "partly", "unsupported"]},
        "problems": strs(), "symptoms_ok": {"type": "boolean"},
        "cause_fixed": {"type": "string"}, "fix_fixed": {"type": "string"}, "versions_fixed": {"type": "string"},
        "resolution_fixed": {"type": "string", "enum": RESOLUTIONS + ["unresolved", ""]},
    }),
    "errcat": obj({
        "id": {"type": "string"}, "cause": {"type": "string"}, "fix": {"type": "string"}, "evidence": strs(),
        "confidence": {"type": "string", "enum": CONFIDENCE + ["unknown"]}, "note": {"type": "string"},
    }),
    "decompose": obj({
        "id": {"type": "string"}, "summary": {"type": "string"}, "triggers": strs(),
        "applies_to": obj({k: strs() for k in ("tool", "toolchain", "core", "component", "api")}),
        "unmapped": strs(), "verification": strs(), "stop_conditions": strs(),
        "rules": {"type": "array", "items": obj({
            "id": {"type": "string"}, "class": {"type": "string", "enum": ["generic", "specific"]},
            "canonical_id": {"type": "string", "enum": CANONICAL + [""]}, "delta": {"type": "string"}})},
        "extracted": {"type": "array", "items": obj({
            "type": {"type": "string", "enum": ["concept", "pattern", "troubleshooting"]}, "title": {"type": "string"},
            "symptoms": strs(), "body": {"type": "string"}})},
    }),
}
PROMPTS = {"decompose": "decompose_prompt.md", "errcat": "errcat_prompt.md", "issues": "issues_prompt.md",
           "issues-qa": "issues_qa_prompt.md"}
KEYS = {"decompose": "id", "errcat": "id", "issues": "issue", "issues-qa": "issue"}
# What the user turn says beyond the prompt: the prompt was written for readers that got a whole batch and
# wrote a file; here every request carries one item and the answer is one JSON object.
NOTES = {
    "issues": "One thread follows. Answer with one JSON object: `kept` true and the entry for it (its `issue` is the "
              "URL below), or `kept` false with a short `skip_reason` and empty entry fields. For an open issue or an "
              "unanswered discussion the resolution is a workaround, a configuration, a user error or not a bug.",
    "issues-qa": "One item follows: the digest, then the thread it was written from. Answer with one JSON object "
                 "for it; for `supported` leave the four `*_fixed` fields empty.",
    "errcat": "One message follows with the source lines around its trigger. Answer with one JSON object for it.",
    "decompose": "One procedure follows with the rules that constrain it, then the list of valid entity ids. "
                 "Answer with one JSON object for it; `rules` holds one entry per rule given, with its id.",
}


# ── helpers ─────────────────────────────────────────────────────────────────

def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def read_unit(p):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", p.read_text(encoding="utf-8"), re.S)
    if not m:
        raise ValueError(f"{p}: no frontmatter")
    return yaml.safe_load(m.group(1)) or {}, m.group(2).strip()


def section(body, heading):
    m = re.search(rf"^## {re.escape(heading)}\n\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def thread_text(t):
    """The thread as the first readers saw it: title, state, the body and the first comments, cut."""
    lines = [f"Thread: {t['url']}", f"Title: {t.get('title', '')}", f"State: {t.get('state', '')}"
             + (f", closed {t['closed']}" if t.get("closed") else "")]
    if t.get("labels"):
        lines.append("Labels: " + ", ".join(t["labels"]))
    lines += ["", "## Body", "", (t.get("body") or "")[:BODY_CHARS]]
    for i, c in enumerate((t.get("comments") or [])[:MAX_COMMENTS], 1):
        c = c if isinstance(c, str) else (c.get("body") or "")
        lines += ["", f"## Comment {i}", "", c[:COMMENT_CHARS]]
    return "\n".join(lines)


def load_threads(folder):
    out = {}
    for f in sorted(Path(folder).glob("*.json")):
        for t in json.loads(f.read_text(encoding="utf-8")):
            out[t["url"]] = t
    return out


def load_answers(out, key):
    """Every answer in the output folder by its key, with the file it is in (the first file wins, as the merges do)."""
    found = {}
    for f in sorted(Path(out).glob("*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  {f}: not JSON, skipped")
            continue
        for a in (data if isinstance(data, list) else [data]):
            if isinstance(a, dict) and a.get(key) and a[key] not in found:
                found[a[key]] = (f.name, a)
    return found


class Item:
    def __init__(self, id, text, meta=None):
        self.id, self.text, self.meta = id, text, meta or {}
        self.sha = sha(text)


# ── items per stage ─────────────────────────────────────────────────────────

def items_issues(a):
    for url, t in load_threads(a.threads).items():
        yield Item(url, NOTES["issues"] + "\n\n" + thread_text(t),
                   {"date": t.get("closed") or t.get("updated") or "", "open": bool(t.get("open"))})


def items_issues_qa(a):
    threads = load_threads(a.threads)
    missing = 0
    for url, (fname, d) in load_answers(a.digests, "issue").items():
        t = threads.get(url)
        if t is None:
            missing += 1
            continue
        digest = {k: v for k, v in d.items() if k not in ("checked",)}
        text = (NOTES["issues-qa"] + "\n\n## Digest\n\n```json\n" + json.dumps(digest, ensure_ascii=False, indent=1)
                + "\n```\n\n## Thread\n\n" + thread_text(t))
        yield Item(url, text, {"digest_sha": sha(json.dumps(digest, sort_keys=True, ensure_ascii=False))})
    if missing:
        print(f"  {missing} digests without a thread in {a.threads}: not checked (their check, if any, stays)")


def source_context(devtools, ref):
    """`path:line` of a unit's source -> the lines around it from the clone, numbered; '' when not there."""
    m = re.match(r"(?:[\w.-]+/[\w.-]+@\w+:)?(.+?):(\d+)$", ref.strip())
    if not m or not devtools:
        return ""
    path, line = Path(devtools) / m.group(1), int(m.group(2))
    if not path.is_file():
        return ""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    lo, hi = max(1, line - CONTEXT_LINES), min(len(lines), line + CONTEXT_LINES)
    return f"### {m.group(1)}:{lo}-{hi}\n\n```\n" + "\n".join(f"{n:5d}  {lines[n - 1]}" for n in range(lo, hi + 1)) + "\n```"


def items_errcat(a):
    ref = ""
    if a.devtools and (Path(a.devtools) / ".git").exists():
        import subprocess
        ref = "Open-CMSIS-Pack/devtools@" + subprocess.run(["git", "-C", a.devtools, "rev-parse", "--short=8", "HEAD"],
                                                           capture_output=True, text=True).stdout.strip()
    for p in sorted(Path(a.units).glob("*.md")):
        meta, body = read_unit(p)
        cause, fix = section(body, "Cause"), section(body, "Fix")
        placeholder = lambda s: not s or re.fullmatch(r"_[^_\n]+_", s) is not None
        existing = "" if placeholder(cause) else cause
        needs = "cause and fix" if placeholder(cause) else ("fix" if placeholder(fix) else "cause and fix (check the README text)")
        trigger = section(body, "Trigger in the source")
        src = str(meta.get("source", ""))
        src_path = re.sub(r"^[\w.-]+/[\w.-]+@\w+:", "", src)
        head = [f"Message id: {meta['id']}", f"Tool: {meta.get('tool', '')}", f"Code: {meta.get('code', '')}",
                f"Severity: {meta.get('severity', '')}", "Message: " + " | ".join(meta.get("symptoms") or [meta.get("title", "")]),
                f"Documented in the README: {'yes' if meta.get('documented') else 'no'}", f"Needed: {needs}",
                f"Source: {src_path}"]
        parts = ["\n".join(head)]
        if existing:
            parts.append("## README cause\n\n" + existing)
        if not placeholder(fix):
            parts.append("## README fix\n\n" + fix)
        if trigger:
            parts.append("## Trigger in the source\n\n" + trigger)
        # The hash covers the message, its trigger and where it is printed, not the source lines (line numbers
        # move with every commit) and not the README or an earlier analysis (errcat_merge.py rewrites them):
        # the same before and after the merge, so a message is sent once.
        stable = "\n".join(head[:6] + [f"Source: {src_path}"]) + ("\n\n" + trigger if trigger else "")
        contexts = [c for c in (source_context(a.devtools, s) for s in [src] + list(meta.get("locations") or [])) if c]
        text = NOTES["errcat"] + "\n\n" + stable + ("\n\n## Source lines\n\n" + "\n\n".join(contexts) if contexts else
                                                      "\n\n## Source lines\n\n(the clone is not available: answer from the message and the trigger alone, confidence at most medium)")
        it = Item(meta["id"], text, {"ref": ref})
        it.sha = sha(stable)
        yield it


def entity_ids(folder):
    """The ids a procedure may name in applies_to: every api, core and toolchain, the components of the Arm and
    Keil packs (the vendor packs would add six thousand lines), and the tools of build_index.py."""
    ids = []
    ent = Path(folder) / "entities.jsonl"
    if ent.exists():
        for line in ent.read_text(encoding="utf-8").splitlines():
            n = json.loads(line)
            t = n.get("type")
            if t in ("api", "core", "toolchain") or (t == "component" and n["id"].split("::")[0] in ("component:ARM", "component:Keil")):
                ids.append(n["id"])
    return sorted(ids) + [f"tool:{t}" for t in ENTITY_TOOLS]


def items_decompose(a):
    units = Path(a.units)
    rules = []
    for rp in sorted((units / "rule").glob("*.md")):
        rm, rb = read_unit(rp)
        rules.append((rm, rp.read_text(encoding="utf-8"), re.split(r"\n## Delta zu ", rb)[0].strip()))
    ents = "\n".join(entity_ids(a.entities))
    for pp in sorted((units / "procedure").glob("*.md")):
        pm, pb = read_unit(pp)
        pid = pm["id"]
        mine = [(rm, raw, core) for rm, raw, core in rules if pid in (rm.get("constrains") or [])]
        text = "# PROCEDURE\n\n" + pp.read_text(encoding="utf-8") + "".join("\n\n# RULE\n\n" + raw for _, raw, _ in mine)
        stable = pb + "".join(f"\n\n# RULE {rm['id']}\n\n{core}" for rm, _, core in mine)
        it = Item(pid, NOTES["decompose"] + "\n\n" + text + "\n\n# ENTITY IDS\n\n" + ents,
                  {"rule_ids": [rm["id"] for rm, _, _ in mine]})
        it.sha = sha(stable)
        yield it


ITEMS = {"issues": items_issues, "issues-qa": items_issues_qa, "errcat": items_errcat, "decompose": items_decompose}


# ── answers ─────────────────────────────────────────────────────────────────

def shape(stage, item, ans):
    """The answer as the merge script expects it, or None when the item is not kept. Raises on a wrong id."""
    if stage == "issues":
        if not ans.get("kept"):
            return None
        e = dict(ans["entry"])
        e["issue"] = item.id
        e["applies_to"] = {k: v for k, v in (e.get("applies_to") or {}).items() if v}
        if item.meta.get("open"):
            e["open"] = True
        if not (e.get("cause") and e.get("fix") and e.get("title")):
            raise ValueError("kept, but cause, fix or title is empty")
        return e
    if stage == "issues-qa":
        ans["issue"] = item.id
        if ans.get("verdict") == "supported":
            for k in ("cause_fixed", "fix_fixed", "versions_fixed", "resolution_fixed"):
                ans.pop(k, None)
        return ans
    if stage == "errcat":
        ans["id"] = item.id
        if item.meta.get("ref"):
            ans["ref"] = item.meta["ref"]
        return ans
    if stage == "decompose":
        ans["id"] = item.id
        given = set(item.meta.get("rule_ids") or [])
        ans["rules"] = [r for r in ans.get("rules", []) if r["id"] in given]
        for r in ans["rules"]:
            if r["class"] != "generic":
                r["canonical_id"], r["delta"] = "", ""
        return ans
    raise ValueError(stage)


def remove_from_files(out, key, ids):
    """Drop the older answers of these ids from every list file of the folder."""
    for f in sorted(Path(out).glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue
        kept = [a for a in data if not (isinstance(a, dict) and a.get(key) in ids)]
        if len(kept) != len(data):
            if kept:
                f.write_text(json.dumps(kept, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            else:
                f.unlink()


def write_answers(stage, out, key, answers, today):
    """answers: {id: shaped answer or None}. Returns the file the kept ones went to."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    if stage == "decompose":
        for pid, ans in answers.items():
            if ans is not None:
                (out / f"{pid}.json").write_text(json.dumps(ans, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return "<id>.json"
    remove_from_files(out, key, set(answers))
    target = out / f"auto-{today}.json"
    data = json.loads(target.read_text(encoding="utf-8")) if target.exists() else []
    data = [a for a in data if a.get(key) not in answers] + [a for a in answers.values() if a is not None]
    if data:
        target.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    elif target.exists():
        target.unlink()
    return target.name


# ── the API ─────────────────────────────────────────────────────────────────

def request_params(model, effort, system, schema, item):
    return dict(model=model, max_tokens=MAX_TOKENS,
                system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
                output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
                messages=[{"role": "user", "content": item.text}])


def parse_message(msg, usage):
    usage["input"] += msg.usage.input_tokens
    usage["output"] += msg.usage.output_tokens
    usage["cache_read"] += getattr(msg.usage, "cache_read_input_tokens", 0) or 0
    usage["cache_write"] += getattr(msg.usage, "cache_creation_input_tokens", 0) or 0
    if msg.stop_reason == "refusal":
        raise RuntimeError("refused: " + str(getattr(msg, "stop_details", "") or ""))
    if msg.stop_reason == "max_tokens":
        raise RuntimeError("answer cut at max_tokens")
    text = next((b.text for b in msg.content if b.type == "text"), "")
    return json.loads(text)


def ask_sync(items, model, effort, system, schema, concurrency, usage):
    import anthropic
    client = anthropic.Anthropic(max_retries=5)

    def one(item):
        msg = client.messages.create(**request_params(model, effort, system, schema, item))
        return item, parse_message(msg, usage)

    results, errors = {}, {}
    with cf.ThreadPoolExecutor(concurrency) as ex:
        for fut in cf.as_completed([ex.submit(one, it) for it in items]):
            try:
                item, ans = fut.result()
                results[item.id] = ans
            except Exception as e:                      # one failed item must not end the run
                errors[str(e)[:200]] = errors.get(str(e)[:200], 0) + 1
                print(f"  failed: {str(e)[:200]}")
    return results, errors


def ask_batch(items, model, effort, system, schema, usage):
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    client = anthropic.Anthropic(max_retries=5)
    by_cid = {f"i{n:05d}": it for n, it in enumerate(items)}
    batch = client.messages.batches.create(requests=[
        Request(custom_id=cid, params=MessageCreateParamsNonStreaming(**request_params(model, effort, system, schema, it)))
        for cid, it in by_cid.items()])
    print(f"  batch {batch.id}: {len(by_cid)} requests")
    while True:
        batch = client.messages.batches.retrieve(batch.id)
        if batch.processing_status == "ended":
            break
        print(f"  {batch.processing_status}: {batch.request_counts.processing} processing", flush=True)
        time.sleep(30)
    results, errors = {}, {}
    for r in client.messages.batches.results(batch.id):
        item = by_cid[r.custom_id]
        try:
            if r.result.type != "succeeded":
                raise RuntimeError(f"batch result {r.result.type}")
            results[item.id] = parse_message(r.result.message, usage)
        except Exception as e:
            errors[str(e)[:200]] = errors.get(str(e)[:200], 0) + 1
            print(f"  failed: {str(e)[:200]}")
    return results, errors


# ── main ────────────────────────────────────────────────────────────────────

def load_manifest(path):
    if Path(path).exists():
        return json.loads(Path(path).read_text(encoding="utf-8"))
    return {"stage": "", "model": "", "prompt_sha": "", "since": "", "items": {}}


def save_manifest(path, m):
    m["items"] = dict(sorted(m["items"].items()))
    Path(path).write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("stage", choices=list(ITEMS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--units")
    ap.add_argument("--threads")
    ap.add_argument("--digests")
    ap.add_argument("--devtools")
    ap.add_argument("--entities", default=str(ROOT / "build" / "entities"))
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--effort")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--batch", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--adopt", action="store_true", help="record the items that have an answer as done, no request")
    ap.add_argument("--adopt-all", action="store_true", help="record every item as done (issues: the threads the readers judged)")
    a = ap.parse_args()
    stage, key = a.stage, KEYS[a.stage]
    need = {"issues": ["threads"], "issues-qa": ["threads", "digests"], "errcat": ["units"], "decompose": ["units"]}[stage]
    for n in need:
        if not getattr(a, n):
            sys.exit(f"{stage} needs --{n}")
    prompt_path = STAGE2 / PROMPTS[stage]
    system = prompt_path.read_text(encoding="utf-8")
    prompt_sha = sha(system)
    manifest_path = Path(str(a.out).rstrip("/") + ".manifest.json")
    m = load_manifest(manifest_path)
    m["stage"] = stage
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()

    items = list(ITEMS[stage](a))
    answers = load_answers(a.out, key)
    if a.adopt or a.adopt_all:
        n = 0
        for it in items:
            if it.id in answers or a.adopt_all:
                fname = answers[it.id][0] if it.id in answers else ""
                m["items"][it.id] = {"sha": it.sha, "at": "adopted", "kept": it.id in answers, "file": fname,
                                     "model": "reader agents", "prompt_sha": ""}
                n += 1
        if stage == "issues":
            dates = [it.meta.get("date", "") for it in items if it.id in m["items"]]
            m["since"] = max([m.get("since", "")] + [d for d in dates if d])
        m["prompt_sha"] = m.get("prompt_sha") or prompt_sha
        save_manifest(manifest_path, m)
        print(f"{stage}: adopted {n} of {len(items)} items into {manifest_path.name}")
        return

    if m.get("prompt_sha") and m["prompt_sha"] != prompt_sha and not a.force:
        print(f"note: {prompt_path.name} changed since the last run; only new or changed items are sent "
              f"(--force re-sends all {len(items)})")
    due = [it for it in items if a.force or it.id not in m["items"] or m["items"][it.id]["sha"] != it.sha]
    cut = a.limit and len(due) > a.limit
    print(f"{stage}: {len(items)} items, {len(due)} due" + (f", {a.limit} sent (--limit)" if cut else ""))
    if cut:
        due = due[:a.limit]
    if a.dry_run:
        for it in due[:50]:
            print(f"  {it.id}  ({len(it.text)} chars)")
        if len(due) > 50:
            print(f"  ... {len(due) - 50} more")
        return
    if not due:
        if stage == "issues" and not cut:
            m["since"] = max([m.get("since", "")] + [it.meta.get("date", "") for it in items])
            save_manifest(manifest_path, m)
        return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY is not set")

    effort = a.effort or EFFORT[stage]
    schema = SCHEMAS[stage]
    usage = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
    t0 = time.time()
    if a.batch:
        results, errors = ask_batch(due, a.model, effort, system, schema, usage)
    else:
        results, errors = ask_sync(due, a.model, effort, system, schema, a.concurrency, usage)

    shaped, bad = {}, 0
    by_id = {it.id: it for it in due}
    for iid, ans in results.items():
        try:
            shaped[iid] = shape(stage, by_id[iid], ans)
        except (ValueError, KeyError, TypeError) as e:
            bad += 1
            print(f"  {iid}: answer rejected: {e}")
    fname = write_answers(stage, a.out, key, shaped, today) if shaped else ""
    for iid, ans in shaped.items():
        m["items"][iid] = {"sha": by_id[iid].sha, "at": now, "kept": ans is not None,
                           "file": fname if ans is not None else "", "model": a.model, "prompt_sha": prompt_sha}
    m["model"], m["prompt_sha"] = a.model, prompt_sha
    if stage == "issues" and not cut and not errors and not bad:
        m["since"] = max([m.get("since", "")] + [it.meta.get("date", "") for it in items])
    save_manifest(manifest_path, m)

    kept = sum(1 for v in shaped.values() if v is not None)
    cost = sum(usage[k] * PRICE[k] / 1e6 for k in usage)
    line = (f"{stage}: {len(due)} sent, {len(shaped)} answered ({kept} kept), {bad} rejected, "
            f"{sum(errors.values())} failed; tokens in {usage['input']} out {usage['output']} cache {usage['cache_read']}; "
            f"about ${cost:.2f} at {a.model} list prices; {time.time() - t0:.0f} s")
    print(line)
    for e, n in errors.items():
        print(f"  {n}x {e}")
    if os.environ.get("MODEL_RUN_LOG"):
        with open(os.environ["MODEL_RUN_LOG"], "a", encoding="utf-8") as fh:
            fh.write("- " + line + "\n")
    if not shaped and due:
        sys.exit(1)


if __name__ == "__main__":
    main()
