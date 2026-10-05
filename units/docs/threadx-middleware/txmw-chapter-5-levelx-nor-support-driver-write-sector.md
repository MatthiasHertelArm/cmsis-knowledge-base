---
id: "txmw-chapter-5-levelx-nor-support-driver-write-sector"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver Write Sector"
summary: "The LevelX NOR driver \"write sector\" service is responsible for writing a specific sector into a block of the NOR flash. All error checking is the responsibility of the driver service. If successful, the LevelX NOR driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-write-sector"
license: "MIT"
mode: "V"
---

The LevelX NOR driver "write sector" service is responsible for writing a specific sector into a block of the NOR flash. All error checking is the responsibility of the driver service. If successful, the LevelX NOR driver returns **LX_SUCCESS**. If not successful, the LevelX NOR driver returns **LX_ERROR**. The prototype of the LevelX NOR driver "write sector" service is:

```c
INT nor_driver_write_sector(
    LX_NOR_FLASH *nor_flash,
    ULONG *flash_address,
    ULONG *source, 
    ULONG words);
```

Where "*flash_address*" specifies the address of a logical sector within a NOR flash block of memory and "*source*" and "*words*" specify the source of the write and how many 32-bit words to write. The *nor_flash* parameter is provided for driver to access the NOR control block if needed.

> **Note:** LevelX relies on the driver to verify that the write sector was successful. This is typically done by reading back the programmed value to ensure it matches the requested value to be written.
