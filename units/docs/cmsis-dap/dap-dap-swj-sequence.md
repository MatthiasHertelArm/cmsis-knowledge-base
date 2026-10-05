---
id: "dap-dap-swj-sequence"
type: "concept"
domain: "debug"
title: "DAP_SWJ_Sequence"
summary: "Generate SWJ sequence SWDIO/TMS \\@SWCLK/TCK"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWJ_Sequence.html"
license: "Apache-2.0"
mode: "V"
---

Generate SWJ sequence SWDIO/TMS \@SWCLK/TCK


The **DAP_SWJ_Sequence Command** can be used to generate required SWJ sequences for
SWD/JTAG Reset, SWD<->JTAG switch and Dormant operation.

**DAP_SWJ_Sequence Command**
```
| BYTE | BYTE **************| BYTE *************|
> 0x12 | Sequence Bit Count | Sequence Bit Data |
|******|********************|+++++++++++++++++++|
```

- **Sequence Bit Count**: Number of bits in sequence: 1..256 (256 encoded as 0)
- **Sequence Bit Data**:  Sequence generated on SWDIO/TMS (with clock \@SWCLK/TCK) LSB is transmitted  first


**DAP_SWJ_Sequence Response**:
```
| BYTE | BYTE **|
< 0x12 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
