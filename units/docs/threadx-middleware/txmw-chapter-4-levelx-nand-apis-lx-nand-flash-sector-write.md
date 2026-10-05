---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-sector-write"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_sector_write"
summary: "This service writes the specified logical sector in the NAND flash instance."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-sector-write"
license: "MIT"
mode: "V"
---

Write NAND flash sector

### Prototype

```c
UINT lx_nand_flash_sector_write(
    LX_NAND_FLASH *nand_flash,
    ULONG logical_sector, 
    VOID *buffer);
```

### Description

This service writes the specified logical sector in the NAND flash instance.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *logical_sector*: Logical sector to write.
- *buffer*: Pointer to the contents of the logical sector. Note that the buffer is assumed to be the size of the NAND flash page size and aligned for ULONG access.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_NO_SECTORS**: (0x02) No more free sectors are available to perform the write.
- **LX_ERROR**: (0x01) Error writing NAND flash sector.

### Allowed From

Threads

### Example

```c
/* Write logical sector 20 of the NAND flash instance "my_nand_flash" with the contents pointed to by "buffer". */  
status = lx_nand_flash_sector_write(&my_nand_flash, 20, buffer);  
  
/* If status is LX_SUCCESS, logical sector 20 has been written with the contents of "buffer". */
```

### See Also

- [levelx NAND Services](#NAND_Services)
