---
id: "mlek-appendix-arm-cortex-m85-memory-map-overview-for-c"
type: "concept"
domain: "edge-ai"
title: "Appendix: Arm® Cortex®-M85 Memory map overview for Corstone™-315 reference design"
summary: "The following table refers to the memory mapping information specific to the Arm® Cortex®-M85."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/appendix.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/appendix.md#arm-cortex-m85-memory-map-overview-for-corstone-315-reference-design"
license: "Apache-2.0"
mode: "V"
---

The following table refers to the memory mapping information specific to the Arm® Cortex®-M85.

| Name | Base address | Limit address | Size    | IDAU | Remarks                                               |
|------|--------------|---------------|---------|------|-------------------------------------------------------|
| ITCM | 0x0000_0000  |  0x0000_7FFF  | 32 kiB  | NS   | ITCM code region                                      |
| BRAM | 0x0100_0000  |  0x0120_0000  | 2 MiB   | NS   | FPGA data SRAM region                                 |
| DTCM | 0x2000_0000  |  0x2000_7FFF  | 32 kiB  | NS   | 4 banks for 8 kiB each                                |
| SRAM | 0x2100_0000  |  0x213F_FFFF  | 4 MiB   | NS   | 2 banks of 2 MiB each as SSE-315 internal SRAM region |
| DDR  | 0x6000_0000  |  0x6FFF_FFFF  | 256 MiB | NS   | DDR memory region                                     |
| ITCM | 0x0A00_0000  |  0x0A00_7FFF  | 32 kiB  | S    | DMA ITCM CPU0 S-AHB Instruction TCM Access            |
| ITCM | 0x1000_0000  |  0x1000_7FFF  | 32 kiB  | S    | ITCM code region                                      |
| BOOT | 0x1100_0000  |  0x1101_FFFF  | 128 KiB | S    | Boot ROM                                              |
| BRAM | 0x1200_0000  |  0x121F_FFFF  | 2 MiB   | S    | FPGA data SRAM region                                 |
| ITCM | 0x1A00_0000  |  0x1A00_7FFF  | 32 kiB  | S    | DMA ITCM                                              |
| DTCM | 0x3000_0000  |  0x3000_7FFF  | 32 kiB  | S    | 4 banks for 8 kiB each                                |
| SRAM | 0x3100_0000  |  0x313F_FFFF  | 4 MiB   | S    | 2 banks of 2 MiB each as SSE-310 internal SRAM region |
| DDR  | 0x7000_0000  |  0x7FFF_FFFF  | 256 MiB | S    | DDR memory region                                     |

The Corstone™-315 memory map can be found here: <https://developer.arm.com/documentation/109395/0000/SSE-315-FVP/SSE-315-FVP-memory-map>.
