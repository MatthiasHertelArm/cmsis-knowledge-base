---
id: "drv-usb-device-interface-arm-usbd-getcapabilities"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_GetCapabilities"
summary: "The function ARM_USBD_GetCapabilities returns information about capabilities in this driver implementation. The data fields of the structure ARM_USBD_CAPABILITIES encode various capabilities, for example if the hardware can create signal events using the ARM_USBD_SignalDeviceEvent callback function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_USBD_CAPABILITIES ARM_USBD_GetCapabilities (void)
```


The function **ARM_USBD_GetCapabilities** returns information about capabilities in this driver implementation.
The data fields of the structure ARM_USBD_CAPABILITIES encode various capabilities, for example
if the hardware can create signal events using the ARM_USBD_SignalDeviceEvent callback function.
 
Example:
```
extern ARM_DRIVER_USBD Driver_USBD0;
ARM_DRIVER_USBD *drv_info;
  
void read_capabilities (void)  {
  ARM_USBD_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_USBD0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
****************************************************************************************************************
