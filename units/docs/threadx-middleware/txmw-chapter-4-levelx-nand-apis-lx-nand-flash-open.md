---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-open"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_open"
summary: "This service opens a NAND flash instance with the specified NAND flash control block and driver initialization function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-open"
license: "MIT"
mode: "V"
---

Open NAND flash instance

### Prototype

```c
UINT lx_nand_flash_open(
    LX_NAND_FLASH *nand_flash, 
    CHAR *name,  
    UINT (*nand_driver_initialize) (LX_NAND_FLASH *),
    ULONG* memory_ptr, 
    UINT memory_size);
```

### Description

This service opens a NAND flash instance with the specified NAND flash control block and driver initialization function. Note that the driver initialization function is responsible for installing various function pointers for reading, writing, and erasing blocks/pages of the NAND hardware associated with this NAND flash instance.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *name*: Name of NAND flash instance.
- *nand_driver_initialize*: Function pointer to NAND flash driver initialization function. Please refer to Chapter 3 of this guide for more details on NAND flash driver responsibilities.
- *memory_ptr*: Pointer to working memory for LevelX.
- *memory_size*: Size of working memory for LevelX. The size must be at least 7 * total block count + 2 * page size.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error opening NAND flash instance.
- **LX_NO_MEMORY**: (0x08) Driver did not provide buffer for reading one page into RAM.

### Allowed From

Threads

### Example

```c
/* Open NAND flash instance "my_nand_flash" with the driver "my_nand_driver_initialize". */ 
status = lx_nand_flash_open(&my_nand_flash,"my nand flash",  
    my_nand_driver_initialize, &my_memory, sizeof(my_memory));  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- lx_nand_flash_close
- lx_nand_flash_initialize
- lx_nand_flash_page_ecc_check
- lx_nand_flash_page_ecc_compute
- lx_nand_flash_sectors_read
- lx_nand_flash_sectors_release
- lx_nand_flash_sectors_write
