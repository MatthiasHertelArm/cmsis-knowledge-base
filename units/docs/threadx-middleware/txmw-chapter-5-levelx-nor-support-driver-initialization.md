---
id: "txmw-chapter-5-levelx-nor-support-driver-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver Initialization"
summary: "These services are setup via setting function pointers in the LX_NOR_FLASH instance within the driver's initialization function. The driver initialization function also is responsible for:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-initialization"
license: "MIT"
mode: "V"
---

These services are setup via setting function pointers in the **LX_NOR_FLASH** instance within the driver's initialization function. The driver initialization function also is responsible for:

1. Specifying the base address of the flash.
1. Specifying the total number of blocks and the number of words per block.
1. A RAM buffer for reading one sector of flash (512 bytes) and aligned for ULONG access.

The driver initialization function likely also performs additional device and/or implementation-specific initialization duties before returning **LX_SUCCESS**.
