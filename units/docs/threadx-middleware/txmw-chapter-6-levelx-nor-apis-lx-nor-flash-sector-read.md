---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-sector-read"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_sector_read"
summary: "This service reads the logical sector from the NOR flash instance and if successful returns the contents in the supplied buffer. Note that NOR sector size is always 512 bytes."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-sector-read"
license: "MIT"
mode: "V"
---

Read NOR flash sector

### Prototype

```c
UINT lx_nor_flash_sector_read(
    LX_NOR_FLASH *nor_flash,  
    ULONG logical_sector, 
    VOID *buffer);
```

### Description

This service reads the logical sector from the NOR flash instance and if successful returns the contents in the supplied buffer. Note that NOR sector size is always 512 bytes.

### Input Parameters

- *nor_flash* NOR flash instance pointer.
- *logical_sector*: Logical sector to read.
- *buffer*: Pointer to destination for contents of the logical sector. Note that the buffer is assumed to be 512 bytes and aligned for ULONG access.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error reading NOR flash sector.

### Allowed From

Threads

### Example

```c
/* Read logical sector 20 of the NOR flash instance "my_nor_flash" and place contents in "buffer". */ 
status = lx_nor_flash_sector_read(&my_nor_flash, 20, buffer);  
  
/* If status is LX_SUCCESS, "buffer" contains the contents of logical sector 20. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
