#!/usr/bin/env bash
# The core index the CMSIS Developer Assistant ships as resources/knowledge/core.db: built offline from the
# committed units and build/entities, keyword search only (--no-vec), the licence gate first, the tests after.
# The result records its origin in the table info (kb_commit, kb_dirty, built_at = the commit time, recipe=core).
# Usage: scripts/build_core.sh [out]   (default build/knowledge.core.db)   PY=<python> picks the interpreter.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
OUT="${1:-build/knowledge.core.db}"
# The unit folders of the core, every one of them Apache-2.0, MIT, BSD-3-Clause or an issue digest in own words;
# units/docs-ccbysa (share-alike, decision 4 of HANDOVER.md) and the book units never enter this index.
UNITS=(units/skills units/canonical units/extracted units/troubleshooting
       units/cda-skills units/cda-routes units/docs units/issues)
$PY tools/check_licences.py "${UNITS[@]}"
ARGS=()
for u in "${UNITS[@]}"; do ARGS+=(--units "$u"); done
# The issue digests the readers were least sure of stay out until a human has reviewed them (HANDOVER.md,
# "every issue digest checked against its thread"); the low-confidence error-catalog units stay in, their
# message text is exact whatever the confidence of the cause.
$PY tools/build_index.py --no-vec --recipe core --drop confidence=low,cause_origin=issue-digest \
  "${ARGS[@]}" --entities build/entities --out "$OUT"
KB_INDEX="$OUT" $PY tests/test_kb.py
$PY - "$OUT" <<'PYEOF'
import hashlib, sqlite3, sys
from pathlib import Path
out = Path(sys.argv[1])
for k, v in sqlite3.connect(out).execute("SELECT key, value FROM info ORDER BY rowid"):
    print(f"{k}={v}")
print(f"{out}: {out.stat().st_size} bytes, sha256 {hashlib.sha256(out.read_bytes()).hexdigest()}")
PYEOF
