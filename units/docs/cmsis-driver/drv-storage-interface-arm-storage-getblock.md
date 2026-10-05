---
id: "drv-storage-interface-arm-storage-getblock"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetBlock"
summary: "Storage Interface: ARM_Storage_GetBlock"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_GetBlock(uint64_t addr, ARM_STORAGE_BLOCK *block);
```

**Note:** This API returns synchronously--it does not result in an invocation
    of a completion callback.
******************************************************************************************************************
