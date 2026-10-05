---
id: "dap-dap-swo-extendedstatus"
type: "concept"
domain: "debug"
title: "DAP_SWO_ExtendedStatus"
summary: "DAP_SWO_ExtendedStatus (0x1E): -----------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_ExtendedStatus.html"
license: "Apache-2.0"
mode: "V"
---

Read SWO trace extended status


DAP_SWO_ExtendedStatus (0x1E):
-----------------------------

Reads extended information about the SWO trace status.

**DAP_SWO_ExtendedStatus Request:**
```
 | BYTE | BYTE    |
 > 0x1E | Control |
 |******|*********|
```

  - **Control**:
    - Bit 0: Trace Status (1 - request, 0 - inactive)
    - Bit 1: Trace Count (1 - request, 0 - inactive)
    - Bit 2: Index/Timestamp (1 - request, 0 - inactive)

**DAP_SWO_ExtendStatus Response:**
```
 | BYTE | BYTE         | WORD        | WORD  | WORD         |
 < 0x1E | Trace Status | Trace Count | Index | TD_TimeStamp |
 |******|++++++++++++++|+++++++++++++|+++++++|++++++++++++++|
```

  - **Trace Status**:
    - Bit 0: Trace Capture (1 - active, 0 - inactive)
    - Bit 6: Trace Stream Error
    - Bit 7: Trace Buffer Overrun

  - **Trace Count**: Number of bytes in Trace Buffer (not yet read)

  - **Index**: Sequence number of next trace information
  - **TD_TimeStamp**: Test Domain Timer value for trace sequence.
