---
id: "drv-sai-interface-arm-sai-getversion"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_GetVersion"
summary: "The function ARM_SAI_GetVersion returns version information of the driver implementation in ARM_DRIVER_VERSION - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
ARM_DRIVER_VERSION ARM_SAI_GetVersion (void)
```


The function **ARM_SAI_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

**Example:**
```
extern ARM_DRIVER_SAI Driver_SAI0;
ARM_DRIVER_SAI *drv_info;
 
void setup_sai (void)  {
  ARM_DRIVER_VERSION  version;
 
  drv_info = &Driver_SAI0;  
  version = drv_info->GetVersion ();
  if (version.api < 0x10A)  {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```
****************************************************************************************************************
