---
id: "drv-storage-interface-arm-storage-getinfo"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetInfo"
summary: "Get information about the Storage device; stored in the structure ARMSTORAGEINFO."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_GetInfo (ARM_STORAGE_INFO *info)
```


Get information about the Storage device; stored in the structure ARM_STORAGE_INFO.

**Note:** It is the caller's responsibility to ensure that the buffer passed in
       is able to be initialized with a ARM_STORAGE_INFO.

**Note:** This API returns synchronously--it does not result in an invocation
   of a completion callback.
******************************************************************************************************************
