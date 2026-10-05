---
id: "dap-dap-swd-sequence"
type: "concept"
domain: "debug"
title: "DAP_SWD_Sequence"
summary: "Generate SWD sequence and output on SWDIO or capture input from SWDIO data."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWD_Sequence.html"
license: "Apache-2.0"
mode: "V"
---

Generate SWD sequence and output on SWDIO or capture input from SWDIO data.

**Note:**
The DAP_SWD_Sequence is available for CMSIS-DAP version 1.2 and higher.  Refer to DAP_Info for more information on how to query the CMSIS-DAP version.


The **DAP_SWD_Sequence Command** is used to generate special sequences in SWD mode on the pins SWCLK and SWDIO.
For example, for SWD multi-drop target selection (see picture) it is required to put the SWDIO pin to input mode (where it is not driven).

" "SWD sequence for multi-drop target selection"

 - For mode=0 (output: SWDIO is driven), the data for the SWDIO pin are part of the **DAP_SWD_Sequence Command**.
 - For mode=1 (input: SWDIO is not driven), the data from the SWDIO pin are captured and returned as part of the **DAP_SWD_Sequence Response**.

**DAP_SWD_Sequence Command**:
```
| BYTE | BYTE **********| BYTE *********| BYTE ******|
> 0x1D | Sequence Count | Sequence Info | SWDIO Data |
|******|****************|///////////////|++++++++++++|
```

- **Sequence Count**: Number of Sequences
- **Sequence Info**: Contains number of SWCLK cycles and SWDIO mode
  - Bit 5 .. 0: Number of TCK cycles: 1 .. 64 (64 encoded as 0)
  - Bit 6: reserved
  - Bit 7: mode: 0=output (SWDIO Data in command), 1=input (SWDIO Data in response)
- **SWDIO Data** (only for output mode):  Data generated on SWDIO
  - One bit for each TCK cycle
  - LSB transmitted first, padded to BYTE boundary

**DAP_SWD_Sequence Response**:
```
| BYTE | BYTE **| BYTE ******|
< 0x1D | Status | SWDIO Data |
|******|********|++++++++++++|
```

- **SWDIO Data** (only for input mode):  Data captured from SWDIO
  - One bit for each SWCLK cycle for input mode
  - LSB received first, padded to BYTE boundary
- **Status:** DAP_Response_Status
