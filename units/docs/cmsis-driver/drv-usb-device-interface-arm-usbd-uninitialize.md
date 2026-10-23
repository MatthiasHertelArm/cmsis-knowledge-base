---
id: "drv-usb-device-interface-arm-usbd-uninitialize"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_Uninitialize"
summary: "The function ARM_USBD_Uninitialize de-initializes the resources of USBD interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_Uninitialize (void)
```


The function **ARM_USBD_Uninitialize** de-initializes the resources of USBD interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
****************************************************************************************************************
