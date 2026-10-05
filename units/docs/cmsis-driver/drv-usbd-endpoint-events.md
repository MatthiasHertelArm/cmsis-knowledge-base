---
id: "drv-usbd-endpoint-events"
type: "concept"
domain: "drivers"
title: "USBD Endpoint Events"
summary: "The USB Device driver generates Endpoint call back events that are notified via the function ARM_USBD_SignalEndpointEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

The USB Device driver generates Endpoint call back events that are notified via the function ARM_USBD_SignalEndpointEvent.
 
This section provides the event values for the ARM_USBD_SignalEndpointEvent callback function.

The following call back notification events are generated:

### ARM_USBD_EVENT_SETUP

```c
ARM_USBD_EVENT_SETUP
```


### ARM_USBD_EVENT_OUT

```c
ARM_USBD_EVENT_OUT
```


### ARM_USBD_EVENT_IN

```c
ARM_USBD_EVENT_IN
```
