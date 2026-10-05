---
id: "dap-dap-swo-transport"
type: "concept"
domain: "debug"
title: "DAP_SWO_Transport"
summary: "DAP_SWO_Transport (0x17): -------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Transport.html"
license: "Apache-2.0"
mode: "V"
---

Set SWO transport mode


DAP_SWO_Transport (0x17):
-------------------------

Sets the SWO transport mode for reading trace data.

**DAP_SWO_Transport Request:**
```
 | BYTE | BYTE      |
 > 0x17 | Transport |
 |******|***********|
```

  - **Transport:**
    - 0 - None (default)
    - 1 - Read trace data via DAP_SWO_Data command
    - 2 - Send trace data via separate USB bulk endpoint (requires CMSIS-DAP v2 configuration)
    - ... - reserved

**DAP_SWO_Transport Response:**
```
 | BYTE | BYTE   |
 < 0x17 | Status |
 |******|********|
```

- **Status:** DAP_Response_Status

**Note:** Currently the trace data can only be read via the existing DAP command request/response channel by using DAP_SWO_Data.
        Future extension might provide separate channels for reading trace data.
