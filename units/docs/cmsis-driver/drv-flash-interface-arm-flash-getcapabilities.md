---
id: "drv-flash-interface-arm-flash-getcapabilities"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_GetCapabilities"
summary: "The function ARMFlashGetCapabilities returns information about capabilities in this driver implementation. The data fields of the struct ARMFLASHCAPABILITIES encode various capabilities, for example if a hardware is able to create signal events using the ARMFlashSignalEvent callback function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_FLASH_CAPABILITIES ARM_Flash_GetCapabilities (void)
```


The function **ARM_Flash_GetCapabilities** returns information about capabilities in this driver implementation.
The data fields of the struct ARM_FLASH_CAPABILITIES encode various capabilities, for example
if a hardware is able to create signal events using the ARM_Flash_SignalEvent callback function.
 
Example:
```
extern ARM_DRIVER_FLASH Driver_Flash0;
ARM_DRIVER_FLASH *drv_info;
  
void read_capabilities (void)  {
  ARM_FLASH_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_Flash0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
******************************************************************************************************************
