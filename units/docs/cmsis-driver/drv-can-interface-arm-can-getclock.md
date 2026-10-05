---
id: "drv-can-interface-arm-can-getclock"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_GetClock"
summary: "The function ARM_CAN_GetClock returns the CAN base clock frequency in [Hz]. This value may be used to validate the bitrate for the function ARM_CAN_SetBitrate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
uint32_t ARM_CAN_GetClock (void)
```


The function **ARM_CAN_GetClock** returns the CAN base clock frequency in `[Hz]`.
This value may be used to validate the **bitrate** for the function ARM_CAN_SetBitrate.

**Example**:
```
  CAN_clock = ARM_CAN_GetClock();  // CAN base clock frequency
```

*************************************************************************************************************************
