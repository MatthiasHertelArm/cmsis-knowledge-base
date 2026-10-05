---
id: "txmw-chapter-3-levelx-nand-support-driver-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver Initialization"
summary: "These services are setup via setting function pointers in the LX_NAND_FLASH instance within the driver's initialization function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-initialization"
license: "MIT"
mode: "V"
---

These services are setup via setting function pointers in the **LX_NAND_FLASH** instance within the driver's initialization function. The driver initialization function also specifies the total number of block, pages per block, bytes per page, spare data offsets and lengths and total spare byte length. There are two spare data stored in each page, spare data 1 and spare data 2. The spare data 1 is used to store data type as described above and must be at least 4 bytes and ECC protected. The spare data 2 is optional and may be used to indicate the start of metadata blocks. The driver initialization function likely also performs additional device and/or implementation-specific initialization duties before returning **LX_SUCCESS**.
