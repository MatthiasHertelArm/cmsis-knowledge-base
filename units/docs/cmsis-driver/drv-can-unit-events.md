---
id: "drv-can-unit-events"
type: "concept"
domain: "drivers"
title: "CAN Unit Events"
summary: "Callback unit events notified via ARMCANSignalUnitEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

Callback unit events notified via ARM_CAN_SignalUnitEvent.

The CAN driver generates callback unit events that are notified via the function ARM_CAN_SignalUnitEvent.

The following callback notification unit events are generated:

### ARM_CAN_EVENT_UNIT_INACTIVE

```c
ARM_CAN_EVENT_UNIT_INACTIVE
```

\sa ARM_CAN_SignalUnitEvent

### ARM_CAN_EVENT_UNIT_ACTIVE

```c
ARM_CAN_EVENT_UNIT_ACTIVE
```

\sa ARM_CAN_SignalUnitEvent

### ARM_CAN_EVENT_UNIT_WARNING

```c
ARM_CAN_EVENT_UNIT_WARNING
```

\sa ARM_CAN_SignalUnitEvent

### ARM_CAN_EVENT_UNIT_PASSIVE

```c
ARM_CAN_EVENT_UNIT_PASSIVE
```

\sa ARM_CAN_SignalUnitEvent

### ARM_CAN_EVENT_UNIT_BUS_OFF

```c
ARM_CAN_EVENT_UNIT_BUS_OFF
```

\sa ARM_CAN_SignalUnitEvent
******************************************************************************************************************
