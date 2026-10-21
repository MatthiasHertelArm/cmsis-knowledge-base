#!/usr/bin/env python3
"""route_refs: `$name` hand-overs to skills that are not installed become links to their procedure units.

The extension installs cmsis-help alone; the other skills are knowledge units (proc-<name>). A unit text
that still says `$start-cmsis-project` would send the agent to a skill it does not have. This rewrites
every such reference in the unit files of the given folders (frontmatter and body alike), with the
rule of skill2ku.route_refs. Targets are the proc-* units found in the folders named by --targets.

Usage: python3 tools/route_refs.py --targets units/skills --targets units/cda-skills <folder> [<folder> ...]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill2ku import route_refs  # noqa: E402


def main(argv):
    targets_from, folders = [], []
    it = iter(argv)
    for a in it:
        if a == "--targets":
            targets_from.append(next(it))
        else:
            folders.append(a)
    targets = {p.stem[5:] for d in targets_from for p in Path(d).rglob("proc-*.md")}
    changed = 0
    for d in folders:
        for p in Path(d).rglob("*.md"):
            text = p.read_text(encoding="utf-8")
            new = route_refs(text, targets)
            if new != text:
                p.write_text(new, encoding="utf-8")
                changed += 1
    print(f"route_refs: {len(targets)} procedure units, {changed} files rewritten")


if __name__ == "__main__":
    main(sys.argv[1:])
