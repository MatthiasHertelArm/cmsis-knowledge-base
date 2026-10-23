---
id: "drv-flash-interface-arm-flash-powercontrol"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_PowerControl"
summary: "The function ARM_Flash_PowerControl operates the power modes of the Flash interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_Flash_PowerControl** operates the power modes of the Flash interface.

The parameter **state** can have the following values:
  - ARM_POWER_FULL : set-up peripheral for data transfers, enable interrupts (NVIC) and optionally DMA. Can be called multiple times. 
                          If the peripheral is already in this mode, then the function performs no operation and returns with ARM_DRIVER_OK.
  - ARM_POWER_LOW : may use power saving. Returns ARM_DRIVER_ERROR_UNSUPPORTED when not implemented.
  - ARM_POWER_OFF : terminates any pending data transfers, disables peripheral, disables related interrupts and DMA.
      
Refer to CallSequence for more information.
******************************************************************************************************************
