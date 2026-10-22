---
id: "drv-can-interface-arm-can-setmode"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_SetMode"
summary: "The function ARM_CAN_SetMode sets the CAN bus communication mode using the parameter mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_SetMode (ARM_CAN_MODE mode)
```


The function **ARM_CAN_SetMode** sets the CAN bus communication mode using the parameter **mode.**

The table lists the values for **mode.**



| Parameter **mode | Bus Communication Mode | supported when ARM_CAN_OBJ_CAPABILITIES data field |
|---|---|---|
| ARM_CAN_MODE_INITIALIZATION | Initialization mode; Used to setup communication parameters for the reception objects and global filtering, while peripheral is not active on the bus. Refer to can_filtering for details. | always supported |
| ARM_CAN_MODE_NORMAL | Normal operation mode. Used when peripheral is in active mode to receive, transmit, and acknowledge messages on the bus. Depending on the current unit state, it can generate error or overload messages. Verify the unit state with ARM_CAN_GetStatus.  always supported |  |
| ARM_CAN_MODE_RESTRICTED | Restricted operation mode. Used for monitoring the bus communication non-intrusively without transmitting. | **restricted_mode** = `1` |
| ARM_CAN_MODE_MONITOR | Bus monitoring mode. | **monitor_mode** = `1` |
| ARM_CAN_MODE_LOOPBACK_INTERNAL | Test mode; loopback of CAN transmission to its receiver. No transmission visible on CAN bus. | **internal_loopback** = `1` |
| ARM_CAN_MODE_LOOPBACK_EXTERNAL | Test mode; loopback of CAN transmission to its receiver. Transmission is visible on CAN bus. | **external_loopback** = `1` |


*************************************************************************************************************************
