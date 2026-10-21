#!/usr/bin/env bash
# Test scenario for pack-carried knowledge: the books of a folder (PDF) as knowledge units, one per
# section, built into the index of the local pack Local.CPP_Books and installed into the pack root.
# The books are copyrighted: units/books and the pack stay local (git-ignored), never in build/knowledge*.db.
# Usage: scripts/build_books.sh [books-dir]   (default ~/Documents/C++)   Set INSTALL=0 to skip the install.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-.venv/bin/python}
BOOKS="${1:-$HOME/Documents/C++}"
PACK=packs/Local.CPP_Books
# Set CONVERT=0 to keep the converted units; set REFINED=0 to ignore units/books-refined (stage 3 output).
if [ "${CONVERT:-1}" != 0 ]; then
  rm -rf units/books
  $PY tools/pdf2ku.py units/books "$BOOKS"/*.pdf
fi
# Per book, the refined units of tools/stage3_books.py when they exist, else the converted ones.
UNITS=()
for d in units/books/*/; do
  b=$(basename "$d")
  if [ "${REFINED:-1}" != 0 ] && [ -d "units/books-refined/$b" ]; then
    UNITS+=(--units "units/books-refined/$b")
  else
    UNITS+=(--units "$d")
  fi
  # Generic knowledge in own words (tools/books_generic.py), with references into the core indexes.
  [ -d "units/books-generic/$b" ] && UNITS+=(--units "units/books-generic/$b")
done
KNOWN=()
for k in build/knowledge.core.db packs/Local.CMSIS_Knowledge/.knowledge/knowledge.db; do
  [ -f "$k" ] && KNOWN+=(--known "$k")
done
EXCL=()
[ -f stage2/books-exclusions.json ] && EXCL+=(--exclude stage2/books-exclusions.json)
mkdir -p "$PACK/.knowledge"
$PY tools/build_index.py --no-vec "${UNITS[@]}" --entities build/entities "${KNOWN[@]}" "${EXCL[@]}" --out "$PACK/.knowledge/knowledge.db"
# Like build_split.sh: the pack index keeps only the entities its units point at; the device graph is the core's.
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
  DEST="$ROOT/Local/CPP_Books/$VERSION"
  mkdir -p "$DEST"
  cp "$PACK"/*.pdsc "$PACK"/LICENSE.txt "$DEST"/ && mkdir -p "$DEST/.knowledge" && cp "$PACK/.knowledge/knowledge.db" "$DEST/.knowledge/"
  echo "installed into $DEST"
fi
