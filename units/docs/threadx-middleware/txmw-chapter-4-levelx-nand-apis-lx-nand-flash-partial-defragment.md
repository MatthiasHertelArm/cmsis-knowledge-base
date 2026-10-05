---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-partial-defragment"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_partial_defragment"
summary: "Partial defragment of NAND flash instance"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-partial-defragment"
license: "MIT"
mode: "V"
---

Partial defragment of NAND flash instance

### Prototype

```c
UINT lx_nand_flash_partial_defragment(
    LX_NAND_FLASH *nand_flash,  
    UINT max_blocks);
```

### Description

This service is deprecated and not supported.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *max_blocks*: Maximum number of blocks.

### Return Values

- **LX_NOT_SUPPORTED**: (0x0C) Not supported.

### Allowed From

Threads

### Example

```c
/* Defragment 1 block of NAND flash instance "my_nand_flash". */  
status = lx_nand_flash_partial_defragment(&my_nand_flash, 1);  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
