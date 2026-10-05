---
id: "txmw-chapter-5-levelx-nor-support-driver-block-erased-verify"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver Block Erased Verify"
summary: "The LevelX NOR driver \"block erased verify\" service is responsible for verifying that the specified block of the NOR flash is erased. If it is erased, the LevelX NOR driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-block-erased-verify"
license: "MIT"
mode: "V"
---

The LevelX NOR driver "block erased verify" service is responsible for verifying that the specified block of the NOR flash is erased. If it is erased, the LevelX NOR driver returns **LX_SUCCESS**. If the block is not erased, the LevelX NOR driver returns **LX_ERROR**. The prototype of the LevelX NOR driver "block erased verify" service is:

```c
INT nor_driver_block_erased_verify(LX_NOR_FLASH *nor_flash, ULONG block);
```

Where "*block*" specifies which block to verify that it is erased. The *nor_flash* parameter is provided for driver to access the NOR control block if needed.

> **Note:** LevelX relies on the driver to examine all bytes of the specified to ensure they are erased (contain all ones).
