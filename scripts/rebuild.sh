#!/usr/bin/env bash
# Full rebuild from live sources: entities, skills (stage 1 + stage 2 results), error catalog, index, tests.
# Usage: scripts/rebuild.sh [work-dir]   (default .work)   Set NO_VEC=1 to skip embeddings.
# Set CDA=<checkout of CMSIS-Developer-Assistant> to regenerate the units of its own skills and the routing units.
set -euo pipefail
cd "$(dirname "$0")/.."
W="${1:-.work}"
python3 scripts/fetch_sources.py "$W"
python3 tools/entities.py "$W/index.pidx" "$W/pdsc" build/entities
rm -rf units/skills units/canonical units/extracted units/troubleshooting
python3 tools/skill2ku.py "$W/cmsis-skills/generic-mcu-skills/skills" units/skills
python3 tools/stage2_merge.py units/skills stage2/out_v2
python3 tools/errcat.py "$W/devtools" units/troubleshooting
# The CMSIS Developer Assistant's own skills and its routing units: set CDA to a checkout of the extension.
CDA_UNITS=()
if [ -n "${CDA:-}" ]; then
  rm -rf units/cda-skills units/cda-routes
  python3 tools/skill2ku.py "$CDA/skills" units/cda-skills --known units/skills
  python3 tools/routes2ku.py "$CDA/scripts/skills.config.json" units/cda-routes units/skills units/cda-skills
fi
[ -d units/cda-skills ] && CDA_UNITS+=(--units units/cda-skills)
[ -d units/cda-routes ] && CDA_UNITS+=(--units units/cda-routes)
python3 tools/build_index.py ${NO_VEC:+--no-vec} \
  --units units/skills --units units/canonical --units units/extracted --units units/troubleshooting \
  "${CDA_UNITS[@]}" --entities build/entities --out build/knowledge.db
python3 tests/test_kb.py
