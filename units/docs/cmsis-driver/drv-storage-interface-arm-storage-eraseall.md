---
id: "drv-storage-interface-arm-storage-eraseall"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_EraseAll"
summary: "This optional function erases the complete device. If the device does not support global erase then the function returns the error value \\ref ARM_DRIVER_ERROR_UNSUPPORTED. The data field 'erase_all' = 1 of the structure ARM_STORAGE_CAPABILITIES encodes that ARM_Storage_EraseAll is supported."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_EraseAll (void)
```


This optional function erases the complete device. If the device does not
support global erase then the function returns the error value \ref
ARM_DRIVER_ERROR_UNSUPPORTED. The data field **'erase_all'** =
`1` of the structure ARM_STORAGE_CAPABILITIES encodes that
ARM_Storage_EraseAll is supported.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
