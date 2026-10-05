---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-defragment"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_defragment"
summary: "This service defragments the previously opened NOR flash instance. The defragment process maximizes the number of free sectors and blocks."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-defragment"
license: "MIT"
mode: "V"
---

Defragment NOR flash instance

### Prototype

```c
UINT lx_nor_flash_defragment(LX_NOR_FLASH *nor_flash);
```

### Description

This service defragments the previously opened NOR flash instance. The defragment process maximizes the number of free sectors and blocks.

### Input Parameters

- *nor_flash*: NOR flash instance pointer.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error defragmenting flash instance.

### Allowed From

Threads

### Example

```c
/* Defragment NOR flash instance "my_nor_flash". */  
status = lx_nor_flash_defragment(&my_nor_flash);  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
