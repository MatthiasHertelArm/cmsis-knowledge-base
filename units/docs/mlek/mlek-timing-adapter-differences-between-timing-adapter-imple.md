---
id: "mlek-timing-adapter-differences-between-timing-adapter-imple"
type: "concept"
domain: "edge-ai"
title: "Timing adapter: Differences between timing adapter implementations in Arm Corstone-300 and Arm Corstone-310"
summary: "Corstone-300 FVP and FPGA implements timing adapters that are tied to AXI buses M0 and M1 on the Ethos-U NPU."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/timing_adapters.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/timing_adapters.md#differences-between-timing-adapter-implementations-in-arm-corstone-300-and-arm-c"
license: "Apache-2.0"
mode: "V"
---

Corstone-300 FVP and FPGA implements timing adapters that are tied to AXI buses M0 and M1 on the Ethos-U NPU.

Corstone-310 **FPGA** implements timing adapter blocks differently and those are placed on each of the main
memories present on FPGA: SRAM, QSPI flash, DDR and user memory.
Moreover, this timer adapter placement does not translate well to FVP, so current Corstone-310 FVP implementation does
not support the feature. Additionally - base addresses of timer adapters blocks have changed for Corstone-310.

### Timer Adapters for Corstone-300 FVP and FPGA:

| TA Number | Interface TA is placed on | Base address (non-secure/secure) | Size  |
|-----------|---------------------------|----------------------------------|-------|
| 0         | M0/SRAM0 for Ethos-U NPU  | 0x4810_3000/0x5810_3000          | 0.5KB |
| 1         | M1/EXT0 for Ethos-U NPU   | 0x4810_3200/0x5810_3200          | 0.5KB |

### Timer Adapter for Corstone-310 FPGA:

| TA Number | Interface TA is placed on | Base address (non-secure/secure) | Size |
|-----------|---------------------------|----------------------------------|------|
| 0         | FPGA SRAM                 | 0x4170_0000/0x5170_0000          | 4KB  |
| 1         | QSPI flash device         | 0x4170_1000/0x5170_1000          | 4KB  |
| 2         | DDR                       | 0x4170_1000/0x5170_2000          | 4KB  |
| 3         | User memory               | 0x4170_3000/0x5170_3000          | 4KB  |

This is why the evaluation kit is configured with timing adapters disabled altogether (parameter
`ETHOS_U_NPU_TIMING_ADAPTER_ENABLED` set to `OFF`) for Corstone-310 target platform.

> **NOTE**: Arm® Corstone™-315 reference platforms do not use timing adapters. Therefore, like for
Arm® Corstone™-310, they are force-disabled in the CMake configuration.
