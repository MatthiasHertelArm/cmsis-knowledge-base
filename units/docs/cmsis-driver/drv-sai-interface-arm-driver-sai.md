---
id: "drv-sai-interface-arm-driver-sai"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_DRIVER_SAI"
summary: "The functions of the SAI driver are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
ARM_DRIVER_SAI
```


The functions of the SAI driver are accessed by function pointers exposed by this structure.
Refer to DriverFunctions for overview information.

Each instance of an SAI interface provides such an access structure. 
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_SAI0** is the name of the access struct of the first instance (no. 0).
 - **Driver_SAI1** is the name of the access struct of the second instance (no. 1).

A middleware configuration setting allows connecting the middleware to a specific driver instance **%Driver_SAI_n_.**
The default is `0`, which connects a middleware to the first instance of a driver.
****************************************************************************************************************
