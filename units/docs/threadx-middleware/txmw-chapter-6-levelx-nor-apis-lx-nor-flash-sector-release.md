---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-sector-release"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_sector_release"
summary: "This service releases the logical sector mapping in the NOR flash instance. Releasing a logical sector when not used makes the LevelX wear leveling more efficient."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-sector-release"
license: "MIT"
mode: "V"
---

Release NOR flash sector

### Prototype

```c
UINT lx_nor_flash_sector_release(
    LX_NOR_FLASH *nor_flash,
    ULONG logical_sector);
```

### Description

This service releases the logical sector mapping in the NOR flash instance. Releasing a logical sector when not used makes the LevelX wear leveling more efficient.

### Input Parameters

- *nor_flash*: NOR flash instance pointer.
- *logical_sector*: Logical sector to release.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error NOR flash sector write.

### Allowed From

Threads

### Example

```c
/* Release logical sector 20 of the NOR flash instance "my_nor_flash". */  
status = lx_nor_flash_sector_release(&my_nor_flash, 20);  
  
/* If status is LX_SUCCESS, logical sector 20 has been released. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
