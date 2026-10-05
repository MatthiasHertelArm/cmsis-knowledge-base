---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-sectors-read"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_sectors_read"
summary: "This service reads the specified number of logical sectors from the NAND flash instance and if successful returns the contents in the supplied buffer. Note that NAND sector size is always the page size of the underlying NAND hardware."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-sectors-read"
license: "MIT"
mode: "V"
---

Read multiple NAND flash sectors

### Prototype

```c
UINT lx_nand_flash_sectors_read(
    LX_NAND_FLASH *nand_flash,  
    ULONG logical_sector, 
    VOID *buffer, 
    ULONG sector_count);
```

### Description

This service reads the specified number of logical sectors from the NAND flash instance and if successful returns the contents in the supplied buffer. Note that NAND sector size is always the page size of the underlying NAND hardware.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *logical_sector*: Logical sector to read.
- *buffer*: Pointer to destination for contents of the logical sector. Note that the logical sector size is the same as NAND flash page size and the buffer is assumed to be large enough to hold all the sectors to read and aligned for ULONG access.
- *sector_count*: Number of logical sectors to read.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error reading NAND flash sector.

### Allowed From

Threads

### Example

```c
/* Read 10 logical sectors starting at logical sector 20 of the NAND flash instance "my_nand_flash" and place contents in "buffer". */
status = lx_nand_flash_sectors_read(&my_nand_flash, 20, buffer, 10);

/* If status is LX_SUCCESS, "buffer" contains the contents of logical sectors 20 through 29. */
```
