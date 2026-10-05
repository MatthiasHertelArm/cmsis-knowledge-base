"""Apply the source analysis of tool messages to the troubleshooting units of errcat.py.

Usage: python errcat_merge.py <units/troubleshooting> <stage2/errcat-out> [repo@commit the analysis read]

Every file in <stage2/errcat-out> is a JSON list of results, one per message:
  {id, cause, fix, evidence: ["path:line[-line]", ...], confidence: high|medium|low|unknown, note}
They were worked out from the devtools source (no tool was run), so they stay status draft.

For each result the unit <id>.md gets:
  - ## Cause and ## Fix replaced by the result where it has one, unless its confidence is unknown;
  - ## Note with the note, when there is one;
  - ## Evidence: the source lines and the confidence;
  - summary: the first sentence of the cause;
  - frontmatter cause_origin "source-analysis", confidence, evidence, and doc_cause with the
    README text the cause replaced, so the review can compare.
Results whose unit does not exist are reported and skipped. Run it after errcat.py.
"""
import json
import re
import sys
from pathlib import Path

PLACEHOLDER = re.compile(r"^_[^_\n]+_$")
SECTION = re.compile(r"^## (.+)$", re.M)


def read_unit(path):
    text = path.read_text(encoding="utf-8")
    _, fm, body = text.split("---\n", 2)
    meta = {}
    for line in fm.strip().splitlines():
        key, _, value = line.partition(": ")
        meta[key] = json.loads(value)
    return meta, body.strip()


def sections(body):
    """The body as an ordered list of (heading, text)."""
    parts = SECTION.split(body)
    out = []
    for i in range(1, len(parts), 2):
        out.append((parts[i].strip(), parts[i + 1].strip()))
    return out


def write_unit(path, meta, secs):
    meta = {k: v for k, v in meta.items() if v not in ("", [], None)}
    fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    body = "\n\n".join(f"## {h}\n\n{t}" for h, t in secs)
    path.write_text(f"---\n{fm}\n---\n\n{body}\n", encoding="utf-8")


def summary_of(cause, words=40):
    """The first sentence of the cause, at most `words` words: what a search hit shows."""
    first = re.split(r"(?<=[.!?])\s+(?=[A-Z<`'\"(])", " ".join(cause.split()), maxsplit=1)[0]
    w = first.split()
    return first if len(w) <= words else " ".join(w[:words - 1]) + " …"


def text_of(value):
    return value.strip() if isinstance(value, str) else ""


def merge(units, results, ref):
    stats = {"merged": 0, "unknown": 0, "missing": 0}
    for res in results:
        path = units / f"{res['id']}.md"
        if not path.exists():
            print(f"  no unit for {res['id']}")
            stats["missing"] += 1
            continue
        meta, body = read_unit(path)
        if not str(meta.get("source", "")).startswith(ref + ":"):
            print(f"  {res['id']}: unit built from {meta.get('source')}, analysis read {ref}; check the evidence lines")
        secs = [s for s in sections(body) if s[0] not in ("Note", "Evidence")]
        get = dict(secs)
        old_cause = get.get("Cause", "")
        cause, fix, note = text_of(res.get("cause")), text_of(res.get("fix")), text_of(res.get("note"))
        confidence = res.get("confidence", "unknown")
        if confidence == "unknown":
            stats["unknown"] += 1
            cause = fix = ""
        else:
            stats["merged"] += 1
            if cause and old_cause and not PLACEHOLDER.match(old_cause) and old_cause != cause:
                meta["doc_cause"] = old_cause
        new = []
        for heading, text in secs:
            if heading == "Cause" and cause:
                text = cause
            elif heading == "Fix" and fix:
                text = fix
            new.append((heading, text))
        if note:
            new.append(("Note", note))
        evidence = [e for e in res.get("evidence", []) if isinstance(e, str) and e.strip()]
        if evidence:
            lines = "\n".join(f"- `{e.strip()}`" for e in evidence)
            new.append(("Evidence", f"Read from the source of {ref}, confidence {confidence}, not reviewed yet:\n\n{lines}"))
        shown = cause or ("" if PLACEHOLDER.match(old_cause) else old_cause)
        if shown and confidence != "unknown":
            meta["summary"] = summary_of(shown)
        meta["cause_origin"] = "source-analysis"
        meta["confidence"] = confidence
        meta["evidence"] = [f"{ref}:{e.strip()}" for e in evidence]
        write_unit(path, meta, new)
    return stats


# The commit the analysis read: its line numbers hold for this commit only.
ANALYSED = "Open-CMSIS-Pack/devtools@30f5e817"


def main(units, results_dir, ref=ANALYSED):
    units, results_dir = Path(units), Path(results_dir)
    total = {"merged": 0, "unknown": 0, "missing": 0}
    for f in sorted(results_dir.glob("*.json")):
        results = json.loads(f.read_text(encoding="utf-8"))
        stats = merge(units, results, ref)
        print(f"{f.stem:14s} {len(results):4d} results: {stats['merged']} merged, "
              f"{stats['unknown']} unknown, {stats['missing']} without a unit")
        for k in total:
            total[k] += stats[k]
    print(f"total          merged {total['merged']}, unknown {total['unknown']}, without a unit {total['missing']}")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(*sys.argv[1:])
