---
id: "drv-usbd-device-events"
type: "concept"
domain: "drivers"
title: "USBD Device Events"
summary: "The USB Device driver generates Device call back events that are notified via the function ARM_USBD_SignalDeviceEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

The USB Device driver generates Device call back events that are notified via the function ARM_USBD_SignalDeviceEvent.
 
This section provides the event values for the ARM_USBD_SignalDeviceEvent callback function.

The following call back notification events are generated:

### ARM_USBD_EVENT_VBUS_ON

```c
ARM_USBD_EVENT_VBUS_ON
```


### ARM_USBD_EVENT_VBUS_OFF

```c
ARM_USBD_EVENT_VBUS_OFF
```


### ARM_USBD_EVENT_RESET

```c
ARM_USBD_EVENT_RESET
```


### ARM_USBD_EVENT_HIGH_SPEED

```c
ARM_USBD_EVENT_HIGH_SPEED
```


### ARM_USBD_EVENT_SUSPEND

```c
ARM_USBD_EVENT_SUSPEND
```


### ARM_USBD_EVENT_RESUME

```c
ARM_USBD_EVENT_RESUME
```
