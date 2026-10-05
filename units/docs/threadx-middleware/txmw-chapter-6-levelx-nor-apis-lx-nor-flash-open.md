---
id: "txmw-chapter-6-levelx-nor-apis-lx-nor-flash-open"
type: "concept"
domain: "rtos"
title: "Chapter 6 - LevelX NOR APIs: lx_nor_flash_open"
summary: "This service opens a NOR flash instance with the specified NOR flash control block and driver initialization function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter6.md#lx-nor-flash-open"
license: "MIT"
mode: "V"
---

Open NOR flash instance

### Prototype

```c
UINT lx_nor_flash_open(
    LX_NOR_FLASH *nor_flash, 
    CHAR *name,  
    UINT (*nor_driver_initialize) (LX_NOR_FLASH *));
```

### Description

This service opens a NOR flash instance with the specified NOR flash control block and driver initialization function. Note that the driver initialization function is responsible for installing various function pointers for reading, writing, and erasing blocks of the NOR hardware associated with this NOR flash instance.

### Input Parameters

- *nor_flash*: NOR flash instance pointer.
- *name*: Name of NOR flash instance.
- *nor_driver_initialize*: Function pointer to NOR flash driver Initialization function. Please refer to Chapter 5 of this guide for more details on NOR flash driver responsibilities.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error opening NOR flash instance.
- **LX_NO_MEMORY**:  (0x08) Driver did not provide buffer for reading none sector into RAM.

### Allowed From

Threads

### Example

```c
/* Open NOR flash instance "my_nor_flash" with the driver "my_nor_driver_initialize". */  
status = lx_nor_flash_open(&my_nor_flash,"my NOR flash",  
    my_nor_driver_initialize);  
  
/* If status is LX_SUCCESS the request was successful. */
```

### See Also

- [levelx NOR Services](#NOR_Services)
