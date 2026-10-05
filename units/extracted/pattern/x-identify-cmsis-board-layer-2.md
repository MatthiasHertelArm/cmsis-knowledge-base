---
id: "x-identify-cmsis-board-layer-2"
type: "pattern"
domain: "project"
title: "List packaged layers for one target type with csolution"
status: "draft"
extracted_from: "proc-identify-cmsis-board-layer"
source: "project/identify-cmsis-board-layer/SKILL.md"
---

Record the active CMSIS-Toolbox version with `csolution --version` and inspect `csolution list layers -h`. Require the installed command to support `--active` and `--verbose`; stop if either option is unavailable.

csolution list layers <solution>.csolution.yml --active "<target-type>" --verbose

Do not omit or replace either option and do not replace target selection with context-pattern selection. Do not pass `--version` to `list layers`; it prints the tool version and exits.
