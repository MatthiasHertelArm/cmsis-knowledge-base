---
id: "drv-usb-device-interface-arm-usbd-endpointstall"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_EndpointStall"
summary: "The function ARM_USBD_EndpointStall sets or clears stall condition for the specified endpoint."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_EndpointStall (uint8_t ep_addr, bool stall)
```


The function **ARM_USBD_EndpointStall** sets or clears stall condition for the specified endpoint.

The parameter **ep_addr** specifies the endpoint address. \n
The parameter **stall** is a boolean parameter.
****************************************************************************************************************
