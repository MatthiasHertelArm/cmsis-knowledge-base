---
id: "drv-storage-interface-arm-storage-getcapabilities"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetCapabilities"
summary: "The function ARM_Storage_GetCapabilities returns information about capabilities in this driver implementation. The data fields of the struct ARM_STORAGE_CAPABILITIES encode various capabilities, for example if the device is able to execute operations asynchronously."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_STORAGE_CAPABILITIES ARM_Storage_GetCapabilities (void)
```



The function **ARM_Storage_GetCapabilities** returns information about
capabilities in this driver implementation. The data fields of the struct
ARM_STORAGE_CAPABILITIES encode various capabilities, for example if the device
is able to execute operations asynchronously.

Example:
```
extern ARM_DRIVER_STORAGE *drv_info;
 
void read_capabilities (void)  {
  ARM_STORAGE_CAPABILITIES drv_capabilities;
 
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities

}
```

**Note:** This API returns synchronously--it does not result in an invocation
   of a completion callback.

**Note:** The function GetCapabilities() can be called any time to obtain the
   required information from the driver (even before initialization). It
   always returns the same information.
******************************************************************************************************************
