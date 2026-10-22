---
id: "ethu-general-system-configuration-and-memory-modes-at"
type: "concept"
domain: "edge-ai"
title: "General: System configuration and memory modes at a glance"
summary: "Ethos-U uses AXI bus interfaces for DMA memory access. The memory access timing for the different data classes has a direct impact on overall performance. Vela optimizes ML model execution based on system and memory parameters in the vela.ini file."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/general/src/main.md#system-configuration-and-memory-modes-at-a-glance"
license: "Apache-2.0"
mode: "V"
---

Ethos-U uses AXI bus interfaces for DMA memory access. The memory access timing
for the different data classes has a direct impact on overall performance.
Vela optimizes ML model execution based on system and memory parameters in the
`vela.ini` file.

Vela uses the logical aliases `Axi0` and `Axi1` to model memory placement and
performance. The selected system configuration maps each alias to a Vela memory
type. These aliases are compiler labels, not necessarily the names or number of
physical AXI ports implemented by the NPU.

Ethos-U65 and Ethos-U85 provide two read/write AXI ports and support all the
memory modes shown below. Ethos-U55 provides one read/write and one read-only
AXI port and supports SRAM-only and Shared-SRAM modes. Dedicated-SRAM mode
places the writable arena in other memory, normally DRAM, while reserving SRAM
for fast staging. Both paths must be writable, so this mode is available on
Ethos-U65 and Ethos-U85. Read-only Flash can hold constants but not the arena.
Shared-SRAM is the typical mode on an Edge AI MCU because it stores the ML model
constants in Flash while using SRAM for the writable arena.

The following diagram compares these memory modes.

(figure: Comparison of Ethos-U memory modes)

|**SRAM-only mode**       | **Shared-SRAM mode**    | **Dedicated-SRAM mode** |
|:------------------------|:------------------------|:------------------------|
| All Vela-managed model storage is placed in SRAM. Constants and the writable arena remain separate logical areas, but both use the same physical memory type. This mode provides low access latency, but the complete compiled model and arena must fit in SRAM. | The writable arena is stored in SRAM. Read-only constants, such as encoded weights and scales, are stored in Flash, MRAM, or DRAM. This arrangement minimizes SRAM usage. | Constants and the writable arena are outside the fast SRAM, normally in DRAM. SRAM is dedicated to fast staging storage. Vela uses spilling to move selected data through this area and reduce external-memory traffic. |

Vela maps to physical memory with the `system-config` and `memory-mode` options.
The related performance parameters are obtained from the device-specific
`vela.ini` file. See Use
the Ethos-U configuration for selecting and inspecting these settings, and
Integration for the corresponding linker sections,
MPU/SAU attributes, cache policy, and driver region configuration.
