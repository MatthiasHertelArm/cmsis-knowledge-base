---
id: "drv-usbh-port-events"
type: "concept"
domain: "drivers"
title: "USBH Port Events"
summary: "The USB Host driver generates Port call back events that are notified via the function ARMUSBHSignalPortEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

The USB Host driver generates Port call back events that are notified via the function ARM_USBH_SignalPortEvent.
 
This section provides the event values for the ARM_USBH_SignalPortEvent callback function.

The following call back notification events are generated:

### ARM_USBH_EVENT_CONNECT

```c
ARM_USBH_EVENT_CONNECT
```


### ARM_USBH_EVENT_DISCONNECT

```c
ARM_USBH_EVENT_DISCONNECT
```


### ARM_USBH_EVENT_OVERCURRENT

```c
ARM_USBH_EVENT_OVERCURRENT
```


### ARM_USBH_EVENT_RESET

```c
ARM_USBH_EVENT_RESET
```


### ARM_USBH_EVENT_SUSPEND

```c
ARM_USBH_EVENT_SUSPEND
```


### ARM_USBH_EVENT_RESUME

```c
ARM_USBH_EVENT_RESUME
```


### ARM_USBH_EVENT_REMOTE_WAKEUP

```c
ARM_USBH_EVENT_REMOTE_WAKEUP
```
