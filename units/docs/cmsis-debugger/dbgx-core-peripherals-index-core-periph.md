---
id: "dbgx-core-peripherals-index-core-periph"
type: "concept"
domain: "debug"
title: "Core Peripherals Index (`core-peripherals-index.yml`)"
summary: "This file lists SCVD files and optional conditions that decide whether each file is loaded for a CPU connection."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:configs/core-peripherals/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/configs/core-peripherals/README.md"
license: "Apache-2.0"
mode: "V"
---

This file lists SCVD files and optional conditions that decide whether each file is loaded for
a CPU connection. The input for the condition is based on the selected core and its available
features as described under `system-resources`>`processors` in the `*.cbuild-run.yml` file.
