---
id: "drv-usb-host-interface-arm-usbh-signalpipeevent"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_SignalPipeEvent"
summary: "The function ARMUSBHSignalPipeEvent is a callback function registered by the function ARMUSBHInitialize."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_USBH_SignalPipeEvent (ARM_USBH_PIPE_HANDLE pipe_hndl, uint32_t event)
```


The function **ARM_USBH_SignalPipeEvent** is a callback function registered by the function ARM_USBH_Initialize. 

The parameter **pipe_hndl** specifies the pipe handle. \n
The parameter **event** indicates one or more events that occurred during driver operation.
Each event is encoded in a separate bit and therefore it is possible to signal multiple events within the same call. 

The following events can be generated:

Parameter **event**                       | Bit| Description 
:-----------------------------------------|---:|:-----------
ARM_USBH_EVENT_TRANSFER_COMPLETE     | 0  | Occurs after all the data has been transferred without errors.
ARM_USBH_EVENT_HANDSHAKE_NAK         | 1  | Occurs when NAK Handshake is received before all the data is transferred.
ARM_USBH_EVENT_HANDSHAKE_NYET        | 2  | Occurs when NYET Handshake is received before all the data is transferred.
ARM_USBH_EVENT_HANDSHAKE_MDATA       | 3  | Occurs when MDATA Handshake is received before all the data is transferred.
ARM_USBH_EVENT_HANDSHAKE_STALL       | 4  | Occurs when STALL Handshake is received before all the data is transferred.
ARM_USBH_EVENT_HANDSHAKE_ERR         | 5  | Occurs when ERR Handshake is received before all the data is transferred.
ARM_USBH_EVENT_BUS_ERROR             | 6  | Occurs when bus error is detected before all the data is transferred.

**See also:**
 - ARM_USBH_PipeCreate
****************************************************************************************************************
