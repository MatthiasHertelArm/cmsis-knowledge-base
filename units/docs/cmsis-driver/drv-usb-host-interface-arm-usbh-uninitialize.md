---
id: "drv-usb-host-interface-arm-usbh-uninitialize"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_Uninitialize"
summary: "The function ARM_USBH_Uninitialize de-initializes the resources of USB Host interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_Uninitialize (void)
```


The function **ARM_USBH_Uninitialize** de-initializes the resources of USB Host interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
****************************************************************************************************************
