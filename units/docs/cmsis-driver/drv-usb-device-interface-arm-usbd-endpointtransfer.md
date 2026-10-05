---
id: "drv-usb-device-interface-arm-usbd-endpointtransfer"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_EndpointTransfer"
summary: "The function ARMUSBDEndpointTransfer reads from or writes data to an USB Endpoint."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_EndpointTransfer (uint8_t ep_addr, uint8_t *data, uint32_t num)
```



The function **ARM_USBD_EndpointTransfer** reads from or writes data to an USB Endpoint.

The parameter **ep_addr** specifies the endpoint address. \n
The parameter **data** is a buffer for data to read or data to write. \n
The parameter **num** is the number of bytes to transfer (must be multiple of endpoint maximum packet size for Read transfers).

The function is non-blocking and returns as soon as the driver starts the operation on the specified endpoint. 
During the operation it is not allowed to call this function again on the same endpoint. 
Also the data buffer must stay allocated and the contents of data must not be modified.

Direction in the endpoint address specifies the type of transfer:
- Endpoint Read for OUT endpoint (direction = 0)
- Endpoint Write for IN endpoint (direction = 1)

Endpoint Read is finished when the requested number of data bytes have been received or when a short packet or ZLP (Zero-Length Packet) has been received.
Completion of operation is indicated by ARM_USBD_EVENT_OUT event. Number of successfully received data bytes can be retrieved 
by calling ARM_USBD_EndpointTransferGetResult.

Endpoint Write is finished when the requested number of data bytes have been sent.
Completion of operation is indicated by ARM_USBD_EVENT_IN event. Number of successfully sent data bytes can be retrieved 
by calling ARM_USBD_EndpointTransferGetResult.

Transfer operation can be aborted by calling ARM_USBD_EndpointTransferAbort.
****************************************************************************************************************
