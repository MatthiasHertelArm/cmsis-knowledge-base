---
id: "drv-flash-interface-arm-flash-status"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_FLASH_STATUS"
summary: "Structure with information about the status of the Flash."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FLASH_STATUS
```


Structure with information about the status of the Flash.

The flag **busy** indicates that the driver is busy executing read/program/erase operation.

The flag **error** flag is cleared on start of read/program/erase operation and is set at the end of the current operation in case of error.

**Returned by:**
  - ARM_Flash_GetStatus
****************************************************************************************************************
