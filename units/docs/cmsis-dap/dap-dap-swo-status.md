---
id: "dap-dap-swo-status"
type: "concept"
domain: "debug"
title: "DAP_SWO_Status"
summary: "DAP_SWO_Status (0x1B): --------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Status.html"
license: "Apache-2.0"
mode: "V"
---

Read SWO trace status


DAP_SWO_Status (0x1B):
--------------------

Reads the SWO trace status.

**DAP_SWO_Status Request:**
```
 | BYTE |
 > 0x1B |
 |******|
```

**DAP_SWO_Status Response:**
```
 | BYTE | BYTE         | WORD        |
 < 0x1B | Trace Status | Trace Count |
 |******|**************|*************|
```

  - **Trace Status**:
    - Bit 0: Trace Capture (1 - active, 0 - inactive)
    - Bit 6: Trace Stream Error
    - Bit 7: Trace Buffer Overrun
  - **Trace Count**: Number of bytes in Trace Buffer (not yet read)
