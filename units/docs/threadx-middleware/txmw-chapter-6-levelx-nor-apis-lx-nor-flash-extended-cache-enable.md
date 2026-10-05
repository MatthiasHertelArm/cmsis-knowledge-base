---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-extended-cache-enable"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_extended_cache_enable"
summary: "This service implements a NOR sector cache layer in RAM using the memory supplied by the application. Each 512 bytes of memory supplied translates to one NOR sector that can be cached."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-extended-cache-enable"
license: "MIT"
mode: "V"
---

Enable/disable extended NOR cache

### Prototype

```c
UINT lx_nor_flash_extended_cache_enable(
    LX_NOR_FLASH *nor_flash,  
    VOID *memory, 
    ULONG size);
```

### Description

This service implements a NOR sector cache layer in RAM using the memory supplied by the application. Each 512 bytes of memory supplied translates to one NOR sector that can be cached. The sectors cached are those that contain the block control information, e.g., erase count, free sector map, and sector mapping information. Data sectors are not stored in this cache.

### Input Parameters

- **nor_flash**: NOR flash instance pointer.  
- **memory**: Starting address for cache memory, aligned for ULONG access. A value of LX_NULL disables the cache.  
- **size**: The size in bytes of the memory supplied (should be multiple of 512 bytes).

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Not enough memory for one NOR sector.
- **LX_DISABLED**: (0x09) NOR extended cache disabled by configuration option.

### Allowed From

Threads

### Example

```c
/* Enable the NOR flash cache for the instance "my_nor_flash". */  
status = lx_nor_flash_extended_cache_enable(&my_nor_flash,  
    &my_memory, sizeof(my_memory));  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
