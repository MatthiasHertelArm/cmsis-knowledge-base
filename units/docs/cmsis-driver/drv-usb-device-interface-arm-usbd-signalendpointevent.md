---
id: "drv-usb-device-interface-arm-usbd-signalendpointevent"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_SignalEndpointEvent"
summary: "The function ARM_USBD_SignalEndpointEvent is a callback function registered by the function ARM_USBD_Initialize."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_USBD_SignalEndpointEvent (uint8_t ep_addr, uint32_t event)
```


The function **ARM_USBD_SignalEndpointEvent** is a callback function registered by the function ARM_USBD_Initialize. 

The argument _ep_addr_ specifies the endpoint. \n
The parameter **event** indicates one or more events that occurred during driver operation.
Each event is encoded in a separate bit and therefore it is possible to signal multiple events within the same call. 

The following events can be generated:

Event                                    | Bit | Description 
:----------------------------------------|----:|:-----------
ARM_USBD_EVENT_SETUP                |  0  | Occurs when SETUP packet is received over Control Endpoint.
ARM_USBD_EVENT_OUT                  |  1  | Occurs when data is received over OUT Endpoint.
ARM_USBD_EVENT_IN                   |  2  | Occurs when data is sent over IN Endpoint.
****************************************************************************************************************
