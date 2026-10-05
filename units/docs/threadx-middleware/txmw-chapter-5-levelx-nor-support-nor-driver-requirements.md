---
id: "txmw-chapter-5-levelx-nor-support-nor-driver-requirements"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: NOR Driver Requirements"
summary: "LevelX requires an underlying NOR flash driver that is specific to the underlying flash part and hardware implementation. The driver is specified to LevelX during initialization via the API lx_nor_flash_open."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#nor-driver-requirements"
license: "MIT"
mode: "V"
---

LevelX requires an underlying NOR flash driver that is specific to the underlying flash part and hardware implementation. The driver is specified to LevelX during initialization via the API ***lx_nor_flash_open***. If **LX_NOR_ENABLE_CONTROL_BLOCK_FOR_DRIVER_INTERFACE** is defined, the driver services functions will have pointer to the NOR control block as the first parameter. The driver may access the user extensions in the control block for driver specific data. The prototype of the LevelX driver is:

```c
INT nor_driver_initialize(LX_NOR_FLASH *instance);
```

The "*instance*" parameter specifies the LevelX NOR control block. The driver initialization function is responsible for setting up all the other driver-level services for the associated LevelX instance. The services required for each LevelX NOR instance are:

- Read Sector
- Write Sector
- Block Erase
- Block Erased Verify
- System Error Handler
