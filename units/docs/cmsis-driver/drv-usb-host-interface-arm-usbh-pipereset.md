---
id: "drv-usb-host-interface-arm-usbh-pipereset"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeReset"
summary: "The function ARM_USBH_PipeReset clears Halt condition and resets data toggle on the specified pipe."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PipeReset (ARM_USBH_PIPE_HANDLE pipe_hndl)
```


The function **ARM_USBH_PipeReset** clears Halt condition and resets data toggle on the specified pipe.
****************************************************************************************************************
