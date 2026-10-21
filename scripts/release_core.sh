#!/usr/bin/env bash
# Publish the core index as a GitHub release the CMSIS Developer Assistant pins and fetches.
# Builds with scripts/build_core.sh at HEAD, then releases four assets under the tag core-<version>:
#   build/knowledge-core-<version>.db      the index
#   build/knowledge-core-<version>.sha256  its hash, `shasum -a 256` format
#   build/knowledge-core-<version>.json    the index's info table as a JSON object plus file, sha256 and size,
#                                          and sources, sources_sha256: the name and hash of the fourth asset
#   build/SOURCES.md                       the attribution of the index's content (tools/sources_md.py)
# The extension's `npm run knowledge:update -- <version>` reads the JSON and rewrites its lock file.
# Usage: scripts/release_core.sh <version>   (version = date of the release, e.g. 2026.10.21)
# Needs a clean, pushed HEAD and an authenticated `gh`; PY=<python> picks the interpreter.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
VERSION="${1:-}"
if ! [[ "$VERSION" =~ ^[0-9]{4}\.[0-9]{2}\.[0-9]{2}(\.[0-9]+)?$ ]]; then
    echo "usage: $0 <version>   e.g. $0 $(date +%Y.%m.%d)" >&2
    exit 2
fi
TAG="core-$VERSION"
HEAD_SHA=$(git rev-parse HEAD)

# The release must be reproducible from the commit it names: no local changes, HEAD on the remote, tag unused.
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "error: the working tree has uncommitted changes; commit or stash them first" >&2
    exit 1
fi
git fetch -q origin
if ! git merge-base --is-ancestor "$HEAD_SHA" origin/master; then
    echo "error: HEAD $HEAD_SHA is not on origin/master; push it first" >&2
    exit 1
fi
if git rev-parse -q --verify "refs/tags/$TAG" >/dev/null || gh release view "$TAG" >/dev/null 2>&1; then
    echo "error: $TAG exists already; pick another version" >&2
    exit 1
fi

scripts/build_core.sh build/knowledge.core.db

DB="build/knowledge-core-$VERSION.db"
cp build/knowledge.core.db "$DB"
(cd build && shasum -a 256 "knowledge-core-$VERSION.db" > "knowledge-core-$VERSION.sha256")

# The JSON asset and the release notes come from the index's own info table.
NOTES="build/knowledge-core-$VERSION.notes.md"
$PY - "$DB" "$HEAD_SHA" "$VERSION" "$NOTES" <<'PYEOF'
import hashlib, json, sqlite3, sys
from pathlib import Path
db, head, version, notes = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4])
info = {}
for key, value in sqlite3.connect(db).execute("SELECT key, value FROM info ORDER BY rowid"):
    info[key] = int(value) if isinstance(value, str) and value.isdigit() else value
if info.get("kb_dirty") != 0:
    sys.exit(f"error: the index was built from a dirty tree (kb_dirty={info.get('kb_dirty')})")
if info.get("kb_commit") != head:
    sys.exit(f"error: the index names commit {info.get('kb_commit')}, HEAD is {head}")
sha256 = hashlib.sha256(db.read_bytes()).hexdigest()
sources = db.parent / "SOURCES.md"
record = dict(info, file=db.name, sha256=sha256, size=db.stat().st_size,
              sources=sources.name, sources_sha256=hashlib.sha256(sources.read_bytes()).hexdigest())
db.with_suffix(".json").write_text(json.dumps(record, indent=2) + "\n")
licences = ", ".join(f"{k[len('license_'):]} {v}" for k, v in info.items() if k.startswith("license_"))
notes.write_text(f"""Core knowledge index {version} of the CMSIS Knowledge Base, the index the CMSIS Developer Assistant ships as `resources/knowledge/core.db`.

- Units: {info['units']} ({info['nodes']} nodes, {info['edges']} edges; {info['dropped']} issue digests left out by `{info['drop']}`)
- Licences of the units: {licences}
- Built from commit {head} by `scripts/build_core.sh` (recipe `{info['recipe']}`, schema {info['schema_version']}, built_at {info['built_at']}); the same commit gives the same bytes
- `{db.name}`: {db.stat().st_size} bytes, sha256 `{sha256}`
- `SOURCES.md`: the sources of the index with repository, licence and what was taken, the copyright lines and licence texts the licences require (sha256 `{record['sources_sha256']}`)

The extension pins this release with `npm run knowledge:update -- {version}` and fetches it with `npm run knowledge:fetch`.
""")
print(f"{db}: {db.stat().st_size} bytes, sha256 {sha256}")
PYEOF

gh release create "$TAG" --target "$HEAD_SHA" --title "Core knowledge index $VERSION" --notes-file "$NOTES" \
    "$DB" "build/knowledge-core-$VERSION.sha256" "build/knowledge-core-$VERSION.json" build/SOURCES.md
gh release view "$TAG" --json url,assets --jq '.url, (.assets[] | .url)'
