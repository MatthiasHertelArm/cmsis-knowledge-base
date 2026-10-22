---
id: "drv-usb-host-interface-arm-usbh-portvbusonoff"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PortVbusOnOff"
summary: "The function ARM_USBH_PortVbusOnOff controls the VBUS signal of the specified port."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_PortVbusOnOff (uint8_t port, bool vbus)
```


The function **ARM_USBH_PortVbusOnOff** controls the VBUS signal of the specified port.  
****************************************************************************************************************
