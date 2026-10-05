---
id: "txmw-chapter-3-levelx-nand-support-driver-copy-pages"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Copy Pages"
summary: "The LevelX NAND driver \"copy pages\" service is responsible for copying one or more pages from one block of the NAND flash to another block of the NAND flash."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-copy-pages"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "copy pages" service is responsible for copying one or more pages from one block of the NAND flash to another block of the NAND flash. All error checking and ECC computation is the responsibility of the driver service. If successful, the LevelX NAND driver returns **LX_SUCCESS**. If not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "copy pages" service is shown below.

```c
INT nand_driver_copy_pages(
    LX_NAND_FLASH *nand_flash,
    ULONG source_block,  
    ULONG source_page,
    ULONG destination_block,
    ULONG destination_page,
    ULONG pages,
    UCHAR *data_buffer);   
```

Where *source_block* and *source_page* identify the first page to copy and *destination_block* and *destination_page* specifies the first destination block and page. And *pages* specify how many pages to copy. The parameter *data_buffer* is provided for driver to store one page and spare data for copy operation if the driver needs to read the source page before writing to the destination page.
