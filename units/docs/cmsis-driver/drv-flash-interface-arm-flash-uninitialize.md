---
id: "drv-flash-interface-arm-flash-uninitialize"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_Uninitialize"
summary: "The function ARM_Flash_Uninitialize de-initializes the resources of Flash interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_Uninitialize (void)
```


The function **ARM_Flash_Uninitialize** de-initializes the resources of Flash interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
******************************************************************************************************************
