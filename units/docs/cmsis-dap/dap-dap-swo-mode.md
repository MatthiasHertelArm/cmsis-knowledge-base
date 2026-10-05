---
id: "dap-dap-swo-mode"
type: "concept"
domain: "debug"
title: "DAP_SWO_Mode"
summary: "DAP_SWO_Mode (0x18): --------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Mode.html"
license: "Apache-2.0"
mode: "V"
---

Set SWO capture mode


DAP_SWO_Mode (0x18):
--------------------

Sets the SWO trace capture mode.

**DAP_SWO_Mode Request:**
```
 | BYTE | BYTE |
 > 0x18 | Mode |
 |******|******|
```

- **Mode:**
  - 0 - Off (default)
  - 1 - UART
  - 2 - Manchester

**DAP_SWO_Mode Response:**
```
 | BYTE | BYTE   |
 < 0x18 | Status |
 |******|********|
```

- **Status:** DAP_Response_Status
