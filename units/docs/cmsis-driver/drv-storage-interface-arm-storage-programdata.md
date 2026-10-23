---
id: "drv-storage-interface-arm-storage-programdata"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_ProgramData"
summary: "Write the contents of a given memory buffer into a range of storage memory. In the case of flash memory, the destination range in storage memory typically has its contents in an erased state from a preceding erase operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_ProgramData (uint64_t addr, const void *data, uint32_t size)
```


Write the contents of a given memory buffer into a range of
storage memory. In the case of flash memory, the destination range in
storage memory typically has its contents in an erased state from a
preceding erase operation. The source memory buffer is owned by the
caller and should remain accessible for the lifetime of this command.

**Note:** It is best for the middleware to write in units of
   'optimal_program_unit' (ARM_STORAGE_INFO) of the device.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.
******************************************************************************************************************
