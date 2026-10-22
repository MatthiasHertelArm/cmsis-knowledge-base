---
id: "drv-flash-interface-arm-flash-erasechip"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_EraseChip"
summary: "The optional function ARM_Flash_EraseChip erases the complete device. If the device does not support global erase or only a portion of the Flash memory space is used for storing files, then the functions returns the error value ARM_DRIVER_ERROR_UNSUPPORTED."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_EraseChip (void)
```

  
The optional function **ARM_Flash_EraseChip** erases the complete device.
If the device does not support global erase or only a portion of the Flash memory space is used for storing files,
then the functions returns the error value ARM_DRIVER_ERROR_UNSUPPORTED.
The data field **eras_chip** = `1` of the structure ARM_FLASH_CAPABILITIES encodes that **ARM_Flash_EraseChip** is supported.
The field can be verified with the function ARM_Flash_GetCapabilities.

The function is non-blocking and returns as soon as the driver has started the operation.
When the operation is completed, the ARM_FLASH_EVENT_READY event is generated (if supported and reported by ARM_Flash_GetCapabilities).
In case of errors, the ARM_FLASH_EVENT_ERROR event is generated at the same time.
Progress of the operation can also be monitored by calling the ARM_Flash_GetStatus function and checking the **busy** flag.

**See also:**
 - ARM_Flash_SignalEvent
******************************************************************************************************************
