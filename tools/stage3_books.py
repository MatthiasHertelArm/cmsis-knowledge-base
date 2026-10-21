#!/usr/bin/env python3
"""stage3_books: refine the book units of pdf2ku with a small model, one request per unit.

Stage A (no model): the clean-up a script can do: list numbers reattached, hyphenated line breaks
joined, boilerplate sections marked with a role. Stage B (Claude Haiku 5.5, stage2/books_prompt.md):
type with the fields of that type, summary, triggers, the body as Markdown, extracts, applies_to.
Stage D (no model): every field the model wrote is checked before it enters a unit: the Markdown
body must contain the words of the input and nothing else, summaries stay within 40 words, types,
domains and applies_to values come from fixed lists, extracts are verbatim. A field that fails
falls back to the input and is listed in the report.

Two ways to run stage B, same prompt, same output:
  prepare  <book-dir> <in-dir>              batch files for reader agents or for `submit`
  submit   <in-dir>                         one Message Batch per book through the Anthropic API
                                            (needs ANTHROPIC_API_KEY); writes <in-dir>/batch.id
  fetch    <in-dir> <out-dir>               the batch's results as the reader agents would write them
  merge    <book-dir> <out-dir> <refined-dir> [--report=path.csv]
                                            the checked units into refined-dir, one report line each

Usage: python stage3_books.py <command> ... [--batch-size=20] [--model=claude-haiku-5-5]
  prepare also takes --roles=intro,summary,preface (only those units) and --first=9 (number the files from 9,
  keeping the earlier ones): a later batch's answer for an id replaces an earlier one in `merge`.
"""
import csv, json, os, re, sys, time
from collections import Counter
from pathlib import Path
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdf2ku import strip_promo  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROMPT = ROOT / "stage2" / "books_prompt.md"
MODEL = "claude-haiku-5-5"
BATCH_SIZE = 20
TYPES = ["concept", "procedure", "pattern", "rule", "troubleshooting"]
DOMAINS = ["cpp", "project", "bring-up", "drivers", "debug", "core", "optimization", "rtos", "test", "general"]
TOOLS = ["csolution", "cbuild", "cpackget", "packchk", "svdconv", "pyocd", "west", "vcpkg", "vela", "gdb",
         "cmsis-debugger", "cmsis-solution"]
ROLES = re.compile(r"(?i)^(technical requirements|summary|questions|answers|further reading|exercises?|"
                   r"join our community[^\n]*|free benefits with your book|how to unlock|preface)$")
NEW_WORD_SHARE = 0.02      # words of body_md that are not in the input, at most
LOST_WORD_SHARE = 0.10     # words of the input that body_md lost, at most
MIN_EXTRACT_CHARS = 160    # an extract shorter than this is a sentence, not a unit
MARKDOWN_WORDS = {"c", "cpp", "cmake", "bash", "asm", "text", "sh", "json", "yaml", "make", "ld", "rust", "python"}
SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["id", "drop", "drop_reason", "type", "domain", "title", "summary", "triggers", "body_md",
                 "fields", "applies_to", "extracted", "confidence"],
    "properties": {
        "id": {"type": "string"}, "drop": {"type": "boolean"}, "drop_reason": {"type": "string"},
        "type": {"type": "string", "enum": TYPES}, "domain": {"type": "string", "enum": DOMAINS},
        "title": {"type": "string"}, "summary": {"type": "string"},
        "triggers": {"type": "array", "items": {"type": "string"}}, "body_md": {"type": "string"},
        "fields": {
            "type": "object", "additionalProperties": False,
            "required": ["steps", "preconditions", "verification", "problem", "solution", "tradeoffs",
                         "severity", "rationale", "symptoms", "cause", "fix"],
            "properties": {
                "steps": {"type": "array", "items": {"type": "string"}},
                "preconditions": {"type": "array", "items": {"type": "string"}},
                "verification": {"type": "array", "items": {"type": "string"}},
                "problem": {"type": "string"}, "solution": {"type": "string"}, "tradeoffs": {"type": "string"},
                "severity": {"type": "string", "enum": ["", "must", "should"]}, "rationale": {"type": "string"},
                "symptoms": {"type": "array", "items": {"type": "string"}},
                "cause": {"type": "string"}, "fix": {"type": "string"},
            },
        },
        "applies_to": {
            "type": "object", "additionalProperties": False, "required": ["core", "toolchain", "tool"],
            "properties": {k: {"type": "array", "items": {"type": "string"}} for k in ("core", "toolchain", "tool")},
        },
        "extracted": {
            "type": "array",
            "items": {
                "type": "object", "additionalProperties": False, "required": ["type", "title", "symptoms", "body"],
                "properties": {
                    "type": {"type": "string", "enum": ["troubleshooting", "rule", "pattern", "concept"]},
                    "title": {"type": "string"}, "symptoms": {"type": "array", "items": {"type": "string"}},
                    "body": {"type": "string"},
                },
            },
        },
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
}


# ── units ───────────────────────────────────────────────────────────────────

def read_unit(p):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", p.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)), m.group(2).strip()


def yaml_val(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, list):
        return "[" + ", ".join(json.dumps(str(x), ensure_ascii=False) for x in v) + "]"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{k}: {yaml_val(x)}" for k, x in v.items()) + "}"
    return json.dumps(str(v), ensure_ascii=False)


def write_unit(p, meta, body):
    lines = ["---"] + [f"{k}: {yaml_val(v)}" for k, v in meta.items() if v not in ("", [], {}, None)] + ["---", "", body.strip(), ""]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(lines), encoding="utf-8")


def allowed_lists():
    cores, toolchains = [], []
    ent = ROOT / "build" / "entities" / "entities.jsonl"
    if ent.exists():
        for line in open(ent, encoding="utf-8"):
            n = json.loads(line)
            if n["type"] == "core":
                cores.append(n["id"].split(":", 1)[1])
            elif n["type"] == "toolchain":
                toolchains.append(n["id"].split(":", 1)[1])
    return {"domain": DOMAINS, "core": sorted(cores), "toolchain": sorted(toolchains), "tool": TOOLS}


# ── stage A ─────────────────────────────────────────────────────────────────

def clean(body):
    """What a script can repair: promotion boxes, list numbers and bullets on their own line, hyphenated breaks."""
    body = strip_promo(body)
    body = re.sub(r"(?m)^(\d{1,2}\.)\n\n(?=\S)", r"\1 ", body)
    body = re.sub(r"(?m)^[•·▪◦‣]\n\n(?=\S)", "- ", body)
    body = re.sub(r"(?m)^[•·▪◦‣] ", "- ", body)
    body = re.sub(r"([a-z]{2,})-\n([a-z]{2,})", r"\1\2", body)
    return body


KEEP_ROLES = {"intro", "summary", "preface"}


def role_of(title):
    """What a boilerplate section is: intro (the chapter's own text), summary, technical requirements, ..."""
    last = re.sub(r" \(part \d+\)$", "", title.split(": ")[-1])
    if ROLES.match(last):
        return last.lower().replace("’", "'")
    return "intro" if ": " not in title else ""


# ── stage B ─────────────────────────────────────────────────────────────────

def prepare(book_dir, in_dir, batch_size, roles=None, first=1):
    """Batch files; `roles` limits the units to those roles (a re-run of the intros), `first` numbers the files."""
    book_dir, in_dir = Path(book_dir), Path(in_dir)
    in_dir.mkdir(parents=True, exist_ok=True)
    if first == 1:
        for old in in_dir.glob("batch-*.json"):
            old.unlink()
    prompt = PROMPT.read_text(encoding="utf-8")
    allowed = allowed_lists()
    units = []
    for p in sorted(book_dir.glob("*.md")):
        meta, body = read_unit(p)
        role = role_of(meta["title"])
        if roles and role not in roles:
            continue
        units.append({"id": meta["id"], "title": meta["title"], "book": meta.get("book", ""),
                      "chapter": meta.get("chapter", 0), "role": role, "body": clean(body)})
    n = first - 1
    for i in range(0, len(units), batch_size):
        n += 1
        (in_dir / f"batch-{n:02d}.json").write_text(
            json.dumps({"prompt": prompt, "allowed": allowed, "units": units[i:i + batch_size]}, ensure_ascii=False, indent=1),
            encoding="utf-8")
    print(f"{len(units)} units in {n} batches -> {in_dir}")


def request_text(allowed, unit):
    return (f"Allowed values\n{json.dumps(allowed, ensure_ascii=False)}\n\n"
            f"Unit\nid: {unit['id']}\ntitle: {unit['title']}\nbook: {unit['book']}\nchapter: {unit['chapter']}\n"
            f"role: {unit['role'] or '(none)'}\n\n{unit['body']}")


def submit(in_dir, model):
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request
    in_dir = Path(in_dir)
    client = anthropic.Anthropic()
    system = [{"type": "text", "text": PROMPT.read_text(encoding="utf-8"), "cache_control": {"type": "ephemeral"}}]
    requests = []
    for bf in sorted(in_dir.glob("batch-*.json")):
        b = json.loads(bf.read_text(encoding="utf-8"))
        for u in b["units"]:
            requests.append(Request(custom_id=u["id"][:64], params=MessageCreateParamsNonStreaming(
                model=model, max_tokens=16000, system=system,
                output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
                messages=[{"role": "user", "content": request_text(b["allowed"], u)}])))
    batch = client.messages.batches.create(requests=requests)
    (in_dir / "batch.id").write_text(batch.id)
    print(f"batch {batch.id}: {len(requests)} requests, {batch.processing_status}")


def fetch(in_dir, out_dir):
    import anthropic
    in_dir, out_dir = Path(in_dir), Path(out_dir)
    client = anthropic.Anthropic()
    batch_id = (in_dir / "batch.id").read_text().strip()
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status == "ended":
            break
        print(f"{batch.processing_status}: {batch.request_counts.processing} processing")
        time.sleep(30)
    results, usage = {}, Counter()
    for r in client.messages.batches.results(batch_id):
        if r.result.type != "succeeded":
            print(f"{r.custom_id}: {r.result.type}")
            continue
        msg = r.result.message
        usage["input"] += msg.usage.input_tokens
        usage["output"] += msg.usage.output_tokens
        usage["cache_read"] += msg.usage.cache_read_input_tokens or 0
        text = next((b.text for b in msg.content if b.type == "text"), "")
        try:
            results[r.custom_id] = json.loads(text)
        except json.JSONDecodeError:
            print(f"{r.custom_id}: no JSON")
    out_dir.mkdir(parents=True, exist_ok=True)
    for bf in sorted(in_dir.glob("batch-*.json")):
        b = json.loads(bf.read_text(encoding="utf-8"))
        rows = [results[u["id"][:64]] for u in b["units"] if u["id"][:64] in results]
        (out_dir / bf.name).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(results)} results -> {out_dir}; tokens {dict(usage)}")


# ── stage D ─────────────────────────────────────────────────────────────────

def words(text):
    return Counter(re.findall(r"[a-z0-9]+", text.lower()))


def word_check(original, candidate):
    """(share of candidate words not in the original, share of original words the candidate lost).
    `original` may be a list of variants (the raw text and its stage A form): a word counts when any has it."""
    variants = original if isinstance(original, list) else [original]
    a = Counter()
    for v in variants:
        a |= words(v)
    least = words(variants[-1])          # the last variant is the smallest the model may reduce the text to
    b = words(candidate)
    for w in MARKDOWN_WORDS:
        b[w] = max(0, b[w] - 3)
    new = sum((b - a).values())
    lost = sum((least - b).values())
    return (new / max(1, sum(b.values())), lost / max(1, sum(least.values())))


CAPTION = re.compile(r"(?m)^Figure \d+\.\d+:.*(\n[^\n]+)?$")


def without_captions(text):
    """The prompt lets the model drop figure captions whose figure is not there."""
    return CAPTION.sub("", text)


def merge(book_dir, out_dir, refined_dir, report):
    book_dir, out_dir, refined_dir = Path(book_dir), Path(out_dir), Path(refined_dir)
    allowed = allowed_lists()
    results = {}
    for f in sorted(out_dir.glob("batch-*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            r["_batch"] = f.name
            results[r.get("id", "")] = r
    if refined_dir.exists():
        for old in refined_dir.glob("*.md"):
            old.unlink()
    rows, stats = [], Counter()
    excl_file = ROOT / "stage2" / "books-exclusions.json"
    excluded = json.loads(excl_file.read_text(encoding="utf-8")) if excl_file.exists() else {}
    for p in sorted(book_dir.glob("*.md")):
        meta, raw = read_unit(p)
        if meta.get("id") in excluded:
            stats["excluded earlier"] += 1
            rows.append([meta["id"], "", "", "excluded", excluded[meta["id"]].get("reason", "")])
            continue
        body = clean(raw)
        variants = [raw, body, without_captions(body)]
        r = results.get(meta["id"])
        issues = []
        if r is None:
            stats["no result"] += 1
            meta["role"] = role_of(meta["title"]) or None
            write_unit(refined_dir / p.name, meta, body)
            rows.append([meta["id"], "concept", "", "no result", ""])
            continue
        role = role_of(meta["title"])
        if r.get("drop") and role not in KEEP_ROLES:
            stats["dropped"] += 1
            rows.append([meta["id"], "", "", "dropped", r.get("drop_reason", "")])
            continue
        new_meta = dict(meta)
        t = r.get("type") if r.get("type") in TYPES else "concept"
        if r.get("type") not in TYPES:
            issues.append("type")
        new_meta["type"] = t
        new_meta["domain"] = r["domain"] if r.get("domain") in DOMAINS else meta.get("domain", "general")
        if r.get("domain") not in DOMAINS:
            issues.append("domain")
        summary = (r.get("summary") or "").strip()
        if 0 < len(summary.split()) <= 40:
            new_meta["summary"] = summary
        else:
            issues.append("summary")
        triggers = [x.strip() for x in (r.get("triggers") or []) if isinstance(x, str) and 0 < len(x.split()) <= 12][:5]
        if triggers:
            new_meta["triggers"] = triggers
        title = (r.get("title") or "").strip()
        if title and word_check(meta["title"], title)[0] == 0:
            new_meta["title"] = title
        body_md = strip_promo(r.get("body_md") or "").strip()
        new, lost = word_check(variants, body_md)
        if body_md and new <= NEW_WORD_SHARE and lost <= LOST_WORD_SHARE:
            out_body = body_md
        else:
            out_body = body
            issues.append(f"body(new {new:.0%}, lost {lost:.0%})")
        f = r.get("fields") or {}
        keep = {"procedure": ("steps", "preconditions", "verification"), "pattern": ("problem", "solution", "tradeoffs"),
                "rule": ("severity", "rationale"), "troubleshooting": ("symptoms", "cause", "fix")}.get(t, ())
        for k in keep:
            v = f.get(k)
            if v:
                new_meta[k] = v
        for k, vals in (r.get("applies_to") or {}).items():
            good = [v for v in vals if v in allowed.get(k, [])]
            if good:
                new_meta.setdefault("applies_to", {})[k] = good
            if len(good) < len(vals):
                issues.append(f"applies_to.{k}")
        if role:
            new_meta["role"] = role
        if r.get("drop"):
            stats["kept despite drop"] += 1
            issues.append("kept(" + (r.get("drop_reason") or "drop") + ")")
        new_meta["confidence"] = r.get("confidence", "")
        new_meta["stage3"] = r["_batch"]
        if issues:
            new_meta["stage3_issues"] = issues
        write_unit(refined_dir / p.name, new_meta, out_body)
        stats[t] += 1
        n_ex = 0
        for i, x in enumerate(r.get("extracted") or [], 1):
            xbody = (x.get("body") or "").strip()
            xnew, _ = word_check(variants, xbody)
            if len(xbody) < MIN_EXTRACT_CHARS or xnew > NEW_WORD_SHARE or x.get("type") not in TYPES:
                issues.append(f"extracted{i}")
                continue
            xid = f"x-{meta['id']}-{i}"
            xmeta = {"id": xid, "type": x["type"], "domain": new_meta["domain"], "title": (x.get("title") or "").strip() or meta["title"],
                     "status": "draft", "collection": meta.get("collection"), "book": meta.get("book"), "chapter": meta.get("chapter"),
                     "extracted_from": meta["id"], "source": meta.get("source"), "page": meta.get("page"),
                     "license": meta.get("license"), "mode": meta.get("mode"), "stage3": r["_batch"]}
            if x["type"] == "troubleshooting" and x.get("symptoms"):
                xmeta["symptoms"] = [s for s in x["symptoms"] if isinstance(s, str) and s.strip()]
            write_unit(refined_dir / f"{xid}.md", xmeta, xbody)
            n_ex += 1
        stats["extracted"] += n_ex
        rows.append([meta["id"], t, r.get("confidence", ""), "; ".join(issues), f"{n_ex} extracted" if n_ex else ""])
    if report:
        with open(report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["id", "type", "confidence", "issues", "note"])
            w.writerows(rows)
    print(f"{len(rows)} units: {dict(stats)} -> {refined_dir}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
    if not args:
        print(__doc__)
        sys.exit(1)
    cmd = args[0]
    if cmd == "prepare":
        prepare(args[1], args[2], int(opts.get("batch-size", BATCH_SIZE)),
                roles=set(opts["roles"].split(",")) if opts.get("roles") else None, first=int(opts.get("first", 1)))
    elif cmd == "submit":
        submit(args[1], opts.get("model", MODEL))
    elif cmd == "fetch":
        fetch(args[1], args[2])
    elif cmd == "merge":
        merge(args[1], args[2], args[3], opts.get("report"))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
