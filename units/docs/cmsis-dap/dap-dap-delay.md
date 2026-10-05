---
id: "dap-dap-delay"
type: "concept"
domain: "debug"
title: "DAP_Delay"
summary: "The DAP_Delay< Command waits for a time period specified in micro-seconds."
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_Delay.html"
license: "Apache-2.0"
mode: "V"
---

Wait for specified delay

The **DAP_Delay< Command** waits for a time period specified in micro-seconds.

**DAP_Delay Command**:
```
| BYTE | SHORT |
> 0x09 | Delay |
|******|*******|
```

- **Delay:** wait time in µs.

**DAP_Delay Response**:
```
| BYTE | BYTE   |
< 0x09 | Status |
|******|********|
```

- **Status:** DAP_Response_Status
