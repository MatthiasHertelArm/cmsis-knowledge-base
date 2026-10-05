---
id: "drv-storage-interface-arm-storage-status"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_STORAGE_STATUS"
summary: "Structure with information about the status of the Storage device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_STORAGE_STATUS
```


Structure with information about the status of the Storage device.

The flag **busy** indicates that the driver is busy executing read/program/erase operation.

The flag **error** flag is cleared on start of read/program/erase operation and is set at the end of the current operation in case of error.

**Returned by:**
  - ARM_Storage_GetStatus
****************************************************************************************************************
