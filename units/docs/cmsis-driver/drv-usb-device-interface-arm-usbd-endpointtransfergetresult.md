---
id: "drv-usb-device-interface-arm-usbd-endpointtransfergetresult"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_EndpointTransferGetResult"
summary: "The function ARM_USBD_EndpointTransferGetResult returns the number of successfully transferred data bytes started by ARM_USBD_EndpointTransfer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_USBD_EndpointTransferGetResult (uint8_t ep_addr)
```


The function **ARM_USBD_EndpointTransferGetResult** returns the number of successfully transferred data bytes started by ARM_USBD_EndpointTransfer.

The parameter **ep_addr** specifies the endpoint address.
****************************************************************************************************************
