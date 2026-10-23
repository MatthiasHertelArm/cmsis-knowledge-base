---
id: "drv-can-interface-arm-can-status"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_STATUS"
summary: "Structure with information about the status of the CAN unit state and errors. The data fields encode the unit bus state, last error code, transmitter error count, and receiver error count."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_STATUS
```


Structure with information about the status of the CAN unit state and errors.
The data fields encode the unit bus state, last error code, transmitter error count, and receiver error count.

**Returned by:**
  - ARM_CAN_GetStatus
****************************************************************************************************************
