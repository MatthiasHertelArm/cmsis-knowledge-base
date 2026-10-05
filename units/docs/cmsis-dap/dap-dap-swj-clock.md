---
id: "dap-dap-swj-clock"
type: "concept"
domain: "debug"
title: "DAP_SWJ_Clock"
summary: "The DAP_SWJ_Clock Command sets the clock frequency for JTAG and SWD communication mode."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWJ_Clock.html"
license: "Apache-2.0"
mode: "V"
---

Select SWD/JTAG Clock

The **DAP_SWJ_Clock Command** sets the clock frequency for JTAG and SWD communication mode.

**DAP_SWJ_Clock Command**:
```
| BYTE | WORD *|
> 0x11 | Clock |
|******|*******|
```

- **Clock:** Selects maximum SWD/JTAG Clock (SWCLK/TCK) value in Hz

**DAP_SWJ_Clock Response**:
```
| BYTE | BYTE **|
< 0x11 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
