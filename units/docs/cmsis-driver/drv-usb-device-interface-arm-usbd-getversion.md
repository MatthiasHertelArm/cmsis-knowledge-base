---
id: "drv-usb-device-interface-arm-usbd-getversion"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_GetVersion"
summary: "The function ARM_USBD_GetVersion returns version information of the driver implementation in ARM_DRIVER_VERSION - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_USBD_GetVersion (void)
```


The function **ARM_USBD_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

Example:
```
extern ARM_DRIVER_USBD Driver_USBD0;
ARM_DRIVER_USBD *drv_info;
 
void setup_usbd (void)  {
  ARM_DRIVER_VERSION  version;
 
  drv_info = &Driver_USBD0;  
  version = drv_info->GetVersion ();
  if (version.api < 0x10A)   {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```
****************************************************************************************************************
