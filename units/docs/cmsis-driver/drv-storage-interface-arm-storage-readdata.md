---
id: "drv-storage-interface-arm-storage-readdata"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_ReadData"
summary: "Read the contents of a range of storage memory into a buffer supplied by the caller. The buffer is owned by the caller and should remain accessible for the lifetime of this command."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_ReadData (uint64_t addr, void *data, uint32_t size)
```


Read the contents of a range of storage memory into a buffer
supplied by the caller. The buffer is owned by the caller and should
remain accessible for the lifetime of this command.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
