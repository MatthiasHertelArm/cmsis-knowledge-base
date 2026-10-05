---
id: "drv-usbh-pipe-events"
type: "concept"
domain: "drivers"
title: "USBH Pipe Events"
summary: "The USB Host driver generates Pipe call back events that are notified via the function ARM_USBH_SignalPipeEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

The USB Host driver generates Pipe call back events that are notified via the function ARM_USBH_SignalPipeEvent.
 
This section provides the event values for the ARM_USBH_SignalPipeEvent callback function.

The following call back notification events are generated:

### ARM_USBH_EVENT_TRANSFER_COMPLETE

```c
ARM_USBH_EVENT_TRANSFER_COMPLETE
```


### ARM_USBH_EVENT_HANDSHAKE_NAK

```c
ARM_USBH_EVENT_HANDSHAKE_NAK
```


### ARM_USBH_EVENT_HANDSHAKE_NYET

```c
ARM_USBH_EVENT_HANDSHAKE_NYET
```


### ARM_USBH_EVENT_HANDSHAKE_MDATA

```c
ARM_USBH_EVENT_HANDSHAKE_MDATA
```


### ARM_USBH_EVENT_HANDSHAKE_STALL

```c
ARM_USBH_EVENT_HANDSHAKE_STALL
```


### ARM_USBH_EVENT_HANDSHAKE_ERR

```c
ARM_USBH_EVENT_HANDSHAKE_ERR
```


### ARM_USBH_EVENT_BUS_ERROR

```c
ARM_USBH_EVENT_BUS_ERROR
```
