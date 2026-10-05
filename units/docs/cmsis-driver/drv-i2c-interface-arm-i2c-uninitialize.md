---
id: "drv-i2c-interface-arm-i2c-uninitialize"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_Uninitialize"
summary: "The function ARM_I2C_Uninitialize releases the I/O resources of I2C interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_Uninitialize (void)
```


The function **ARM_I2C_Uninitialize** releases the I/O resources of I2C interface.

It is called when the middleware component stops operation and releases the I/O resources used by the I2C interface.
Refer to CallSequence for more information.

\sa ARM_I2C_Initialize
\sa ARM_I2C_PowerControl

******************************************************************************************************************
