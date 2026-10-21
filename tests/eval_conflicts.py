#!/usr/bin/env python3
"""Conflicts on the request side: what an agent gets for a generic request once a pack index is read next to the core.

The extension reads several indexes as one set and merges their BM25 lists by rank. This script does the same
over the core index, the documentation pack and a candidate pack (the books), for two kinds of requests:
the golden set of CMSIS questions (tests/golden.json, with the core unit that answers each) and a list of
generic requests an agent makes (tests/agent-requests.json, no expected unit). It reports

  - shadowing: for the golden questions, the rank of the expected core unit with and without the candidate
    pack, and how often a unit of the candidate pack outranks it;
  - exposure: for every request, which candidate-pack units reach the top k;

and writes, for every request where a candidate unit reaches the top k, a batch file for the judge
(stage2/books_request_conflict_prompt.md): the request, the core units that answer it, the candidate units.

Usage: .venv/bin/python tests/eval_conflicts.py --candidate=packs/Local.CPP_Books/.knowledge/knowledge.db
           [--core=build/knowledge.core.db] [--docs=packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db]
           [--k=8] [--out=stage2/books-request-in/<name>] [--batch-size=12]
           [--gate=0.7] [--book-golden=tests/golden-architecture.json]
"""
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from kb_lib import KB  # noqa: E402

RRF_K = 60
EXCERPT = 700

opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
k = int(opts.get("k", 8))
core_db = opts.get("core", "build/knowledge.core.db")
docs_db = opts.get("docs", "packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db")
cand_db = opts["candidate"]
cand_name = Path(cand_db).parent.name
out_dir = Path(opts.get("out", f"stage2/books-request-in/{cand_name}"))
batch_size = int(opts.get("batch-size", 12))
# Weight of a candidate-pack rank in the fusion: 1.0 is the extension's merge (every index places its top
# hits in the set's top), a smaller value models a pack prior.
cand_weight = float(opts.get("candidate-weight", 1.0))
# Relevance gate: a candidate-pack hit enters the fusion only when its BM25 score reaches this share of the
# best BM25 score the base indexes have for the query (0 = no gate, the extension's merge today).
gate = float(opts.get("gate", 0.0))
write_batches = opts.get("batches", "1") != "0"

indexes = [("core", core_db), ("docs", docs_db), ("candidate", cand_db)]
kbs = {name: KB(path, use_vec=False) for name, path in indexes if Path(path).exists()}
cons = {name: sqlite3.connect(path) for name, path in indexes if Path(path).exists()}


def bm25_scores(name, query, n=30):
    """BM25 of the prototype's FTS query, as positive numbers (fts5 reports them negative)."""
    terms = re.findall(r"\w+", query)
    if not terms:
        return {}
    fts = " OR ".join(f'"{t}"' for t in terms)
    rows = cons[name].execute("SELECT id, -bm25(nodes_fts, 0, 8, 4, 1, 6, 6) FROM nodes_fts WHERE nodes_fts MATCH ? "
                              "ORDER BY bm25(nodes_fts, 0, 8, 4, 1, 6, 6) LIMIT ?", (fts, n)).fetchall()
    return {r[0]: r[1] for r in rows}


def fused(query, members, n=k):
    """The set's ranking: each member's BM25 list, fused by rank as the extension does; with `gate`, a
    candidate hit must score at least gate times the base indexes' best BM25 to take part."""
    score, where = {}, {}
    threshold = 0.0
    if gate > 0 and "candidate" in members:
        best = [max(bm25_scores(m, query).values(), default=0.0) for m in members if m != "candidate"]
        threshold = gate * max(best, default=0.0)
    for name in members:
        admitted = bm25_scores(name, query) if (name == "candidate" and threshold > 0) else None
        rank = 0
        for r in kbs[name].search(query, k=30, budget=10 ** 7)["results"]:
            if admitted is not None and admitted.get(r["id"], 0.0) < threshold:
                continue
            score[r["id"]] = score.get(r["id"], 0) + (cand_weight if name == "candidate" else 1.0) / (RRF_K + rank + 1)
            where.setdefault(r["id"], name)
            rank += 1
    top = sorted(score, key=lambda i: -score[i])[:n]
    return [(i, where[i]) for i in top]


def node(name, nid):
    row = cons[name].execute("SELECT id, type, title, summary, body FROM nodes WHERE id=?", (nid,)).fetchone()
    return {"id": row[0], "type": row[1], "title": row[2], "summary": row[3] or "", "body": (row[4] or "")[:EXCERPT]} if row else None


golden = json.loads((ROOT / "tests/golden.json").read_text(encoding="utf-8"))["queries"]
requests_file = ROOT / "tests/agent-requests.json"
generic = json.loads(requests_file.read_text(encoding="utf-8"))["requests"] if requests_file.exists() else []

base = [m for m in kbs if m != "candidate"]
shadowed, moved, exposed, judge_items = 0, 0, 0, []
rank_before = rank_after = 0.0
for g in golden:
    before = [i for i, _ in fused(g["q"], base)]
    after = fused(g["q"], list(kbs))
    rb = next((i for i, x in enumerate(before) if x in g["expect"]), -1)
    ra = next((i for i, (x, _) in enumerate(after) if x in g["expect"]), -1)
    rank_before += 1 / (rb + 1) if rb >= 0 else 0
    rank_after += 1 / (ra + 1) if ra >= 0 else 0
    cands = [(x, src) for x, src in after if src == "candidate"]
    if cands:
        exposed += 1
    if ra != rb:
        moved += 1
    if cands and (ra < 0 or any(after.index((x, "candidate")) < ra for x, _ in cands)):
        shadowed += 1
    if cands:
        judge_items.append({"request": g["q"], "kind": "golden", "expected": g["expect"],
                            "core": [node(src, x) for x, src in after if src != "candidate"][:4] + [node("core", e) or node("docs", e) for e in g["expect"][:1]],
                            "candidate": [node("candidate", x) for x, _ in cands]})
print(f"golden: {len(golden)} questions; MRR without the pack {rank_before/len(golden):.3f}, with it {rank_after/len(golden):.3f}; "
      f"pack unit in the top {k} for {exposed}; expected unit moved for {moved}; pack unit above the expected one for {shadowed}")

books_golden = Path(opts["book-golden"]) if "book-golden" in opts else ROOT / "tests/golden-books.json"
if books_golden.exists() and "candidate" in kbs:
    bq = json.loads(books_golden.read_text(encoding="utf-8"))["queries"]
    hit5 = sum(1 for g in bq if any(x in g["expect"] for x, _ in fused(g["q"], list(kbs), 5)))
    print(f"book questions through the set: {len(bq)}; expected pack unit in the top 5 for {hit5}")

exposed_generic = 0
for q in generic:
    after = fused(q, list(kbs))
    cands = [(x, src) for x, src in after if src == "candidate"]
    if cands:
        exposed_generic += 1
        judge_items.append({"request": q, "kind": "generic", "expected": [],
                            "core": [node(src, x) for x, src in after if src != "candidate"][:4],
                            "candidate": [node("candidate", x) for x, _ in cands]})
print(f"generic requests: {len(generic)}; pack unit in the top {k} for {exposed_generic}")

for item in judge_items:
    item["core"] = [c for c in item["core"] if c]
    seen = set()
    item["core"] = [c for c in item["core"] if not (c["id"] in seen or seen.add(c["id"]))]
if not write_batches:
    sys.exit(0)
out_dir.mkdir(parents=True, exist_ok=True)
for old in out_dir.glob("batch-*.json"):
    old.unlink()
prompt = (ROOT / "stage2/books_request_conflict_prompt.md").read_text(encoding="utf-8")
n = 0
for i in range(0, len(judge_items), batch_size):
    n += 1
    (out_dir / f"batch-{n:02d}.json").write_text(json.dumps({"prompt": prompt, "requests": judge_items[i:i + batch_size]},
                                                             ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(judge_items)} requests with pack units in the top {k}, {n} judge batches -> {out_dir}")
