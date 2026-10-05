---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-initialize"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_initialize"
summary: "This service initializes LevelX NAND flash support. It must be called before any other LevelX NAND APIs."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-initialize"
license: "MIT"
mode: "V"
---

Initialize NAND flash support

### Prototype

```c
UINT lx_nand_flash_initialize(void);
```

### Description

This service initializes LevelX NAND flash support. It must be called before any other LevelX NAND APIs.

### Input Parameters

- **None**

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error initializing NAND flash support.

### Allowed From

Initialization, Threads

### Example

```c
/* Initialize NAND flash support. */
status = lx_nand_flash_initialize();  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
