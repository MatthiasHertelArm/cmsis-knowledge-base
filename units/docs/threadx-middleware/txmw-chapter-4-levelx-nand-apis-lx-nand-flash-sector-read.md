---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-sector-read"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_sector_read"
summary: "This service reads the logical sector from the NAND flash instance and if successful returns the contents in the supplied buffer. Note that NAND sector size is always the page size of the underlying NAND hardware."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-sector-read"
license: "MIT"
mode: "V"
---

Read NAND flash sector

### Prototype

```c
UINT lx_nand_flash_sector_read(
    LX_NAND_FLASH *nand_flash,  
    ULONG logical_sector, 
    VOID *buffer);
```

### Description

This service reads the logical sector from the NAND flash instance and if successful returns the contents in the supplied buffer. Note that NAND sector size is always the page size of the underlying NAND hardware.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *logical_sector*: Logical sector to read.
- *buffer*: Pointer to destination for contents of the logical sector. Note that the buffer is assumed to be the size of the NAND flash page size and aligned for ULONG access.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error reading NAND flash sector.

### Allowed From

Threads

### Example

```c
/* Read logical sector 20 of the NAND flash instance "my_nand_flash" and place contents in "buffer". */
status = lx_nand_flash_sector_read(&my_nand_flash, 20, buffer);  
  
/* If status is LX_SUCCESS, "buffer" contains the contents of logical sector 20. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
