#!/usr/bin/env bash
# Two indexes instead of one: the core (tool messages, procedures, rules, routes, issue digests) for
# knowledge.indexPath, and a pack index of the converted documentation (units/docs) that an installed
# pack carries as .knowledge/knowledge.db. The pack index keeps only the entities its units point at; the device
# graph stays in the core, and the extension reads both as one set.
# Usage: scripts/build_split.sh   (writes build/knowledge.core.db and packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db)
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
CORE=(--units units/skills --units units/canonical --units units/extracted --units units/troubleshooting
      --units units/cda-skills --units units/cda-routes --units units/issues)
$PY tools/build_index.py --no-vec "${CORE[@]}" --entities build/entities --out build/knowledge.core.db
# The documentation collections the review keeps: one folder per collection under units/docs, listed in
# sources/sources-review.csv with tier "pack" (the debug-adapters folder belongs to debug-adapter-registry).
PACK_UNITS=()
while IFS= read -r coll; do
  [ -d "units/docs/$coll" ] && PACK_UNITS+=(--units "units/docs/$coll")
  [ "$coll" = debug-adapter-registry ] && PACK_UNITS+=(--units units/docs/debug-adapters)
done < <($PY -c "import csv; [print(r['collection']) for r in csv.DictReader(open('sources/sources-review.csv')) if r['tier']=='pack' and r['collection']]")
mkdir -p packs/Local.CMSIS_Knowledge/.knowledge
$PY tools/build_index.py --no-vec "${PACK_UNITS[@]}" --entities build/entities --out packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db
sqlite3 packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db "
  DELETE FROM nodes WHERE kind='entity' AND type NOT IN ('core','toolchain','tool','api')
    AND id NOT IN (SELECT dst FROM edges WHERE src IN (SELECT id FROM nodes WHERE kind='knowledge'));
  DELETE FROM edges WHERE src NOT IN (SELECT id FROM nodes) OR dst NOT IN (SELECT id FROM nodes);
  VACUUM;"
ls -la build/knowledge.core.db packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db
