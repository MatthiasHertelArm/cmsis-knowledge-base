---
id: "ethu-configure-ethos-u-for-fvp-simulati-ethos-u65"
type: "concept"
domain: "edge-ai"
title: "Configure Ethos-U for FVP Simulation Models: Ethos-U65"
summary: "Configure Ethos-U for FVP Simulation Models: Ethos-U65"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/integration/src/fvp-ethos-setup.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/integration/src/fvp-ethos-setup.md#ethos-u65"
license: "Apache-2.0"
mode: "V"
---

| Setting            | SRAM only                     | Shared SRAM                   | Dedicated SRAM                |
|--------------------|-------------------------------|-------------------------------|-------------------------------|
| Target type        | `SSE-300-U65`                 | `SSE-300-U65`                 | `SSE-300-U65`                 |
| Solution           | `Test-Ethos-U65`              | `Test-Ethos-U65`              | `Test-Ethos-U65`              |
| NPU                | U65, 256 MACs                 | U65, 256 MACs                 | U65, 256 MACs                 |
| Vela INI           | `Model/vela.ini`              | `Model/vela.ini`              | `Model/vela.ini`              |
| Vela `system`      | `Ethos_U65_Embedded`          | `Ethos_U65_Embedded`          | `Ethos_U65_Mid_End`           |
| Vela `memory`      | `Sram_Only`                   | `Shared_Sram`                 | `Dedicated_Sram_384KB`        |
| `NPU_QCONFIG`      | `1`                           | `2` (default)                 | `2`                           |
| `NPU_REGIONCFG_0`  | `1`                           | `3` (default)                 | `3`                           |
| `NPU_REGIONCFG_1`  | `0`                           | `0` (default)                 | `2`                           |
| `NPU_REGIONCFG_2`  | Unused                        | Unused                        | `1`                           |
| `ETHOS_CACHE_SIZE` | Not used                      | Not used                      | `393216` bytes                |
| `ethos_model`      | SRAM_VM0 / RAM1 via `AXI0`    | DDR4_3 / ROM2 via `AXI1`      | DDR4_3 / ROM2 via `AXI1`      |
| `ethos_arena`      | SRAM_VM0 / RAM1 via `AXI0`    | SRAM_VM0 / RAM1 via `AXI0`    | DDR4_1 / RAM0 via `AXI1`      |
| `ethos_cache`      | Unused                        | Unused                        | SRAM_VM0 / RAM1 via `AXI0`    |
