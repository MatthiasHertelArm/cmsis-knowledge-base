---
id: "drv-flash-interface-arm-flash-programdata"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_ProgramData"
summary: "This function ARM_Flash_ProgramData programs data to the Flash device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_ProgramData (uint32_t addr, const void *data, uint32_t cnt)
```

  
This function **ARM_Flash_ProgramData** programs data to the Flash device.

The parameter **addr** specifies the address to where to program data (needs to be aligned to **program_unit** specified in ARM_FLASH_INFO). \n
The parameter **data** specifies the pointer to a buffer containing data to be programmed. 
The data type is **uint8_t,** **uint16_t** or **uint32_t** and is specified by the **data_width** in ARM_FLASH_CAPABILITIES. \n
The parameter **cnt** specifies the number of data items to program (data size needs to be a multiple of **program_unit).**

The function executes in the following ways:
 - When the operation is non-blocking (typically) then the function only starts the operation and returns with zero number of data items programmed. 
   When the operation is completed the ARM_FLASH_EVENT_READY event is generated (if supported and reported by ARM_Flash_GetCapabilities).
   In case of errors the ARM_FLASH_EVENT_ERROR event is generated at the same time.
   Progress of the operation can also be monitored by calling the ARM_Flash_GetStatus function and checking the **busy** flag.
 - When the operation is blocking then the function returns after the data is programmed and returns the number of data items programmed.
******************************************************************************************************************
