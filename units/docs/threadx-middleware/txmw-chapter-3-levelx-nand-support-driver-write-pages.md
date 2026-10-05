---
id: "txmw-chapter-3-levelx-nand-support-driver-write-pages"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Write Pages"
summary: "The LevelX NAND driver \"write pages\" service is responsible for writing one or more pages into the specified block of the NAND flash. All error checking and ECC computation is the responsibility of the driver service."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-write-pages"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "write pages" service is responsible for writing one or more pages into the specified block of the NAND flash. All error checking and ECC computation is the responsibility of the driver service. If successful, the LevelX NAND driver returns **LX_SUCCESS**. If not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "write pages" service is shown below.

```c
INT nand_driver_write_pages(
    LX_NAND_FLASH *nand_flash,
    ULONG block, 
    ULONG page,
    UCHAR* main_buffer,
    UCHAR* spare_buffer,
    ULONG pages);
```

Where *block* and *page* identify the first page to write and *main_buffer* and *spare_buffer* specify the source of the page contents and spare data. And *pages* specify how many pages to write. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.

> **Note:** LevelX relies on the driver for low-level error detection when writing to the flash page, which typically involves reading back the page and comparing with the write buffer to ensure the write was successful.
