---
id: "txmw-chapter-3-levelx-nand-support-driver-block-erase"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Block Erase"
summary: "The LevelX NAND driver \"block erase\" service is responsible for erasing the specified block of the NAND flash. If successful, the LevelX NAND driver returns LX_SUCCESS. If not successful, the LevelX NAND driver returns LX_ERROR."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-block-erase"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "block erase" service is responsible for erasing the specified block of the NAND flash. If successful, the LevelX NAND driver returns **LX_SUCCESS**. If not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "block erase" service is as follows.

```c
INT nand_driver_block_erase(
    LX_NAND_FLASH *nand_flash,
    ULONG block,  
    ULONG erase_count);
```

Where *block* identifies which block to erase. The parameter *erase_count* is provided for diagnostic purposes. For example, the driver may want to alert another portion of the application software when the erase count exceeds a specific threshold. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.

> **Note:** LevelX relies on the driver for low-level error detection when the block is erased, which typically involves ensuring that all pages of the block are all ones.
