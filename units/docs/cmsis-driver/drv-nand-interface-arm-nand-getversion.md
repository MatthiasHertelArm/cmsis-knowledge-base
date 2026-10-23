---
id: "drv-nand-interface-arm-nand-getversion"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_GetVersion"
summary: "The function ARM_NAND_GetVersion returns version information of the driver implementation in ARM_DRIVER_VERSION - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_NAND_GetVersion (void)
```


The function **ARM_NAND_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

Example:
```
extern ARM_DRIVER_NAND Driver_NAND0;
ARM_DRIVER_NAND *drv_info;
 
void setup_nand (void)  {
  ARM_DRIVER_VERSION  version;
 
  drv_info = &Driver_NAND0;  
  version = drv_info->GetVersion ();
  if (version.api < 0x10A)   {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```
******************************************************************************************************************
