---
id: "drv-flash-interface-arm-flash-erasesector"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_EraseSector"
summary: "This function ARM_Flash_EraseSector erases a flash sector specified by the parameter adr (points to start of the sector)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_EraseSector (uint32_t addr)
```

  
This function **ARM_Flash_EraseSector** erases a flash sector specified by the parameter _adr_ (points to start of the sector).

The function is non-blocking and returns as soon as the driver has started the operation.
When the operation is completed the ARM_FLASH_EVENT_READY event is generated (if supported and reported by ARM_Flash_GetCapabilities).
In case of errors the ARM_FLASH_EVENT_ERROR event is generated at the same time.
Progress of the operation can also be monitored by calling the ARM_Flash_GetStatus function and checking the **busy** flag.
******************************************************************************************************************
