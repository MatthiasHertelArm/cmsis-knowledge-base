---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-defragment"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_defragment"
summary: "This service is deprecated and not supported."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-defragment"
license: "MIT"
mode: "V"
---

Defragment NAND flash instance

### Prototype

```c
UINT lx_nand_flash_defragment(LX_NAND_FLASH *nand_flash);
```

### Description

This service is deprecated and not supported.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.

### Return Values

- **LX_NOT_SUPPORTED**: (0x0C) Not supported.

### Allowed From

Threads

### Example

```c
/* Defragment NAND flash instance "my_nand_flash". */  
status = lx_nand_flash_defragment(&my_nand_flash);  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
