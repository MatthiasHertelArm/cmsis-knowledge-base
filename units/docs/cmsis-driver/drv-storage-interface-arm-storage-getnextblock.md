---
id: "drv-storage-interface-arm-storage-getnextblock"
type: "concept"
domain: "drivers"
title: "Storage Interface: ARM_Storage_GetNextBlock"
summary: "This helper function fetches (an iterator to) the next block (or the first block if 'prev_block' is passed in as NULL). In the failure case, a terminating, invalid block iterator is filled into the out parameter: 'next_block'."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Storage.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Storage_GetNextBlock(const ARM_STORAGE_BLOCK* prev_block, ARM_STORAGE_BLOCK *next_block);
```


This helper function fetches (an iterator to) the next block (or
the first block if 'prev_block' is passed in as NULL). In the failure
case, a terminating, invalid block iterator is filled into the out
parameter: 'next_block'. In combination with \ref
ARM_STORAGE_VALID_BLOCK, it can be used to iterate over the sequence
of blocks within the storage map:

```
  ARM_STORAGE_BLOCK block;
  for (drv->GetNextBlock(NULL, &block); ARM_STORAGE_VALID_BLOCK(&block); drv->GetNextBlock(&block, &block)) {
      // make use of block
  }
```

**Note:** This API returns synchronously--it does not result in an invocation
    of a completion callback.
******************************************************************************************************************
