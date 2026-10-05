---
id: "drv-nand-interface-arm-nand-powercontrol"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_PowerControl"
summary: "The function ARMNANDPowerControl controls the power modes of the NAND interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_NAND_PowerControl** controls the power modes of the NAND interface.  

The parameter **state** sets the operation and can have the following values:
  - ARM_POWER_FULL : set-up peripheral for data transfers, enable interrupts (NVIC) and optionally DMA. 
                          Can be called multiple times. If the peripheral is already in this mode the function performs 
						  no operation and returns with ARM_DRIVER_OK.
  - ARM_POWER_LOW : may use power saving. Returns ARM_DRIVER_ERROR_UNSUPPORTED when not implemented.
  - ARM_POWER_OFF : terminates any pending data transfers, disables peripheral, disables related interrupts and DMA.
      
Refer to CallSequence for more information.
******************************************************************************************************************
