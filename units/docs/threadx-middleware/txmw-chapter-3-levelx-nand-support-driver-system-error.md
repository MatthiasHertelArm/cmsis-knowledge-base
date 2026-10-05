---
id: "txmw-chapter-3-levelx-nand-support-driver-system-error"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: Driver System Error"
summary: "The LevelX NAND driver \"system error handler\" service is responsible for setting handling system errors detected by LevelX. The processing in this routine is application dependent. If it is successful, the LevelX NAND driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#driver-system-error"
license: "MIT"
mode: "V"
---

The LevelX NAND driver "system error handler" service is responsible for setting handling system errors detected by LevelX. The processing in this routine is application dependent. If it is successful, the LevelX NAND driver returns **LX_SUCCESS**. If it is not successful, the LevelX NAND driver returns **LX_ERROR**. The prototype of the LevelX NAND driver "system error" service is:

```c
INT nand_driver_system_error(
    LX_NAND_FLASH *nand_flash,
    UINT error_code,  
    ULONG block, 
    ULONG page);
```

Where *block* specifies which block, and *page* specifies the specific page the error represented by *error_code* occurred. The *nand_flash* parameter is provided for driver to access the NAND control block if needed.
