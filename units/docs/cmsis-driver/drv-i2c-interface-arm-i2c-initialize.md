---
id: "drv-i2c-interface-arm-i2c-initialize"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_Initialize"
summary: "The function ARMI2CInitialize initializes the I2C interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_Initialize (ARM_I2C_SignalEvent_t cb_event)
```

 
The function **ARM_I2C_Initialize** initializes the I2C interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes and the I/O resources for the I2C interface.
  - Registers the ARM_I2C_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_I2C_SignalEvent callback function.
Use a NULL pointer when no callback events are required.

Can be called multiple times. If the peripheral is already initialized the function performs no operation and 
returns with ARM_DRIVER_OK. Refer to CallSequence for more information.

\sa ARM_I2C_PowerControl
\sa ARM_I2C_Uninitialize

**Example:**
 - refer to Example Code
 
******************************************************************************************************************
