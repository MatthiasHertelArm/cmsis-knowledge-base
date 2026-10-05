---
id: "drv-usb-host-interface-arm-usbh-pipedelete"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeDelete"
summary: "The function ARM_USBH_PipeDelete deletes a pipe that was created with ARM_USBH_PipeCreate (deactivates the pipe and releases used resources)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PipeDelete (ARM_USBH_PIPE_HANDLE pipe_hndl)
```


The function **ARM_USBH_PipeDelete** deletes a pipe that was created with ARM_USBH_PipeCreate (deactivates the pipe and releases used resources).
****************************************************************************************************************
