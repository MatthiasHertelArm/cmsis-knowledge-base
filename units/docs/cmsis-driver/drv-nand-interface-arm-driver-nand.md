---
id: "drv-nand-interface-arm-driver-nand"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_DRIVER_NAND"
summary: "The functions of the NAND driver are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_NAND
```


The functions of the NAND driver are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information.

Each instance of a NAND interface provides such an access structure. 
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_NAND0** is the name of the access struct of the first instance (no. 0).
 - **Driver_NAND1** is the name of the access struct of the second instance (no. 1).

A middleware configuration setting allows connecting the middleware to a specific driver instance **Driver_NAND_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.
******************************************************************************************************************
