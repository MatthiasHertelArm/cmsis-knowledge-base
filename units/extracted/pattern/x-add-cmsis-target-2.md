---
id: "x-add-cmsis-target-2"
type: "pattern"
domain: "project"
title: "Bind a copied packaged board layer in target variables"
status: "draft"
extracted_from: "proc-add-cmsis-target"
source: "project/add-cmsis-target/SKILL.md"
---

In the new target's `variables:`, bind the same board-layer variable consumed by the project to the copied layer file. Use a portable `$SolutionDir()$` path and document the exact source directory with `copied-from:`.

variables:
  - Board-Layer: $SolutionDir()$/Board/<board-name>/<layer-file>.clayer.yml
    copied-from: ${CMSIS_PACK_ROOT}/<vendor>/<pack>/<version>/<reported-path>/

Preserve the actual variable key, filename, pack path, and version reported for the selected candidate. Never refer the active layer variable directly to `${CMSIS_PACK_ROOT}`.
