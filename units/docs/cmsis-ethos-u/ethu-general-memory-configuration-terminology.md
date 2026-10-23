---
id: "ethu-general-memory-configuration-terminology"
type: "concept"
domain: "edge-ai"
title: "General: Memory configuration terminology"
summary: "Memory configuration spans several description layers. Similar names at different layers do not refer to the same object:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/general/src/main.md#memory-configuration-terminology"
license: "Apache-2.0"
mode: "V"
---

Memory configuration spans several description layers. Similar names at
different layers do not refer to the same object:

| Layer | Examples | Meaning |
| --- | --- | --- |
| Physical memory | SRAM, Flash or MRAM, DRAM | Storage implemented by the device and connected through its interconnect. |
| Vela memory type | `Sram`, `OnChipFlash`, `OffChipFlash`, `Dram` | Performance-model category used by a Vela system configuration. |
| Vela logical alias | `Axi0`, `Axi1` | Logical memory domain used by a Vela memory mode. An alias does not necessarily represent one physical AXI port. |
| Vela data role | `const_mem_area`, `arena_mem_area`, `cache_mem_area` | Kind of generated model data assigned to a logical memory domain. |
| Runtime allocation | Compiled model, tensor arena, optional fast-scratch buffer | Actual linked or dynamically allocated storage used for inference. |
| Driver memory access configuration | `NPU_QCONFIG`, `NPU_REGIONCFG_0..7` | NPU access route and attributes used for the command stream and base-pointer regions. |

The selected memory mode maps Vela data roles to logical aliases. The system
configuration maps those aliases to Vela memory types. The linker and runtime
then place the corresponding allocations in physical memory, and the driver
must select matching NPU access routes. See
Vela memory mode parameters
for the exact configuration keys and
Configure memory placement and the linker script
for the end-to-end mapping.
