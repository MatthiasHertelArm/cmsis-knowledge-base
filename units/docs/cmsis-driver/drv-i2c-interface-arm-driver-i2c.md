---
id: "drv-i2c-interface-arm-driver-i2c"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_DRIVER_I2C"
summary: "The functions of the I2C interface are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_I2C
```


The functions of the I2C interface are accessed by function pointers exposed by this structure. Refer to DriverFunctions for 
overview information.

Each instance of an I2C provides such an access structure. The instance is indicated by
a postfix in the symbol name of the access structure, for example:
 - **Driver_I2C0** is the name of the access struct of the first instance (no. 0).
 - **Driver_I2C1** is the name of the access struct of the second instance (no. 1).


A configuration setting in the middleware allows connecting the middleware to a specific driver instance **%Driver_I2C_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.
******************************************************************************************************************
