#!/usr/bin/env python3
"""routes2ku: one routing unit per domain, "which procedure for which task, in which order".

The CMSIS Developer Assistant ships a router skill per category (cmsis-project, cmsis-bring-up,
cmsis-pack): a table of the member skills and a typical workflow. Without skills that entry point
is gone. This script writes the same thing as a knowledge unit of type concept, id route-<domain>,
from the procedures that exist in the given unit folders and from the category texts of the
extension's scripts/skills.config.json. A domain without a category text gets the table alone.

Usage: python routes2ku.py <CMSIS-Developer-Assistant/scripts/skills.config.json> <out-dir> <units-dir> [<units-dir> ...]
"""
import json, re, sys
from pathlib import Path
import yaml

MIN_MEMBERS = 2
SUMMARY_WORDS = 40
LABELS = {"debug": "Live debugging", "devops": "DevOps", "ethos-u": "Ethos-U NPU"}


def frontmatter(p):
    m = re.match(r"---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


def one_line(text, words=30):
    first = re.split(r"(?<=[.!?])\s", " ".join(str(text).split()), maxsplit=1)[0]
    parts = first.split()
    return first if len(parts) <= words else " ".join(parts[:words]) + " …"


def main(config, out, unit_dirs):
    out = Path(out)
    categories = {c["id"]: c for c in json.loads(Path(config).read_text(encoding="utf-8"))["categories"]}
    by_domain = {}
    for d in unit_dirs:
        for p in sorted(Path(d).rglob("proc-*.md")):
            fm = frontmatter(p)
            if fm.get("type") == "procedure" and fm.get("domain"):
                by_domain.setdefault(fm["domain"], []).append(fm)
    written = 0
    for domain, members in sorted(by_domain.items()):
        if len(members) < MIN_MEMBERS:
            continue
        members.sort(key=lambda fm: fm["id"])
        cat = categories.get(domain, {})
        label = cat.get("label") or LABELS.get(domain) or domain
        ids = {fm["title"]: fm["id"] for fm in members}

        def to_id(match):
            # `$name` of a skill becomes the id of its procedure; an unknown name stays as it is.
            name = match.group(1)
            return f"`{ids[name]}`" if name in ids else match.group(0)

        rows = [f"| {one_line(fm.get('summary', '')).replace('|', '/')} | `{fm['id']}` |" for fm in members]
        body = [f"# {label}: which procedure", "",
                "Read the procedure with `knowledge_get` before acting on it, and follow its own "
                "prerequisites and guardrails. A `$name` inside a procedure is the procedure `proc-<name>`.", "",
                "| If the task is to … | Procedure |", "|---|---|", *rows]
        if cat.get("workflow"):
            body += ["", "## Typical order", ""]
            body += [f"{i}. {re.sub(r'`[$/]([a-z][a-z0-9-]+)`', to_id, line)}" for i, line in enumerate(cat["workflow"], 1)]
        summary = f"{cat.get('shortDescription') or label}: which procedure fits a task, and the usual order."
        assert len(summary.split()) <= SUMMARY_WORDS, summary
        meta = dict(type="concept", domain=domain, title=f"{label}: which procedure", summary=summary,
                    triggers=[cat["description"]] if cat.get("description") else [], status="draft",
                    source="CMSIS-Developer-Assistant/scripts/skills.config.json", id=f"route-{domain}",
                    references=[fm["id"] for fm in members])
        p = out / "concept" / f"route-{domain}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        fmtxt = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items() if v not in ("", []))
        p.write_text(f"---\n{fmtxt}\n---\n\n" + "\n".join(body) + "\n", encoding="utf-8")
        written += 1
        print(f"route-{domain}: {len(members)} procedures{', with workflow' if cat.get('workflow') else ''}")
    print(f"Routing units: {written}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
