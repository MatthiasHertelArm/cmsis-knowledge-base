---
id: "drv-usb-host-interface-arm-usbh-pipetransfer"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeTransfer"
summary: "The function ARM_USBH_PipeTransfer generates packets for sending or receiving data from an USB Endpoint."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PipeTransfer (ARM_USBH_PIPE_HANDLE pipe_hndl, uint32_t packet, uint8_t *data, uint32_t num)
```


The function **ARM_USBH_PipeTransfer** generates packets for sending or receiving data from an USB Endpoint.

The function specifies the buffer with data to send or for data to receive and the number of bytes to transfer (must be multiple of device endpoint maximum packet size for receive).
It also specifies USBH_packets with parameter **packet.**

The function is non-blocking and returns as soon as the driver starts the operation on the specified pipe. During the operation it is not allowed to call this function again on the same pipe. Also the data buffer must stay allocated and the contents of data must not be modified.

Operation is completed when the the requested number of data bytes have been transferred and is indicated with ARM_USBH_EVENT_TRANSFER_COMPLETE event.
It can also finish earlier on reception of different handshake tokens which are also indicated through USBH_pipe_events.
 
Transfer operation can be aborted by calling ARM_USBH_PipeTransferAbort.
****************************************************************************************************************
