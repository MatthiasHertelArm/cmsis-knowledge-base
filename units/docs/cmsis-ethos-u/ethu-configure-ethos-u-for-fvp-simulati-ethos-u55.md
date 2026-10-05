---
id: "ethu-configure-ethos-u-for-fvp-simulati-ethos-u55"
type: "concept"
domain: "edge-ai"
title: "Configure Ethos-U for FVP Simulation Models: Ethos-U55"
summary: "Configure Ethos-U for FVP Simulation Models: Ethos-U55"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/fvp-ethos-setup.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/fvp-ethos-setup.md#ethos-u55"
license: "Apache-2.0"
mode: "V"
---

| Setting            | SRAM only                     | Shared SRAM                   |
|--------------------|-------------------------------|-------------------------------|
| Target type        | `SSE-300-U55`                 | `SSE-300-U55`                 |
| Solution           | `Test-Ethos-U55`              | `Test-Ethos-U55`              |
| NPU                | U55, 128 MACs                 | U55, 128 MACs                 |
| Vela INI           | `Model/vela.ini`              | `Model/vela.ini`              |
| Vela `system`      | `Ethos_U55_High_End_Embedded` | `Ethos_U55_High_End_Embedded` |
| Vela `memory`      | `Sram_Only`                   | `Shared_Sram`                 |
| `NPU_QCONFIG`      | `1`                           | `2` (default)                 |
| `NPU_REGIONCFG_0`  | `1`                           | `3` (default)                 |
| `NPU_REGIONCFG_1`  | `0`                           | `0` (default)                 |
| `NPU_REGIONCFG_2`  | Unused                        | Unused                        |
| `ETHOS_CACHE_SIZE` | Not used                      | Not used                      |
| `ethos_model`      | SRAM_VM0 / RAM1 via `AXI0`    | DDR4_3 / ROM2 via `AXI1`      |
| `ethos_arena`      | SRAM_VM0 / RAM1 via `AXI0`    | SRAM_VM0 / RAM1 via `AXI0`    |
| `ethos_cache`      | Unused                        | Unused                        |
