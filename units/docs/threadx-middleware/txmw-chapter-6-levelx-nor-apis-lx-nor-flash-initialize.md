---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-initialize"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_initialize"
summary: "This service initializes LevelX NOR flash support. It must be called before any other LevelX NOR APIs."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-initialize"
license: "MIT"
mode: "V"
---

Initialize NOR flash support

### Prototype

```c
UINT lx_nor_flash_initialize(void);
```

### Description

This service initializes LevelX NOR flash support. It must be called before any other LevelX NOR APIs.

### Input Parameters

- **None**

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error initializing NOR flash support.

### Allowed From

Initialization, Threads

### Example

```c
/* Initialize NOR flash support. */  
status = lx_nor_flash_initialize();  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
