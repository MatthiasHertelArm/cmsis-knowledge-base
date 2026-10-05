---
id: "drv-usb-device-interface-arm-usbd-devicesetaddress"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_DeviceSetAddress"
summary: "Assigns an address to the device. Note: This function is called after status stage of the Set Address request (after IN packet in status stage was sent with the old address)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_DeviceSetAddress (uint8_t dev_addr)
```


Assigns an address to the device.
**Note:** This function is called after status stage of the Set Address request (after IN packet in status stage was sent with the old address).

****************************************************************************************************************
