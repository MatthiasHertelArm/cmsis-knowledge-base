---
id: "ethu-vela-match-the-driver-configuration"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file / Match the driver configuration"
summary: "Part of: Create device-specific vela.ini file"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/vela/src/main.md#match-the-driver-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Create device-specific vela.ini file_

The driver configuration must select NPU access paths that match the physical
placement established by `vela.ini` and the linker script. For the common
embedded output flow, verify these relationships:

| Generated content | Typical compiler memory area | Driver setting |
|---|---|---|
| Command stream | Placed with compiled model constants | `NPU_QCONFIG` |
| Base region 0: constants and encoded weights | `const_mem_area` | `NPU_REGIONCFG_0` |
| Base region 1: activations and scratch | `arena_mem_area` | `NPU_REGIONCFG_1` |
| Base region 2: optional scratch-fast storage | `cache_mem_area` | `NPU_REGIONCFG_2` |

The numeric values of these driver settings are target-specific. Additional
base regions can be present in specialized output flows, so use the generated
command stream and the device integration information as the authority. Also
configure address translation and cache maintenance when Cortex-M software and
the NPU access the same physical memory through different addresses or cache
policies.

See Integration for system validation, platform
hooks, target-specific driver build configuration, cache maintenance, and
address-remapping guidance.
