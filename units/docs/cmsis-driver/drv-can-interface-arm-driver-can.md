---
id: "drv-can-interface-arm-driver-can"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_DRIVER_CAN"
summary: "The functions of the CAN are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_DRIVER_CAN
```


The functions of the CAN are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information.

Each instance of a CAN provides such an access structure.
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_CAN0** is the name of the access struct of the first instance (no. 0).
 - **Driver_CAN1** is the name of the access struct of the second instance (no. 1).

A configuration setting in the middleware allows you to connect the middleware to a specific driver instance **Driver_CAN_n_**.
******************************************************************************************************************
