"""The golden set against the prototype's search (kb_lib), with and without the embeddings.

Usage: .venv/bin/python tests/eval_search.py [build/knowledge.db] [--k=5] [--golden=tests/golden-books.json]
       [--min-hit5=0.85] [--min-mrr=0.65]   exit 1 when BM25 alone scores below a threshold (the CI gate)
Compares BM25 alone with BM25 plus vector search (rank fusion), to judge what embeddings would
add to the extension, whose search is BM25 only (tests/eval_search.js measures that one).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from kb_lib import KB  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
k = int(next((a[4:] for a in sys.argv[1:] if a.startswith("--k=")), 5))
db = Path(args[0]) if args else ROOT / "build/knowledge.db"
golden_file = next((a[9:] for a in sys.argv[1:] if a.startswith("--golden=")), None)
min_hitk = float(next((a[11:] for a in sys.argv[1:] if a.startswith("--min-hit5=")), 0))
min_mrr = float(next((a[10:] for a in sys.argv[1:] if a.startswith("--min-mrr=")), 0))
failed = False
golden = json.loads((Path(golden_file) if golden_file else ROOT / "tests/golden.json").read_text(encoding="utf-8"))["queries"]

for use_vec in (False, True):
    kb = KB(db, use_vec=use_vec)
    if use_vec and kb.vec is None:
        print("vectors: not available (sqlite-vec or fastembed missing)")
        continue
    hit1 = hitk = rr = 0
    for g in golden:
        ctx = {f"tool:{t}" for t in g["tools"]} if g.get("tools") else None
        ids = [r["id"] for r in kb.search(g["q"], k=10, budget=100000, ctx=ctx)["results"]]
        rank = next((i for i, x in enumerate(ids) if x in g["expect"]), -1)
        hit1 += rank == 0
        hitk += 0 <= rank < k
        rr += 1 / (rank + 1) if rank >= 0 else 0
    n = len(golden)
    print(f"{'BM25 + vectors' if use_vec else 'BM25 only':15s} {n} queries  hit@1 {hit1 / n:.2f}  hit@{k} {hitk / n:.2f}  MRR {rr / n:.3f}")
    if not use_vec and (hitk / n < min_hitk or rr / n < min_mrr):
        print(f"FAIL: below the gate hit@{k} {min_hitk} / MRR {min_mrr}")
        failed = True
sys.exit(1 if failed else 0)
