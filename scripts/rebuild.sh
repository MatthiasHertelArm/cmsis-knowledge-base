#!/usr/bin/env bash
# Full rebuild from live sources: entities, skills (stage 1 + stage 2 results), error catalog, index, tests.
# Usage: scripts/rebuild.sh [work-dir]   (default .work)   Set NO_VEC=1 to skip embeddings.
# Set CCBYSA=1 to include the CC BY-SA documentation (units/docs-ccbysa), which is open for legal review.
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
# Cause and fix of the messages, read from the devtools source (stage2/errcat-out), then the review list.
python3 tools/errcat_merge.py units/troubleshooting stage2/errcat-out
python3 tools/review_csv.py units/troubleshooting messages-to-review.csv
# Documentation of open-licence repositories, one unit per section (sources/docs.yml).
python3 tools/doc2ku.py sources/docs.yml "$W/docs" units/docs --fetch
# One unit per debug adapter of the CMSIS debug adapter registry (cloned by doc2ku as a docs source).
python3 tools/adapters2ku.py "$W/docs/debug-adapter-registry" units/docs/debug-adapters
DOC_UNITS=(--units units/docs)
# Closed GitHub issues of the tools, digested in own words (stage2/issues_prompt.md, mode S).
python3 tools/issues2ku.py stage2/issues-out units/issues "$W/issues/batches"
DOC_UNITS+=(--units units/issues)
if [ -n "${CCBYSA:-}" ]; then
  python3 tools/doc2ku.py sources/docs-ccbysa.yml "$W/docs" units/docs-ccbysa --fetch
  DOC_UNITS+=(--units units/docs-ccbysa)
fi
# The CMSIS Developer Assistant's own skills and its routing units: set CDA to a checkout of the extension.
CDA_UNITS=()
if [ -n "${CDA:-}" ]; then
  rm -rf units/cda-skills units/cda-routes
  python3 tools/skill2ku.py "$CDA/skills" units/cda-skills --known units/skills
fi
# Stage 2 of the extension's skills; also without CDA, since units/extracted was cleared above.
if [ -d units/cda-skills ]; then
  python3 tools/stage2_merge.py units/cda-skills stage2/out_cda
fi
if [ -n "${CDA:-}" ]; then
  python3 tools/routes2ku.py "$CDA/scripts/skills.config.json" units/cda-routes units/skills units/cda-skills
fi
[ -d units/cda-skills ] && CDA_UNITS+=(--units units/cda-skills)
[ -d units/cda-routes ] && CDA_UNITS+=(--units units/cda-routes)
python3 tools/build_index.py ${NO_VEC:+--no-vec} \
  --units units/skills --units units/canonical --units units/extracted --units units/troubleshooting \
  "${CDA_UNITS[@]}" "${DOC_UNITS[@]}" --entities build/entities --out build/knowledge.db
python3 tests/test_kb.py
