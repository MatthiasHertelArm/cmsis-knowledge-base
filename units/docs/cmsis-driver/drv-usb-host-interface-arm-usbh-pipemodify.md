---
id: "drv-usb-host-interface-arm-usbh-pipemodify"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeModify"
summary: "The function ARM_USBH_PipeModify modifies a pipe configuration that was created with ARM_USBH_PipeCreate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PipeModify (ARM_USBH_PIPE_HANDLE pipe_hndl, uint8_t dev_addr, uint8_t dev_speed, uint8_t hub_addr, uint8_t hub_port, uint16_t ep_max_packet_size)
```


The function **ARM_USBH_PipeModify** modifies a pipe configuration that was created with ARM_USBH_PipeCreate.
****************************************************************************************************************
