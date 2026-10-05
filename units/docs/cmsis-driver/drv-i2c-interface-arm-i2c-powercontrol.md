---
id: "drv-i2c-interface-arm-i2c-powercontrol"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_PowerControl"
summary: "The function ARMI2CPowerControl operates the power modes of the I2C interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_I2C_PowerControl** operates the power modes of the I2C interface.

The parameter **state** can have the following values:
  - ARM_POWER_FULL : set-up peripheral for data transfers, enable interrupts (NVIC) and optionally DMA. 
                          Can be called multiple times. If the peripheral is already in this mode, 
						  then the function performs no operation and returns with ARM_DRIVER_OK.
  - ARM_POWER_LOW : may use power saving. Returns ARM_DRIVER_ERROR_UNSUPPORTED when not implemented.
  - ARM_POWER_OFF : terminates any pending data transfers, disables peripheral, disables related interrupts and DMA.
      
Refer to CallSequence for more information.

\sa ARM_I2C_Initialize
\sa ARM_I2C_Uninitialize

******************************************************************************************************************
