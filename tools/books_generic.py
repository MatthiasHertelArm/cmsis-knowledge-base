#!/usr/bin/env python3
"""books_generic: generic knowledge out of refined book units, checked against the core knowledge base.

Two model passes (Claude Haiku 5.5 as reader agents, or the Message Batches API), each with a script
before and after it:

  extract-prepare <refined-dir> <in-dir>             batch files of the refined units (stage2/books_generic_prompt.md)
  extract-merge   <refined-dir> <out-dir> <pieces.json> [--report=csv]
        the readers' pieces, checked: the evidence quote must be in the source unit, summaries stay within
        40 words, bodies within 40 to 260 words, types, domains and applies_to values come from the lists,
        a piece that repeats another of the same book is dropped; the survivors go to pieces.json
  check-prepare   <pieces.json> <in-dir> --index=<knowledge.db> [--index=...]
        for each piece the five nearest units of the core indexes (BM25 of the prototype search), as batch
        files for the conflict check (stage2/books_conflict_prompt.md)
  check-merge     <pieces.json> <out-dir> <generic-dir> [--review-dir=dir] [--report=csv]
  classify-prepare <in-dir> <unit-dir> [<unit-dir> ...] [--batch-size=400]
        batch files for the scope classification (stage2/books_scope_prompt.md): coding and design knowledge
        stays, tool usage, project management and the rest leave the pack
  classify-merge   <out-dir> <unit-dir> [<unit-dir> ...] [--report=csv]
        writes `scope` into each unit's frontmatter and lists tool, project and other units in
        stage2/books-exclusions.json, which build_index.py --exclude and both merges honour
  request-merge   <judge-out-dir> <unit-dir> [<unit-dir> ...] [--review-dir=dir] [--report=csv]
        the judgements of tests/eval_conflicts.py's batches (stage2/books_request_conflict_prompt.md): a unit
        that contradicts the core for any request is moved out of the unit dirs into the review dir and listed
        in stage2/books-exclusions.json, which stage3_books.py merge and check-merge honour; a unit that
        diverts for a request gets the request and the note as `caution` in its frontmatter
        keep: the unit is written with `references` to the core units it complements; drop (a duplicate of
        the core): not written; review (a contradiction): written to the review dir with the notes, not to
        the pack

Units are mode S: own words, with the book page and a verbatim evidence quote in the frontmatter.
Usage: python books_generic.py <command> ... [--batch-size=20]
"""
import csv, json, re, sqlite3, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from stage3_books import (DOMAINS, TYPES, allowed_lists, read_unit, write_unit, words)  # noqa: E402

EXTRACT_PROMPT = ROOT / "stage2" / "books_generic_prompt.md"
CONFLICT_PROMPT = ROOT / "stage2" / "books_conflict_prompt.md"
BATCH_SIZE = 20
EVIDENCE_MAX = 320
BODY_WORDS = (40, 260)
DUP_JACCARD = 0.5
STOP_WORDS = {"a", "an", "the", "of", "to", "in", "on", "for", "and", "or", "its", "is", "are", "s", "with", "by", "from",
              "as", "at", "be", "it", "that", "this", "before", "after", "into", "when", "than", "not", "each", "any"}
CANDIDATES = 5
EXCERPT = 600
FIELD_KEYS = {"rule": ("severity", "rationale"), "pattern": ("problem", "solution", "tradeoffs"),
              "troubleshooting": ("symptoms", "cause", "fix"), "procedure": ("steps", "verification"), "concept": ()}


def slug(s, n=60):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-")


def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace(" ", " ")
    return re.sub(r"[\s`*_#>|-]+", " ", s).strip().lower()


def content_words(text):
    return {w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP_WORDS}


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def load_units(refined_dir):
    out = {}
    for p in sorted(Path(refined_dir).glob("*.md")):
        meta, body = read_unit(p)
        out[meta["id"]] = (meta, body)
    return out


# ── pass 1: extraction ──────────────────────────────────────────────────────

def extract_prepare(refined_dir, in_dir, batch_size):
    in_dir = Path(in_dir)
    in_dir.mkdir(parents=True, exist_ok=True)
    for old in in_dir.glob("batch-*.json"):
        old.unlink()
    units = [{"id": m["id"], "title": m["title"], "type": m.get("type", "concept"), "summary": m.get("summary", ""), "body": b}
             for m, b in load_units(refined_dir).values() if m.get("id") and not m["id"].startswith("x-")]
    prompt, allowed = EXTRACT_PROMPT.read_text(encoding="utf-8"), allowed_lists()
    n = 0
    for i in range(0, len(units), batch_size):
        n += 1
        (in_dir / f"batch-{n:02d}.json").write_text(
            json.dumps({"prompt": prompt, "allowed": allowed, "units": units[i:i + batch_size]}, ensure_ascii=False, indent=1),
            encoding="utf-8")
    print(f"{len(units)} units in {n} batches -> {in_dir}")


def extract_merge(refined_dir, out_dir, pieces_file, report):
    units = load_units(refined_dir)
    allowed = allowed_lists()
    rows, kept, stats = [], [], Counter()
    seen_words = []
    for f in sorted(Path(out_dir).glob("batch-*.json")):
        for p in json.loads(f.read_text(encoding="utf-8")):
            issues = []
            src = units.get(p.get("from", ""))
            if src is None:
                issues.append("unknown source unit")
            ev = norm(p.get("evidence") or "")
            if not ev or len(p.get("evidence") or "") > EVIDENCE_MAX:
                issues.append("evidence missing or too long")
            elif src and ev not in norm(src[1]) and ev not in norm(src[0].get("summary", "")):
                issues.append("evidence not in source")
            if p.get("type") not in TYPES:
                issues.append("type")
            if p.get("domain") not in DOMAINS:
                issues.append("domain")
            s = (p.get("summary") or "").split()
            if not 0 < len(s) <= 40:
                issues.append("summary")
            nb = len((p.get("body") or "").split())
            if not BODY_WORDS[0] <= nb <= BODY_WORDS[1]:
                issues.append(f"body {nb} words")
            if not (p.get("title") or "").strip():
                issues.append("title")
            bad = [f"{k}:{v}" for k, vals in (p.get("applies_to") or {}).items() for v in vals if v not in allowed.get(k, [])]
            if bad:
                issues.append("applies_to " + ",".join(bad))
                p["applies_to"] = {k: [v for v in vals if v in allowed.get(k, [])] for k, vals in p["applies_to"].items()}
            # a repeat of another piece of the same book: the same claim under another title ("...before writing
            # its registers" / "...before touching its registers"), judged on the words of title and summary
            if not issues:
                t = content_words(p["title"])
                ts = content_words(p["title"] + " " + p["summary"])
                if any(jaccard(t, o) >= DUP_JACCARD or jaccard(ts, os) >= DUP_JACCARD for o, os in seen_words):
                    issues.append("repeats an earlier piece")
                else:
                    seen_words.append((t, ts))
            if issues:
                stats["rejected"] += 1
                rows.append([p.get("from", ""), p.get("title", ""), p.get("type", ""), "; ".join(issues)])
                continue
            meta, _ = src
            prefix = meta["id"].split("-ch", 1)[0]
            pid = f"g-{prefix}-{slug(p['title'])}"
            n = 2
            while any(k["id"] == pid for k in kept):
                pid = f"g-{prefix}-{slug(p['title'], 56)}-{n}"
                n += 1
            p["id"] = pid
            p["_source"] = {k: meta.get(k) for k in ("collection", "book", "chapter", "source", "page", "license")}
            kept.append(p)
            stats[p["type"]] += 1
            rows.append([p["from"], p["title"], p["type"], ""])
    Path(pieces_file).write_text(json.dumps(kept, ensure_ascii=False, indent=1), encoding="utf-8")
    if report:
        with open(report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["from", "title", "type", "issues"])
            w.writerows(rows)
    print(f"{len(rows)} pieces read, {len(kept)} kept: {dict(stats)} -> {pieces_file}")


# ── pass 2: conflict check against the core ─────────────────────────────────

def check_prepare(pieces_file, in_dir, indexes, batch_size):
    from kb_lib import KB
    pieces = json.loads(Path(pieces_file).read_text(encoding="utf-8"))
    kbs = [(Path(ix).name, KB(ix, use_vec=False), sqlite3.connect(ix)) for ix in indexes]
    in_dir = Path(in_dir)
    in_dir.mkdir(parents=True, exist_ok=True)
    for old in in_dir.glob("batch-*.json"):
        old.unlink()
    items = []
    for p in pieces:
        query = f"{p['title']} {p['summary']}"
        found = []
        for name, kb, con in kbs:
            for r in kb.search(query, k=CANDIDATES, budget=100000)["results"]:
                row = con.execute("SELECT type, title, summary, body FROM nodes WHERE id=?", (r["id"],)).fetchone()
                if row:
                    found.append({"id": r["id"], "score": r["score"], "index": name, "type": row[0], "title": row[1],
                                  "summary": row[2] or "", "body": (row[3] or "")[:EXCERPT]})
        found.sort(key=lambda c: -c["score"])
        cands, ids = [], set()
        for c in found:
            if c["id"] not in ids:
                ids.add(c["id"])
                cands.append({k: c[k] for k in ("id", "type", "title", "summary", "body")})
            if len(cands) == CANDIDATES:
                break
        items.append({"id": p["id"], "type": p["type"], "title": p["title"], "summary": p["summary"], "body": p["body"],
                      "candidates": cands})
    prompt = CONFLICT_PROMPT.read_text(encoding="utf-8")
    n = 0
    for i in range(0, len(items), batch_size):
        n += 1
        (in_dir / f"batch-{n:02d}.json").write_text(json.dumps({"prompt": prompt, "pieces": items[i:i + batch_size]},
                                                               ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(items)} pieces with candidates in {n} batches -> {in_dir}")


def check_merge(pieces_file, out_dir, generic_dir, review_dir, report):
    pieces = {p["id"]: p for p in json.loads(Path(pieces_file).read_text(encoding="utf-8"))}
    decisions = {}
    for f in sorted(Path(out_dir).glob("batch-*.json")):
        for d in json.loads(f.read_text(encoding="utf-8")):
            decisions[d.get("id")] = d
    generic_dir, review_dir = Path(generic_dir), Path(review_dir) if review_dir else None
    for d in (generic_dir, review_dir):
        if d and d.exists():
            for old in d.glob("*.md"):
                old.unlink()
    rows, stats = [], Counter()
    excl = exclusions()
    for pid, p in pieces.items():
        if pid in excl:
            stats["excluded earlier"] += 1
            rows.append([pid, p["type"], "excluded", "", "", excl[pid].get("reason", "")])
            continue
        d = decisions.get(pid)
        if d is None:
            decision, cands = "keep", []
            stats["unchecked"] += 1
        else:
            decision, cands = d.get("decision", "keep"), d.get("candidates") or []
        if decision not in ("keep", "drop", "review"):
            decision = "review"
        complements = [c["id"] for c in cands if c.get("relation") == "complements"]
        conflicts = [(c["id"], c.get("note", "")) for c in cands if c.get("relation") == "contradicts"]
        duplicates = [c["id"] for c in cands if c.get("relation") == "duplicate"]
        src = p["_source"]
        meta = {"id": pid, "type": p["type"], "domain": p["domain"], "title": p["title"].strip(), "summary": p["summary"].strip(),
                "status": "draft", "collection": src.get("collection"), "book": src.get("book"), "chapter": src.get("chapter"),
                "derived_from": p["from"], "source": src.get("source"), "page": src.get("page"), "evidence": p["evidence"],
                "license": src.get("license"), "mode": "S", "triggers": p.get("triggers") or [], "confidence": p.get("confidence", ""),
                "stage": "generic"}
        for k in FIELD_KEYS.get(p["type"], ()):
            v = (p.get("fields") or {}).get(k)
            if v:
                meta[k] = v
        if any(v for v in (p.get("applies_to") or {}).values()):
            meta["applies_to"] = {k: v for k, v in p["applies_to"].items() if v}
        if complements:
            meta["references"] = complements
        if decision == "keep":
            write_unit(generic_dir / f"{pid}.md", meta, p["body"])
        elif decision == "review" and review_dir:
            meta["conflicts_with_core"] = [c for c, _ in conflicts]
            meta["conflict_notes"] = [n for _, n in conflicts if n]
            write_unit(review_dir / f"{pid}.md", meta, p["body"])
        stats[decision] += 1
        rows.append([pid, p["type"], decision, ";".join(duplicates), ";".join(complements),
                     " | ".join(f"{c}: {n}" for c, n in conflicts)])
    if report:
        with open(report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["id", "type", "decision", "duplicates", "complements", "contradictions"])
            w.writerows(rows)
    print(f"{len(rows)} pieces: {dict(stats)} -> {generic_dir}" + (f", review in {review_dir}" if review_dir else ""))


EXCLUSIONS = ROOT / "stage2" / "books-exclusions.json"


def exclusions():
    return json.loads(EXCLUSIONS.read_text(encoding="utf-8")) if EXCLUSIONS.exists() else {}


def request_merge(out_dir, unit_dirs, review_dir, report):
    """Apply the request-side judgements to the units they name."""
    per_unit = {}
    for f in sorted(Path(out_dir).glob("batch-*.json")):
        for d in json.loads(f.read_text(encoding="utf-8")):
            for u in d.get("units") or []:
                per_unit.setdefault(u.get("id"), []).append((d.get("request", ""), u.get("relation", ""), u.get("note", "")))
    excl = exclusions()
    review_dir = Path(review_dir) if review_dir else None
    rows, stats = [], Counter()
    for uid, judgements in per_unit.items():
        path = next((Path(d) / f"{uid}.md" for d in unit_dirs if (Path(d) / f"{uid}.md").exists()), None)
        contradictions = [(r, n) for r, rel, n in judgements if rel == "contradicts"]
        diversions = [(r, n) for r, rel, n in judgements if rel == "diverts"]
        if path is None:
            rows.append([uid, "not found", "", ""])
            continue
        meta, body = read_unit(path)
        if contradictions:
            excl[uid] = {"reason": "contradicts the core", "requests": [r for r, _ in contradictions], "notes": [n for _, n in contradictions if n]}
            meta["conflicts_with_core"] = [f"{r}: {n}" if n else r for r, n in contradictions]
            if review_dir:
                write_unit(review_dir / path.name, meta, body)
            path.unlink()
            stats["excluded"] += 1
            rows.append([uid, "excluded", "; ".join(r for r, _ in contradictions), " | ".join(n for _, n in contradictions)])
            continue
        if diversions:
            meta["caution"] = [f"{r}: {n}" if n else r for r, n in diversions]
            write_unit(path, meta, body)
            stats["caution"] += 1
            rows.append([uid, "caution", "; ".join(r for r, _ in diversions), " | ".join(n for _, n in diversions)])
        else:
            stats["fine"] += 1
    EXCLUSIONS.write_text(json.dumps(excl, ensure_ascii=False, indent=1), encoding="utf-8")
    if report:
        with open(report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["id", "outcome", "requests", "notes"])
            w.writerows(rows)
    print(f"{len(per_unit)} units judged: {dict(stats)}; exclusions in {EXCLUSIONS}")


SCOPE_PROMPT = ROOT / "stage2" / "books_scope_prompt.md"
SCOPES = ("coding", "design", "tool", "project", "other")
BANNED_SCOPES = ("tool", "project", "other")


def unit_files(unit_dirs):
    for d in unit_dirs:
        for p in sorted(Path(d).glob("*.md")):
            yield p


def classify_prepare(in_dir, unit_dirs, batch_size):
    in_dir = Path(in_dir)
    in_dir.mkdir(parents=True, exist_ok=True)
    for old in in_dir.glob("batch-*.json"):
        old.unlink()
    units = []
    for p in unit_files(unit_dirs):
        meta, body = read_unit(p)
        text = re.sub(r"\s+", " ", body)[:160]
        units.append({"id": meta["id"], "book": meta.get("book", ""), "title": meta.get("title", ""),
                      "summary": meta.get("summary", ""), "excerpt": text})
    prompt = SCOPE_PROMPT.read_text(encoding="utf-8")
    n = 0
    for i in range(0, len(units), batch_size):
        n += 1
        (in_dir / f"batch-{n:02d}.json").write_text(json.dumps({"prompt": prompt, "units": units[i:i + batch_size]},
                                                               ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(units)} units in {n} batches -> {in_dir}")


def classify_merge(out_dir, unit_dirs, report):
    scopes = {}
    for f in sorted(Path(out_dir).glob("batch-*.json")):
        for r in json.loads(f.read_text(encoding="utf-8")):
            if r.get("scope") in SCOPES:
                scopes[r.get("id")] = (r["scope"], r.get("reason", ""))
    excl = exclusions()
    rows, stats = [], Counter()
    for p in unit_files(unit_dirs):
        meta, body = read_unit(p)
        uid = meta["id"]
        if uid not in scopes:
            stats["unclassified"] += 1
            rows.append([uid, meta.get("book", ""), "", "", "unclassified"])
            continue
        scope, reason = scopes[uid]
        meta["scope"] = scope
        write_unit(p, meta, body)
        stats[scope] += 1
        if scope in BANNED_SCOPES:
            excl[uid] = {"reason": f"scope {scope}: {reason}"}
        elif uid in excl and excl[uid].get("reason", "").startswith("scope "):
            del excl[uid]
        rows.append([uid, meta.get("book", ""), scope, reason, ""])
    EXCLUSIONS.write_text(json.dumps(excl, ensure_ascii=False, indent=1), encoding="utf-8")
    if report:
        with open(report, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["id", "book", "scope", "reason", "note"])
            w.writerows(rows)
    print(f"{sum(stats.values())} units: {dict(stats)}; {sum(1 for v in excl.values() if v.get('reason', '').startswith('scope'))} excluded by scope -> {EXCLUSIONS}")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    opts = {}
    for a in sys.argv[1:]:
        if a.startswith("--") and "=" in a:
            k, v = a[2:].split("=", 1)
            opts.setdefault(k, []).append(v)
    one = lambda k, d=None: opts[k][-1] if k in opts else d  # noqa: E731
    if not args:
        print(__doc__)
        sys.exit(1)
    cmd, size = args[0], int(one("batch-size", BATCH_SIZE))
    if cmd == "extract-prepare":
        extract_prepare(args[1], args[2], size)
    elif cmd == "extract-merge":
        extract_merge(args[1], args[2], args[3], one("report"))
    elif cmd == "check-prepare":
        check_prepare(args[1], args[2], opts.get("index", []), size)
    elif cmd == "check-merge":
        check_merge(args[1], args[2], args[3], one("review-dir"), one("report"))
    elif cmd == "classify-prepare":
        classify_prepare(args[1], args[2:], int(one("batch-size", 400)))
    elif cmd == "classify-merge":
        classify_merge(args[1], args[2:], one("report"))
    elif cmd == "request-merge":
        request_merge(args[1], args[2:], one("review-dir"), one("report"))
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
