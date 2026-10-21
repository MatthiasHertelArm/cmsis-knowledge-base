#!/usr/bin/env bash
# One local pack from named book collections: the refined units of a book when they exist, else the converted
# ones, plus its generic units; tool, project and other units left out (stage2/books-exclusions.json);
# edges into the core indexes allowed. Installed into the pack root unless INSTALL=0.
# Usage: scripts/build_pack.sh <Pack> <collection> [<collection> ...]   e.g. CPP_Architecture softwarearchitecturewithcplusplusseconde
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
NAME="$1"; shift
PACK="packs/Local.$NAME"
UNITS=()
for b in "$@"; do
  if [ -d "units/books-refined/$b" ]; then UNITS+=(--units "units/books-refined/$b"); else UNITS+=(--units "units/books/$b"); fi
  [ -d "units/books-generic/$b" ] && UNITS+=(--units "units/books-generic/$b")
done
KNOWN=(); for k in build/knowledge.core.db packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db; do [ -f "$k" ] && KNOWN+=(--known "$k"); done
EXCL=(); [ -f stage2/books-exclusions.json ] && EXCL+=(--exclude stage2/books-exclusions.json)
mkdir -p "$PACK/.knowledge"
$PY tools/build_index.py --no-vec "${UNITS[@]}" --entities build/entities "${KNOWN[@]}" "${EXCL[@]}" --out "$PACK/.knowledge/knowledge.db"
sqlite3 "$PACK/.knowledge/knowledge.db" "
  DELETE FROM nodes WHERE kind='entity' AND type NOT IN ('core','toolchain','tool','api')
    AND id NOT IN (SELECT dst FROM edges WHERE src IN (SELECT id FROM nodes WHERE kind='knowledge'));
  DELETE FROM edges WHERE src NOT IN (SELECT id FROM nodes)
    OR (dst NOT IN (SELECT id FROM nodes) AND rel NOT IN ('references', 'requires', 'refines'));
  VACUUM;"
ls -la "$PACK"
if [ "${INSTALL:-1}" != 0 ]; then
  ROOT="${CMSIS_PACK_ROOT:-$HOME/.cache/arm/packs}"
  VERSION=$(sed -n 's/.*<release version="\([^"]*\)".*/\1/p' "$PACK"/*.pdsc | head -1)
  DEST="$ROOT/Local/$NAME/$VERSION"
  mkdir -p "$DEST" && cp "$PACK"/*.pdsc "$PACK"/LICENSE.txt "$DEST"/ && mkdir -p "$DEST/.knowledge" && cp "$PACK/.knowledge/knowledge.db" "$DEST/.knowledge/"
  echo "installed into $DEST"
fi
