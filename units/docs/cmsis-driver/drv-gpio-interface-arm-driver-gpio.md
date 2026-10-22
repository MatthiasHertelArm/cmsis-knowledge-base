---
id: "drv-gpio-interface-arm-driver-gpio"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_DRIVER_GPIO"
summary: "The functions of the GPIO driver are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_GPIO
```

 
The functions of the GPIO driver are accessed by function pointers exposed by this structure.
Refer to DriverFunctions for overview information.

Each instance of a GPIO interface provides such an access structure. 
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_GPIO0** is the name of the access struct of the first instance (no. 0).
 - **Driver_GPIO1** is the name of the access struct of the second instance (no. 1).

A middleware configuration setting allows connecting the middleware to a specific driver instance **%Driver_GPIO_n_.**
The default is `0`, which connects a middleware to the first instance of a driver.
*************************************************************************************************************************
