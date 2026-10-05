---
id: "txmw-chapter-3-levelx-nand-support-nand-driver-requirements"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: NAND Driver Requirements"
summary: "LevelX requires an underlying NAND flash driver that is specific to the underlying flash part and hardware implementation. The driver is specified to LevelX during initialization via the API lx_nand_flash_open and lx_nand_flash_format."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#nand-driver-requirements"
license: "MIT"
mode: "V"
---

LevelX requires an underlying NAND flash driver that is specific to the underlying flash part and hardware implementation. The driver is specified to LevelX during initialization via the API ***lx_nand_flash_open*** and ***lx_nand_flash_format***. If **LX_NAND_ENABLE_CONTROL_BLOCK_FOR_DRIVER_INTERFACE** is defined, the driver services functions will have pointer to the NAND control block as the first parameter. The driver may access the user extensions in the control block for driver specific data. The prototype of the LevelX driver is as follows.

```c
INT nand_driver_initialize(LX_NAND_FLASH *instance);
```

The *instance* parameter specifies the LevelX NAND control block. The driver initialization function is responsible for setting up all the other driver-level services for the associated LevelX instance. The services required for each LevelX NAND instance are shown in the list below.

- Read Pages
- Write Pages
- Copy Pages
- Block Erase
- Block Erased Verify
- Page Erased Verify
- Block Status Get
- Block Status Set
- System Error Handler
