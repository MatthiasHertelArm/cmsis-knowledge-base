---
id: "drv-spi-interface-arm-spi-uninitialize"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_Uninitialize"
summary: "The function ARM_SPI_Uninitialize de-initializes the resources of SPI interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_SPI_Uninitialize (void)
```


The function **ARM_SPI_Uninitialize** de-initializes the resources of SPI interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
*************************************************************************************************************************
