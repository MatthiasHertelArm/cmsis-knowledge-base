---
id: "txmw-chapter-3-levelx-nand-support-driver-block-status-get"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Block Status Get"
summary: "The LevelX NAND driver \"block status get\" service is responsible for retrieving the bad block flag of the specified block of the NAND flash. If it is successful, the LevelX NAND driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-block-status-get"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "block status get" service is responsible for retrieving the bad block flag of the specified block of the NAND flash. If it is successful, the LevelX NAND driver returns **LX_SUCCESS**. If it is not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "block status get" service is: shown below.

```c
INT nand_driver_block_status_get(
    LX_NAND_FLASH *nand_flash,
    ULONG block,  
    UCHAR *bad_block_byte);
```

Where *block* specifies which block and *bad_block_byte* specifies the destination for the bad block flag. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.
