---
id: "dap-dap-resettarget"
type: "concept"
domain: "debug"
title: "DAP_ResetTarget"
summary: "Reset Target with Device specific sequence."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_ResetTarget.html"
license: "Apache-2.0"
mode: "V"
---

Reset Target with Device specific sequence.

The **DAP_ResetTarget Command** requests a target reset with a device specific command sequence.
This command calls the user configurable function RESET_TARGET.

**DAP_ResetTarget Command**:
```
| BYTE |
> 0x0A |
|******|
```

**DAP_ResetTarget Response**:
```
| BYTE | BYTE   | BYTE    |
< 0x0A | Status | Execute |
|******|********|*********|
```

- **Execute:** indicates whether a device specific reset sequence was executed.
  - no device specific reset sequence is implemented.
  - 1 = a device specific reset sequence is implemented.
- **Status:** DAP_Response_Status
