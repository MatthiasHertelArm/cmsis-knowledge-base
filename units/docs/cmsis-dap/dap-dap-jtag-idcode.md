---
id: "dap-dap-jtag-idcode"
type: "concept"
domain: "debug"
title: "DAP_JTAG_IDCODE"
summary: "The DAP_JTAG_IDCODE Command request the JTAG IDCODE for the selected device on the JTAG chain."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_jtag_idcode.html"
license: "Apache-2.0"
mode: "V"
---

Read JTAG IDCODE

The **DAP_JTAG_IDCODE Command** request the JTAG IDCODE for the selected device on the JTAG chain.

**DAP_JTAG_IDCODE Command**:
```
| BYTE | BYTE ******|
> 0x16 | JTAG Index |
|******|************|
```

- **JTAG Index**: Zero based JTAG index of selected device.

**DAP_JTAG_IDCODE Response**:
```
| BYTE | BYTE **| WORD ***|
< 0x16 | Status | ID Code |
|******|********|*********|
```

- **ID Code**: 32-bit JTAG ID Code of the device.
- **Status:** DAP_Response_Status
