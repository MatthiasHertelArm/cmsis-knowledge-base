---
id: "txmw-chapter-3-levelx-nand-support-driver-block-status-set"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Block Status Set"
summary: "The LevelX NAND driver \"block status set\" service is responsible for setting the bad block flag of the specified block of the NAND flash. If it is successful, the LevelX NAND driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-block-status-set"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "block status set" service is responsible for setting the bad block flag of the specified block of the NAND flash. If it is successful, the LevelX NAND driver returns **LX_SUCCESS**. If it is not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "block status set" service is:

```c
INT nand_driver_block_status_set(
    LX_NAND_FLASH *nand_flash,
    ULONG block,
    UCHAR bad_block_byte);
```

Where *block* specifies which block and *bad_block_byte* specifies the value of the bad block flag. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.
