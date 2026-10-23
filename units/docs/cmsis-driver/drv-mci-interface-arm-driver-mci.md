---
id: "drv-mci-interface-arm-driver-mci"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_DRIVER_MCI"
summary: "The functions of the MCI are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_MCI
```

 
The functions of the MCI are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information.

Each instance of an MCI provides such an access structure. 
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_MCI0** is the name of the access struct of the first instance (no. 0).
 - **Driver_MCI1** is the name of the access struct of the second instance (no. 1).

A configuration setting in the middleware allows connecting the middleware to a specific driver instance **Driver_MCI_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.
******************************************************************************************************************
