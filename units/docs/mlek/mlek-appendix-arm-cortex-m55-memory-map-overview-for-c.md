---
id: "mlek-appendix-arm-cortex-m55-memory-map-overview-for-c"
type: "concept"
domain: "edge-ai"
title: "Appendix: Arm® Cortex®-M55 Memory map overview for Corstone™-300 reference design"
summary: "The following table refers to the memory mapping information specific to the Arm® Cortex®-M55."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/appendix.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/appendix.md#arm-cortex-m55-memory-map-overview-for-corstone-300-reference-design"
license: "Apache-2.0"
mode: "V"
---

The following table refers to the memory mapping information specific to the Arm® Cortex®-M55.

| Name  | Base address | Limit address |  Size     | IDAU |  Remarks                                                  |
|-------|--------------|---------------|-----------|------|-----------------------------------------------------------|
| ITCM  | 0x0000_0000  |  0x0007_FFFF  |  512 kiB  |  NS  |   ITCM code region                                        |
| BRAM  | 0x0100_0000  |  0x0110_0000  |   1 MiB   |  NS  |   FPGA data SRAM region                                   |
| DTCM  | 0x2000_0000  |  0x2007_FFFF  |  512 kiB  |  NS  |   4 banks for 128 kiB each                                |
| SRAM  | 0x2100_0000  |  0x2120_0000  |   2 MiB   |  NS  |   2 banks of 1 MiB each as SSE-300 internal SRAM region   |
| DDR   | 0x6000_0000  |  0x6FFF_FFFF  |   256 MiB |  NS  |   DDR memory region                                       |
| ITCM  | 0x1000_0000  |  0x1007_FFFF  |   512 kiB |  S   |   ITCM code region                                        |
| BRAM  | 0x1100_0000  |  0x1110_0000  |   1 MiB   |  S   |   FPGA data SRAM region                                   |
| DTCM  | 0x3000_0000  |  0x3007_FFFF  |   512 kiB |  S   |   4 banks for 128 kiB each                                |
| SRAM  | 0x3100_0000  |  0x3120_0000  |   2 MiB   |  S   |   2 banks of 1 MiB each as SSE-300 internal SRAM region   |
| DDR   | 0x7000_0000  |  0x7FFF_FFFF  |  256 MiB  |  S   |   DDR memory region                                       |

The default Cortex®-M55 memory map can be found here: <https://developer.arm.com/documentation/101051/0002/Memory-model/Memory-map>.

The Corstone™-300 memory map can be found here: <https://developer.arm.com/documentation/100966/1126/Arm--Corstone-SSE-300-FVP/Memory-map-overview-for-Corstone-SSE-300>.
