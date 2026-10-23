---
id: "drv-usb-host-interface-arm-usbh-pipetransferabort"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeTransferAbort"
summary: "The function ARM_USBH_PipeTransferAbort aborts an active pipe transfer started by ARM_USBH_PipeTransfer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PipeTransferAbort (ARM_USBH_PIPE_HANDLE pipe_hndl)
```



The function **ARM_USBH_PipeTransferAbort** aborts an active pipe transfer started by ARM_USBH_PipeTransfer.
****************************************************************************************************************
