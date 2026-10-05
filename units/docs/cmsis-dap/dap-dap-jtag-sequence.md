---
id: "dap-dap-jtag-sequence"
type: "concept"
domain: "debug"
title: "DAP_JTAG_Sequence"
summary: "Generate JTAG sequence TMS, TDI and capture TDO"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_JTAG_Sequence.html"
license: "Apache-2.0"
mode: "V"
---

Generate JTAG sequence TMS, TDI and capture TDO

The **DAP_JTAG_Sequence Command** may be used to auto-detect devices on the JTAG chain.
The result of this command can be used to calculate on the host computer the number of JTAG
devices and the JTAG IR register length. This information is the input for DAP_JTAG_Configure.

**DAP_JTAG_Sequence Command**:
```
| BYTE | BYTE **********| BYTE *********| BYTE ****|
> 0x14 | Sequence Count | Sequence Info | TDI Data |
|******|****************|///////////////|//////////|
```

- **Sequence Count**: Number of Sequences
- **Sequence Info**: Contains number of TDI bits and fixed TMS value
  - Bit 5 .. 0: Number of TCK cycles: 1 .. 64 (64 encoded as 0)
  - Bit 6: TMS value
  - Bit 7: TDO Capture
- **TDI Data**:  Data generated on TDI
  - One bit for each TCK cycle
  - LSB transmitted first, padded to BYTE boundary

**DAP_JTAG_Sequence Response**:
```
| BYTE | BYTE **| BYTE ****|
< 0x14 | Status | TDO Data |
|******|********|++++++++++|
```

- **TDO Data**:  Data captured from TDO
  - One bit for each TCK cycle when TDO Capture is enabled
  - LSB received first, padded to BYTE boundary
- **Status:** DAP_Response_Status
