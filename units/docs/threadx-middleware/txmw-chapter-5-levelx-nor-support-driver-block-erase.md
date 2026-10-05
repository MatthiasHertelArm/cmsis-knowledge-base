---
id: "txmw-chapter-5-levelx-nor-support-driver-block-erase"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver Block Erase"
summary: "The LevelX NOR driver \"block erase\" service is responsible for erasing the specified block of the NOR flash. If successful, the LevelX NOR driver returns LX_SUCCESS. If not successful, the LevelX NOR driver returns LX_ERROR."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-block-erase"
license: "MIT"
mode: "V"
---

The LevelX NOR driver "block erase" service is responsible for erasing the specified block of the NOR flash. If successful, the LevelX NOR driver returns **LX_SUCCESS**. If not successful, the LevelX NOR driver returns **LX_ERROR**. The prototype of the LevelX NOR driver "block erase" service is:

```c
INT nor_driver_block_erase(
    LX_NOR_FLASH *nor_flash,
    ULONG block,  
    ULONG erase_count);
```

Where "*block*" identifies which NOR block to erase. The parameter "*erase_count*" is provided for diagnostic purposes. For example, the driver may want to alert another portion of the application software when the erase count exceeds a specific threshold. The *nor_flash* parameter is provided for driver to access the NOR control block if needed.

> **Note:** LevelX relies on the driver to examine all bytes of the block to ensure they are erased (contain all ones).
