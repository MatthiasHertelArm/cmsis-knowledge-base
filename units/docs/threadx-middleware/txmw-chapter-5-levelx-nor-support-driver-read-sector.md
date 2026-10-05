---
id: "txmw-chapter-5-levelx-nor-support-driver-read-sector"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver Read Sector"
summary: "The LevelX NOR driver \"read sector\" service is responsible for reading a specific sector in a specific block of the NOR flash. All error checking and correcting logic is the responsibility of the driver service."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-read-sector"
license: "MIT"
mode: "V"
---

The LevelX NOR driver "read sector" service is responsible for reading a specific sector in a specific block of the NOR flash. All error checking and correcting logic is the responsibility of the driver service. If successful, the LevelX NOR driver returns **LX_SUCCESS**. If not successful, the LevelX NOR driver returns *LX_ERROR*. The prototype of the LevelX NOR driver "read sector" service is:

```c
INT nor_driver_read_sector(
    LX_NOR_FLASH *nor_flash,
    ULONG *flash_address,
    ULONG *destination, 
    ULONG words);
```

Where "*flash_address*" specifies the address of a logical sector within a NOR flash block of memory and "*destination*" and "*words*" specify where to place the sector contents and how many 32-bit words to read. The *nor_flash* parameter is provided for driver to access the NOR control block if needed.
