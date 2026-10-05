---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-sector-write"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_sector_write"
summary: "This service writes the specified logical sector in the NOR flash instance."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-sector-write"
license: "MIT"
mode: "V"
---

Write NOR flash sector

### Prototype

```c
UINT lx_nor_flash_sector_write(
    LX_nor_FLASH *NOR_flash,
    ULONG logical_sector, 
    VOID *buffer);
```

### Description

This service writes the specified logical sector in the NOR flash instance.

### Input Parameters

- *nor_flash*: NOR flash instance pointer.
- *logical_sector*: Logical sector to write.
- *buffer*: Pointer to the contents of the logical sector. Note that the buffer is assumed to be 512 bytes aligned for ULONG access.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_NO_SECTORS**: (0x02) No more free sectors are available to perform the write.
- **LX_ERROR**: (0x01) Error releasing NOR flash sector.

### Allowed From

Threads

### Example

```c
/* Write logical sector 20 of the NOR flash instance "my_nor_flash" with the contents pointed to by "buffer". */ 
status = lx_nor_flash_sector_write(&my_nor_flash, 20, buffer);  
  
/* If status is LX_SUCCESS, logical sector 20 has been written with the contents of "buffer". */
```

### See Also

- [levelx NOR Services](#NOR_Services)
