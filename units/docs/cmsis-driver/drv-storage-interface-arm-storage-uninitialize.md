---
id: "drv-storage-interface-arm-storage-uninitialize"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_Uninitialize"
summary: "It is called when the middleware component stops operation, and wishes to release the software resources used by the interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_Uninitialize (void)
```


It is called when the middleware component stops operation, and wishes to
release the software resources used by the interface.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
