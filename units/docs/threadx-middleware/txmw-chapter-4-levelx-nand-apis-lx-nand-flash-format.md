---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-format"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_format"
summary: "This service erase the NAND flash and formats the NAND flash instance with the specified name, driver initialization function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-format"
license: "MIT"
mode: "V"
---

Format NAND flash instance

### Prototype

```c
UINT  _lx_nand_flash_format(LX_NAND_FLASH* nand_flash, CHAR* name,
                            UINT(*nand_driver_initialize)(LX_NAND_FLASH*),
                            ULONG* memory_ptr, UINT memory_size);
```

### Description

This service erase the NAND flash and formats the NAND flash instance with the specified name, driver initialization function. Note that the driver initialization function is responsible for installing various function pointers for reading, writing, and erasing blocks/pages of the NAND hardware associated with this NAND flash instance. 

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *name*: Name of NAND flash instance.
- *nand_driver_initialize*: Function pointer to NAND flash driver initialization function. Please refer to Chapter 3 of this guide for more details on NAND flash driver responsibilities.
- *memory_ptr*: Pointer to working memory for LevelX.
- *memory_size*: Size of working memory for LevelX. The size must be at least 7 * total block count + 2 * page size.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error formatting NAND flash instance.
- **LX_NO_BLOCKS**: (0x0B) Not enough blocks to format NAND flash instance.

### Allowed From

Threads

### Example

```c
/* Format NAND flash instance "my_nand_flash". */
status = lx_nand_flash_format(&my_nand_flash, "my nand flash",  
    my_nand_driver_initialize, &my_memory, sizeof(my_memory));

/* If status is LX_SUCCESS the NAND is erased and initial format is built, it can be opened later by calling lx_nand_flash_open. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
