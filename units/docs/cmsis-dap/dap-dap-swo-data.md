---
id: "dap-dap-swo-data"
type: "concept"
domain: "debug"
title: "DAP_SWO_Data"
summary: "DAP_SWO_Data (0x1C): --------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Data.html"
license: "Apache-2.0"
mode: "V"
---

Read SWO trace data


DAP_SWO_Data (0x1C):
--------------------

Reads the captured SWO trace data from Trace Buffer.

**DAP_SWO_Data Request:**
```
 | BYTE | SHORT       |
 > 0x1C | Trace Count |
 |******|*************|
```
  - **Trace Count**: Maxim number of Trace Data bytes to read

**DAP_SWO_Data Response:**
```
 | BYTE | BYTE         | SHORT       | BYTE       |
 < 0x1C | Trace Status | Trace Count | Trace Data |
 |******|**************|*************|////////////|
```

  - **Trace Status**:
    - Bit 0: Trace Capture (1 - active, 0 - inactive)
    - Bit 6: Trace Stream Error
    - Bit 7: Trace Buffer Overrun
  - **Trace Count**: Number of Trace Data bytes read
  - **Trace Data**:  Trace Data bytes read
