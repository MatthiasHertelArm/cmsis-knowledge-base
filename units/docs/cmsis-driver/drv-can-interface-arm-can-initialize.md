---
id: "drv-can-interface-arm-can-initialize"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_Initialize"
summary: "The function initializes the CAN interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_Initialize (ARM_CAN_SignalUnitEvent_t cb_unit_event, ARM_CAN_SignalObjectEvent_t cb_object_event)
```


The function **initializes** the CAN interface.

The function performs the following operations:
  - Initializes the resources needed for the CAN interface, for example dynamic memory allocation, RTOS object allocation, and possibly hardware pin configuration.
  - Registers the ARM_CAN_SignalUnitEvent callback function.
  - Registers the ARM_CAN_SignalObjectEvent callback function.

The parameter **cb_unit_event** is a pointer to the ARM_CAN_SignalUnitEvent callback function; use a NULL pointer
when no callback signals are required.

The parameter **cb_object_event** is a pointer to the ARM_CAN_SignalObjectEvent callback function; use a NULL pointer
when no callback signals are required.

**Example:**
 - see can_interface_gr

*************************************************************************************************************************
