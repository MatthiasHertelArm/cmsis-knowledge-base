---
id: "drv-can-interface-arm-can-powercontrol"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_PowerControl"
summary: "The function ARM_CAN_PowerControl controls the power modes of the CAN interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_CAN_PowerControl** controls the power modes of the CAN interface.

The parameter **state** can be:
    - ARM_POWER_FULL: Activate clocks and driver functionality as if peripheral was reset.
    - ARM_POWER_OFF:  Unconditionally put peripheral into non-functional (reset) state.
    - ARM_POWER_LOW:  Put peripheral into low power consumption state ready to wake up on bus event.

*************************************************************************************************************************
