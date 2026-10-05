---
id: "drv-theory-of-operation-shared-i-o-pins"
type: "concept"
domain: "drivers"
title: "Theory of Operation: Shared I/O Pins"
summary: "All CMSIS-Driver provide a CS_start and CS_stop. Therefore two different drivers can share the same I/O pins, for example UART1 and SPI1 can have overlapping I/O pins. In this case the communication channels can be used as shown below:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/operation.md#shared-i-o-pins"
license: "Apache-2.0"
mode: "V"
---

All CMSIS-Driver provide a CS_start and CS_stop. Therefore two different drivers can share the same I/O pins, for example UART1 and SPI1 can have overlapping I/O pins. In this case the communication channels can be used as shown below:

```c
  SPI1drv->Initialize (...);                // Start SPI1
  SPI1drv->PowerControl (ARM_POWER_FULL);
   ...                                      // Do operations with SPI1
  SPI1drv->PowerControl (ARM_POWER_OFF);    // Stop SPI1
  SPI1drv->Uninitialize ();
   ...
  USART1drv->Initialize (...);              // Start USART1
  USART1drv->PowerControl (ARM_POWER_FULL);
   ...                                      // Do operations with USART1
  USART1drv->PowerControl (ARM_POWER_OFF);  // Stop USART1
  USART1drv->Uninitialize ();
```
