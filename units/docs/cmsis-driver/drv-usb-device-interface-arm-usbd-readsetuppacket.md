---
id: "drv-usb-device-interface-arm-usbd-readsetuppacket"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_ReadSetupPacket"
summary: "The function ARM_USBD_ReadSetupPacket reads the last SETUP packet (8 bytes) that was received over Control Endpoint (Endpoint 0) which is indicated by ARM_USBD_EVENT_SETUP event."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_ReadSetupPacket (uint8_t *setup)
```


The function **ARM_USBD_ReadSetupPacket** reads the last SETUP packet (8 bytes) that was received over Control Endpoint (Endpoint 0)
which is indicated by ARM_USBD_EVENT_SETUP event.

**See also:**
 - ARM_USBD_SignalEndpointEvent
****************************************************************************************************************
