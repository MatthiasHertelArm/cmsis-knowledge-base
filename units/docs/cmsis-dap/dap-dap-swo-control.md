---
id: "dap-dap-swo-control"
type: "concept"
domain: "debug"
title: "DAP_SWO_Control"
summary: "DAP_SWO_Control (0x1A): --------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Control.html"
license: "Apache-2.0"
mode: "V"
---

Control SWO trace data capture


DAP_SWO_Control (0x1A):
--------------------

Controls the SWO trace data capture.

**DAP_SWO_Control Request:**
```
 | BYTE | BYTE    |
 > 0x1A | Control |
 |******|*********|
```
  - **Control:**
    - 0 - Stop
    - 1 - Start

**DAP_SWO_Control Response:**
```
 | BYTE | BYTE   |
 < 0x1A | Status |
 |******|********|
```

- **Status:** DAP_Response_Status

**Note:** Starting capture automatically flushes any existing trace data in buffers which has not yet been read
