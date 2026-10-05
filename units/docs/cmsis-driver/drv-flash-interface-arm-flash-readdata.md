---
id: "drv-flash-interface-arm-flash-readdata"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_ReadData"
summary: "This function ARMFlashReadData reads data from the Flash device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_ReadData (uint32_t addr, void *data, uint32_t cnt)
```

  
This function **ARM_Flash_ReadData** reads data from the Flash device.

The parameter **addr** specifies the address from where to read data (needs to be aligned to data type size). \n
The parameter **data** specifies the pointer to a buffer storing the data read. 
The data type is **uint8_t,** **uint16_t** or **uint32_t** and is specified by the **data_width** in ARM_FLASH_CAPABILITIES. \n
The parameter **cnt** specifies the number of data items to read.

The function executes in the following ways:
 - When the operation is non-blocking (typical for SPI Flash) then the function only starts the operation and returns with zero number of data items read. 
   When the operation is completed the ARM_FLASH_EVENT_READY event is generated (if supported and reported by ARM_Flash_GetCapabilities).
   In case of errors the ARM_FLASH_EVENT_ERROR event is generated at the same time.   
   Progress of the operation can also be monitored by calling the ARM_Flash_GetStatus function and checking the **busy** flag.
 - When the operation is blocking (typical for memory mapped Flash) then the function returns after the data is read and returns the number of data items read.
******************************************************************************************************************
