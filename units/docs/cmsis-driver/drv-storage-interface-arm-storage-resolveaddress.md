---
id: "drv-storage-interface-arm-storage-resolveaddress"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_ResolveAddress"
summary: "Only applicable to devices with memory-mapped storage."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_Storage_ResolveAddress(uint64_t addr)
```


Only applicable to devices with memory-mapped storage.

**Note:** This API returns synchronously. The invocation should return quickly,
   and result in a resolved address.
******************************************************************************************************************
