"""List the troubleshooting units that a person still has to review, as CSV: the error catalog or the issue digests.

Usage: python review_csv.py <units/troubleshooting | units/issues> <out.csv>

One row per draft unit, the least certain first. Error catalog: units without a cause, then the
causes from the source analysis by confidence (unknown, low, medium, high), then README texts.
Issue digests: those the check found unsupported, then corrected, then supported, each by confidence.
The file starts with a BOM so that Excel reads it as UTF-8; reviewer and comment are empty
columns to fill in.
"""
import csv
import re
import sys
from pathlib import Path

from errcat_merge import PLACEHOLDER, read_unit, sections

ORDER = {"write cause and fix": 0, "unknown": 1, "low": 2, "medium": 3, "high": 4, "check README text": 5}
COLUMNS = ["needs", "confidence", "checked", "tool", "code", "severity", "message", "id", "title", "cause", "fix", "note",
           "doc_cause", "evidence", "source", "unit_file", "reviewer", "comment"]


def row(path, root):
    meta, body = read_unit(path)
    if meta.get("status") != "draft":
        return None
    secs = dict(sections(body))
    cause, fix = secs.get("Cause", ""), secs.get("Fix", "")
    blank = lambda s: "" if PLACEHOLDER.match(s) else s
    confidence = meta.get("confidence", "")
    if not blank(cause):
        needs = "write cause and fix"
    elif meta.get("cause_origin") == "source-analysis":
        needs = "review cause and fix"
    elif meta.get("cause_origin") == "issue-digest":
        needs = "review digest against the thread" if meta.get("checked") == "unsupported" else "review digest"
    else:
        needs = "check README text"
    symptoms = meta.get("symptoms", [])
    return {
        "needs": needs, "confidence": confidence, "tool": meta.get("tool", ""), "code": meta.get("code", ""),
        "severity": meta.get("severity", ""), "message": symptoms[-1] if symptoms else "", "id": meta["id"],
        "title": meta.get("title", ""), "checked": meta.get("checked", ""),
        "cause": blank(cause), "fix": blank(fix), "note": secs.get("Note", ""), "doc_cause": meta.get("doc_cause", ""),
        "evidence": "\n".join(meta.get("evidence", [])), "source": meta.get("source", ""),
        "unit_file": str(path.relative_to(root)), "reviewer": "", "comment": "",
    }


def main(units, out):
    units, out = Path(units), Path(out)
    root = units.parent.parent if units.parent.name == "units" else units.parent
    rows = [r for r in (row(p, root) for p in sorted(units.rglob("*.md"))) if r]
    check = {"unsupported": 0, "partly": 1, "supported": 2}
    def rank(r):
        if r["checked"]:                                    # issue digests: unsupported first, then by confidence
            return (check.get(r["checked"], 3), ORDER.get(r["confidence"], 9))
        if r["needs"] == "review cause and fix":            # error catalog: by confidence of the source analysis
            return (0, ORDER.get(r["confidence"], 9))
        return (0, ORDER.get(r["needs"], 9))
    rows.sort(key=lambda r: (rank(r), r["tool"], r["code"] or r["message"]))
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)
    counts = {}
    for r in rows:
        key = r["needs"] + (f" ({r['confidence']})" if r["confidence"] else "")
        counts[key] = counts.get(key, 0) + 1
    print(f"{len(rows)} rows -> {out}")
    for k, v in sorted(counts.items()):
        print(f"  {v:4d}  {k}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.path.insert(0, str(Path(__file__).parent))
    main(*sys.argv[1:])
