---
id: "txmw-chapter-3-levelx-nand-support-driver-block-erased-verify"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Block Erased Verify"
summary: "The LevelX NAND driver \"block erased verify\" service is responsible for verifying that the specified block of the NAND flash is erased. If it is erased, the LevelX NAND driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-block-erased-verify"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "block erased verify" service is responsible for verifying that the specified block of the NAND flash is erased. If it is erased, the LevelX NAND driver returns **LX_SUCCESS**. If the block is not erased, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "block erased verify" service is:

```c
INT nand_driver_block_erased_verify(
    LX_NAND_FLASH *nand_flash,
    ULONG block);
```

Where *block* specifies which block to verify that it is erased. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.

> **Note:** LevelX relies on the driver to examine all pages and all bytes of each page – including spare and data bytes – to ensure they are erased (contain all ones).
