---
id: "drv-usb-device-interface-arm-usbd-endpointconfigure"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_EndpointConfigure"
summary: "The function ARMUSBDEndpointConfigure configures an endpoint for transfers."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_EndpointConfigure (uint8_t ep_addr, uint8_t ep_type, uint16_t ep_max_packet_size)
```

       
The function **ARM_USBD_EndpointConfigure** configures an endpoint for transfers.


****************************************************************************************************************
