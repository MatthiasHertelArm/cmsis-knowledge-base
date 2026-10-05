---
id: "drv-storage-interface-arm-storage-erase"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_Erase"
summary: "This function erases a range of storage specified by [addr, addr + size). Both 'addr' and 'addr + size' should align with the 'eraseunit'(s) of the respective owning storage block(s) (see \\ref ARMSTORAGEBLOCK and ARMSTORAGEBLOCKATTRIBUTES)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_Erase (uint64_t addr, uint32_t size)
```



This function erases a range of storage specified by [addr, addr +
size). Both 'addr' and 'addr + size' should align with the
'erase_unit'(s) of the respective owning storage block(s) (see \ref
ARM_STORAGE_BLOCK and ARM_STORAGE_BLOCK_ATTRIBUTES). The range to
be erased will have its contents returned to the un-programmed state--
i.e. to ARM_STORAGE_INFO::erased_value, which
is usually 1 to indicate the pattern of all ones: 0xFF.

**Note:** This API may execute asynchronously if
   ARM_STORAGE_CAPABILITIES::asynchronous_ops is set. Asynchronous
   execution is optional even if 'asynchronous_ops' is set.

**Note:** Erase() may return a smaller (positive) value than the size of the
   requested range. The returned value indicates the actual number of bytes
   erased. It is the caller's responsibility to follow up with an appropriate
   request to complete the operation.

**Note:** in the case of a failed erase (except when
   ARM_DRIVER_ERROR_PARAMETER, ARM_STORAGE_ERROR_PROTECTED, or
   ARM_STORAGE_ERROR_NOT_ERASABLE is returned synchronously), the
   requested range should be assumed to be in an unknown state. The
   previous contents may not be retained.
******************************************************************************************************************
