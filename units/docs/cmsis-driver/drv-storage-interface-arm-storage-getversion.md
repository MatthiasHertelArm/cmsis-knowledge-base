---
id: "drv-storage-interface-arm-storage-getversion"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetVersion"
summary: "The function ARM_Storage_GetVersion returns version information of the driver implementation in ARM_DRIVER_VERSION. - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_Storage_GetVersion (void)
```


The function **ARM_Storage_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION.
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

Example:
```
extern ARM_DRIVER_STORAGE *drv_info;
 
void read_version (void)  {
  ARM_DRIVER_VERSION  version;
 
  version = drv_info->GetVersion ();
  if (version.api < 0x10A)   {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```

**Note:** HAPI returns synchronously--it does not result in an invocation
   of a completion callback.

**Note:** The function GetVersion() can be called any time to obtain the
   required information from the driver (even before initialization). It
   always returns the same information.
******************************************************************************************************************
