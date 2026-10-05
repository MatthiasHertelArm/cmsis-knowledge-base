---
id: "drv-usb-host-interface-arm-usbh-pipe-handle"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PIPE_HANDLE"
summary: "Each pipe is identified through a unique number, which is created by the function ARMUSBHPipeCreate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_USBH_PIPE_HANDLE
```

 
Each pipe is identified through a unique number, which is created by the function ARM_USBH_PipeCreate.

**Parameter for:**
 - ARM_USBH_PipeModify,
   ARM_USBH_PipeDelete,
   ARM_USBH_PipeReset,
   ARM_USBH_PipeTransfer,
   ARM_USBH_PipeTransferGetResult,
   ARM_USBH_PipeTransferAbort,
   ARM_USBH_SignalPipeEvent

**Retruned by:**
 - ARM_USBH_PipeCreate
****************************************************************************************************************
