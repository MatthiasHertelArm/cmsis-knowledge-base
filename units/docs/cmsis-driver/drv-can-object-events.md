---
id: "drv-can-object-events"
type: "concept"
domain: "drivers"
title: "CAN Object Events"
summary: "Callback objects events notified via ARM_CAN_SignalObjectEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

Callback objects events notified via ARM_CAN_SignalObjectEvent.

The CAN driver generates callback objects events that are notified via the function ARM_CAN_SignalObjectEvent.

The following callback notification object events are generated:

### ARM_CAN_EVENT_SEND_COMPLETE

```c
ARM_CAN_EVENT_SEND_COMPLETE
```

\sa ARM_CAN_SignalObjectEvent

### ARM_CAN_EVENT_RECEIVE

```c
ARM_CAN_EVENT_RECEIVE
```

\sa ARM_CAN_SignalObjectEvent

### ARM_CAN_EVENT_RECEIVE_OVERRUN

```c
ARM_CAN_EVENT_RECEIVE_OVERRUN
```

\sa ARM_CAN_SignalObjectEvent
******************************************************************************************************************
