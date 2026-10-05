---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-extended-cache-enable"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_extended_cache_enable"
summary: "This service is deprecated and not supported."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-extended-cache-enable"
license: "MIT"
mode: "V"
---

Enable/disable extended NAND cache

### Prototype

```c
UINT lx_nand_flash_extended_cache_enable(
    LX_NAND_FLASH
    *nand_flash,  
    VOID *memory, 
    ULONG size);
```

### Description

This service is deprecated and not supported.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.  
- *memory*: Starting address for cache memory aligned for ULONG access. A value of LX_NULL disables the cache.  
- *size*: The size in bytes of the memory supplied.

### Return Values

- **LX_NOT_SUPPORTED**: (0x0C) Not supported.

### Allowed From

Threads

### Example

```c
/* Enable the NAND flash cache for the instance "my_nand_flash". */
status = lx_nand_flash_extended_cache_enable(&my_nand_flash,  
    &my_memory, sizeof(my_memory));  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
