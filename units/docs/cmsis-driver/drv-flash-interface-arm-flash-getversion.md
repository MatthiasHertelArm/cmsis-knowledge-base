---
id: "drv-flash-interface-arm-flash-getversion"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_GetVersion"
summary: "The function ARMFlashGetVersion returns version information of the driver implementation in ARMDRIVERVERSION - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_Flash_GetVersion (void)
```


The function **ARM_Flash_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

Example:
```
extern ARM_DRIVER_FLASH Driver_Flash0;
ARM_DRIVER_FLASH *drv_info;
 
void read_version (void)  {
  ARM_DRIVER_VERSION  version;
 
  drv_info = &Driver_Flash0;  
  version = drv_info->GetVersion ();
  if (version.api < 0x10A)   {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```
******************************************************************************************************************
