---
id: "drv-usb-device-interface-arm-usbd-endpointtransferabort"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_EndpointTransferAbort"
summary: "The function ARM_USBD_EndpointTransferAbort aborts the transfer to an endpoint started by ARM_USBD_EndpointTransfer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_EndpointTransferAbort (uint8_t ep_addr)
```


The function **ARM_USBD_EndpointTransferAbort** aborts the transfer to an endpoint started by ARM_USBD_EndpointTransfer.

The parameter **ep_addr** specifies the endpoint address.
****************************************************************************************************************
