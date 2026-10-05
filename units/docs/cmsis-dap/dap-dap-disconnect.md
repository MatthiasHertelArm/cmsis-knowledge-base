---
id: "dap-dap-disconnect"
type: "concept"
domain: "debug"
title: "DAP_Disconnect"
summary: "The DAP_Disconnect Command de-initializes the DAP I/O pins by calling the function PORT_OFF."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Disconnect.html"
license: "Apache-2.0"
mode: "V"
---

Disconnect from active Debug Port

The **DAP_Disconnect Command** de-initializes the DAP I/O pins by calling the function PORT_OFF.

**DAP_Disconnect Command**:
```
| BYTE |
> 0x03 |
|******|
```

**DAP_Disconnect Response**:
```
| BYTE | BYTE   |
< 0x03 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
