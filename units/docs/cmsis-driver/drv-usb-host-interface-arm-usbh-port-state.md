---
id: "drv-usb-host-interface-arm-usbh-port-state"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PORT_STATE"
summary: "This structure stores information about the state of the USB Host Port. The data fields encode whether a device is connected to the port, if port overcurrent is detected, and the port speed."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_USBH_PORT_STATE
```


This structure stores information about the state of the USB Host Port. The data fields encode whether a device 
is connected to the port, if port overcurrent is detected, and the port speed.

**Returned by:**
  - ARM_USBH_PortGetState
****************************************************************************************************************
