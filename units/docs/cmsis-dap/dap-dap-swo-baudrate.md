---
id: "dap-dap-swo-baudrate"
type: "concept"
domain: "debug"
title: "DAP_SWO_Baudrate"
summary: "DAP_SWO_Baudrate (0x19): ------------------------"
status: "draft"
collection: "cmsis-dap"
source: "ARM-software/CMSIS-DAP@1263659:Documentation/Doxygen/src/ref_dap.txt"
doc_source: "https://arm-software.github.io/CMSIS-DAP/latest/DAP_SWO_Baudrate.html"
license: "Apache-2.0"
mode: "V"
---

Set SWO baudrate


DAP_SWO_Baudrate (0x19):
------------------------

Sets the baudrate for capturing SWO trace data. Can be called iteratively to determine supported baudrates.

**DAP_SWO_Baudrate Request:**
```
 | BYTE | WORD     |
 > 0x19 | Baudrate |
 |******|**********|
```
  - **Baudrate:** Requested baudrate

**DAP_SWO_Baudrate Response:**
```
 | BYTE | WORD     |
 < 0x19 | Baudrate |
 |******|**********|
```

  - **Baudrate:** Actual baudrate or 0 (baudrate not configured).
    When requested baudrate is not achievable the closest configured baudrate can be returned or 0
    which indicates that baudrate was not configured.

**Note:**   When Manchester Mode is used and if decoder is implemented with clock recovery then baudrate
        is not required since clock is automatically decoded. However such decoders are harder to implement
        (especially for high frequencies) and the clock recovery might not be implemented.
        Therefore the baudrate should be provided also for Manchester mode.
