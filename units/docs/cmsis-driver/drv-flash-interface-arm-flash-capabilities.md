---
id: "drv-flash-interface-arm-flash-capabilities"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_FLASH_CAPABILITIES"
summary: "A Flash driver can be implemented with different capabilities. The data fields of this struct encode the capabilities implemented by this driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FLASH_CAPABILITIES
```


A Flash driver can be implemented with different capabilities. The data fields of this struct encode 
the capabilities implemented by this driver.

The element **event_ready** indicates that the driver is able to generate the ARM_FLASH_EVENT_READY event. In case that this event is not available it is possible to poll the driver status by calling the ARM_Flash_GetStatus and check the **busy** flag.

The element **data_width** specifies the data access size and also defines the data type (uint8_t, uint16_t or uint32_t) for the **data** parameter in ARM_Flash_ReadData and ARM_Flash_ProgramData functions.

The element **erase_chip** specifies that the ARM_Flash_EraseChip function is supported. Typically full chip erase is much faster than erasing the whole device sector per sector.

**Returned by:**
  - ARM_Flash_GetCapabilities
******************************************************************************************************************
