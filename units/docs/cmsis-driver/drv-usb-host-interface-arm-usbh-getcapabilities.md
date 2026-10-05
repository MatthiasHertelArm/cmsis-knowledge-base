---
id: "drv-usb-host-interface-arm-usbh-getcapabilities"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_GetCapabilities"
summary: "The function ARM_USBH_GetCapabilities returns information about capabilities in this driver implementation. The data fields of the structure ARM_USBH_CAPABILITIES encode various capabilities, for example available HUB ports or if the hardware can generate signal events using the ARM_USBH_SignalPortEvent callback function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_USBH_CAPABILITIES ARM_USBH_GetCapabilities (void)
```


The function **ARM_USBH_GetCapabilities** returns information about capabilities in this driver implementation.
The data fields of the structure ARM_USBH_CAPABILITIES encode various capabilities, for example
available HUB ports or if the hardware can generate signal events using the ARM_USBH_SignalPortEvent 
callback function.
 
Example:
```
extern ARM_DRIVER_USBH Driver_USBH0;
ARM_DRIVER_USBH *drv_info;
  
void read_capabilities (void)  {
  ARM_USBH_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_USBH0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
****************************************************************************************************************
