---
id: "ethu-overview-memory-modes"
type: "concept"
domain: "edge-ai"
title: "Overview: Memory modes"
summary: "Ethos-U systems can place model constants, the tensor arena, and temporary data in different memories. Vela uses the selected memory mode and the target's memory-performance configuration to optimize data movement and execution."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:overview/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/overview/README.md#memory-modes"
license: "Apache-2.0"
mode: "V"
---

Ethos-U systems can place model constants, the tensor arena, and temporary data
in different memories. Vela uses the selected memory mode and the target's
memory-performance configuration to optimize data movement and execution.

(figure: Comparison of Ethos-U memory modes)

- **SRAM-only mode** keeps both constants and the tensor arena in SRAM for low
  access latency, but the complete model and arena must fit there.
- **Shared-SRAM mode** keeps the tensor arena in SRAM while read-only constants
  reside in Flash, MRAM, or DRAM, reducing SRAM usage.
- **Dedicated-SRAM mode** places constants and the tensor arena in larger memory
  and uses SRAM as a fast staging area for selected data.

See the [General documentation](https://arm-software.github.io/CMSIS-Ethos-U/main/general/index.html)
for memory-mode concepts and the [Integration documentation](https://arm-software.github.io/CMSIS-Ethos-U/main/integration/index.html)
for linker placement, memory attributes, cache policy, and driver configuration.
