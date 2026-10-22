---
id: "drv-storage-interface-arm-storage-getstatus"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetStatus"
summary: "Get the status of the current (or previous) command executed by the storage controller; stored in the structure ARM_STORAGE_STATUS."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_STORAGE_STATUS ARM_Storage_GetStatus (void)
```


Get the status of the current (or previous) command executed by the
storage controller; stored in the structure ARM_STORAGE_STATUS.

**Note:** This API returns synchronously--it does not result in an invocation
   of a completion callback.
******************************************************************************************************************
