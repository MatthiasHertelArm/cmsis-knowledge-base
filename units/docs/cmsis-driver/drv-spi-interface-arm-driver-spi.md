---
id: "drv-spi-interface-arm-driver-spi"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_DRIVER_SPI"
summary: "The functions of the SPI driver are accessed by function pointers exposed by this structure. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_SPI
```

 
The functions of the SPI driver are accessed by function pointers exposed by this structure.
Refer to DriverFunctions for overview information.

Each instance of a SPI interface provides such an access structure. 
The instance is identified by a postfix number in the symbol name of the access structure, for example:
 - **Driver_SPI0** is the name of the access struct of the first instance (no. 0).
 - **Driver_SPI1** is the name of the access struct of the second instance (no. 1).

A middleware configuration setting allows connecting the middleware to a specific driver instance **%Driver_SPI_n_.**
The default is `0`, which connects a middleware to the first instance of a driver.
*************************************************************************************************************************
