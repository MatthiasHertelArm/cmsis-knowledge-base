---
id: "txmw-chapter-3-levelx-nand-support-driver-read-pages"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Read Pages"
summary: "The LevelX NAND driver \"read pages\" service is responsible for reading one or more pages in a specific block of the NAND flash. All error checking and correcting logic is the responsibility of the driver service."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-read-pages"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "read pages" service is responsible for reading one or more pages in a specific block of the NAND flash. All error checking and correcting logic is the responsibility of the driver service. If successful, the LevelX NAND driver returns **LX_SUCCESS**. If not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "read pages" service is given below.

```c
INT nand_driver_read_pages(
    LX_NAND_FLASH *nand_flash,
    ULONG block,
    ULONG page,
    UCHAR* main_buffer,
    UCHAR* spare_buffer,
    ULONG pages);
```

Where *block* and *page* identify the first page to read and *main_buffer* and *spare_buffer* specify where to place the page contents and spare data. And *pages* specify how many pages to read. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.
