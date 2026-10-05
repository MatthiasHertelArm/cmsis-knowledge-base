---
id: "x-add-board-layer-5"
type: "concept"
domain: "project"
title: "CMSIS pack root and automatic pack download"
status: "draft"
extracted_from: "proc-add-board-layer"
source: "add-board-layer/SKILL.md"
---

Pack root: `$CMSIS_PACK_ROOT` (default `~/.cache/arm/packs` on Linux and macOS, `%LOCALAPPDATA%\Arm\Packs` on Windows). Missing packs need no command from you: the CMSIS Solution extension downloads them when it loads the solution and when `cmsis_action build` runs (its setting `cmsis-csolution.downloadPacks`, on by default). `cpackget add Vendor::Pack` or `cbuild --packs` only when the user works from a terminal.
