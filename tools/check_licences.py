#!/usr/bin/env python3
"""check_licences: the licence gate of an index build.

Every knowledge unit of the given folders must say in its frontmatter under which licence its text may
be served: Apache-2.0, MIT or BSD-3-Clause for text taken from the source (mode V), or the marker
"own summary of a GitHub issue" the issue digests carry (mode S). A missing field, any other value
(CC BY-SA in particular, which waits for the legal review) and mode P (private, the book units) fail
the gate: exit 1 and the files listed. A folder without units fails too, so that a recipe cannot lose
a folder unnoticed. scripts/build_core.sh runs the gate before it builds the shipped index.

Usage: python tools/check_licences.py <units-dir> [<units-dir> ...]
"""
import re, sys
from collections import Counter
from pathlib import Path
import yaml

ALLOWED = ("Apache-2.0", "MIT", "BSD-3-Clause", "own summary of a GitHub issue")
PRIVATE_MODE = "P"


def frontmatter(p):
    m = re.match(r"---\n(.*?)\n---", p.read_text(encoding="utf-8"), re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def main(dirs):
    bad, counts = [], Counter()
    for d in dirs:
        files = sorted(Path(d).rglob("*.md"))
        if not files:
            bad.append(f"{d}: no units")
        for p in files:
            try:
                meta = frontmatter(p)
            except yaml.YAMLError as ex:
                bad.append(f"{p}: frontmatter does not parse ({ex})")
                continue
            lic, mode = meta.get("license"), meta.get("mode")
            if lic is None:
                bad.append(f"{p}: no license field")
            elif lic not in ALLOWED:
                bad.append(f"{p}: license '{lic}' is not allowed")
            if str(mode) == PRIVATE_MODE:
                bad.append(f"{p}: mode P (private)")
            counts[str(lic)] += 1
    for lic, n in sorted(counts.items()):
        print(f"{n:6d}  {lic}")
    if bad:
        print(f"licence gate: {len(bad)} problems", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print(f"licence gate: {sum(counts.values())} units in {len(dirs)} folders, all allowed")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1:]))
