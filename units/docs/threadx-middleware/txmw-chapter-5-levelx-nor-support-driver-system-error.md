---
id: "txmw-chapter-5-levelx-nor-support-driver-system-error"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support: Driver System Error"
summary: "The LevelX NOR driver \"system error handler\" service is responsible for setting handling system errors detected by LevelX. The processing in this routine is application dependent. If it is successful, the LevelX NOR driver returns LX_SUCCESS."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md#driver-system-error"
license: "MIT"
mode: "V"
---

The LevelX NOR driver "system error handler" service is responsible for setting handling system errors detected by LevelX. The processing in this routine is application dependent. If it is successful, the LevelX NOR driver returns **LX_SUCCESS**. If it is not successful, the LevelX NOR driver returns **LX_ERROR**. The prototype of the LevelX NOR driver "system error" service is:

```c
INT nor_driver_system_error(LX_NOR_FLASH *nor_flash, UINT error_code);
```

Where "*error_code*" represents the error that occurred. The *nor_flash* parameter is provided for driver to access the NOR control block if needed.
