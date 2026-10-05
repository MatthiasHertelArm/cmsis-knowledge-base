---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-close"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_close"
summary: "This service closes the previously opened NAND flash instance."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-close"
license: "MIT"
mode: "V"
---

Close NAND flash instance

### Prototype

```c
UINT lx_nand_flash_close(LX_NAND_FLASH *nand_flash);
```

### Description

This service closes the previously opened NAND flash instance.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error closing flash instance.

### Allowed From

Threads

### Example

```c
/* Close NAND flash instance "my_nand_flash". */
status = lx_nand_flash_close(&my_nand_flash);  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
