---
id: "drv-can-interface-arm-can-signalunitevent"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_SignalUnitEvent"
summary: "The function ARM_CAN_SignalUnitEvent is a callback function registered by the function ARM_CAN_Initialize."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
void ARM_CAN_SignalUnitEvent (uint32_t event)
```


The function **ARM_CAN_SignalUnitEvent** is a callback function registered by the function ARM_CAN_Initialize. 

The parameter **event** indicates unit event that occurred during driver operation.

The following callback notifications are generated:

Parameter **event**                | Value |Description
:----------------------------------|:-----:|:-------------------------------------------------
ARM_CAN_EVENT_UNIT_INACTIVE   |   0   | Unit entered Inactive state.
ARM_CAN_EVENT_UNIT_ACTIVE     |   1   | Unit entered Error Active state.
ARM_CAN_EVENT_UNIT_WARNING    |   2   | Unit entered Error Warning state (one or both error counters >= `96`).
ARM_CAN_EVENT_UNIT_PASSIVE    |   3   | Unit entered Error Passive state.
ARM_CAN_EVENT_UNIT_BUS_OFF    |   4   | Unit entered Bus-off state.

\sa ARM_CAN_GetStatus
******************************************************************************************************************
