---
id: "drv-spi-interface-arm-spi-initialize"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_Initialize"
summary: "The function ARMSPIInitialize initializes the SPI interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_SPI_Initialize (ARM_SPI_SignalEvent_t cb_event)
```


The function **ARM_SPI_Initialize** initializes the SPI interface. 

The parameter **cb_event** is a pointer to the ARM_SPI_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

The function is called when the middleware component starts operation and performs the following:
  - Initializes the resources needed for the SPI interface.
  - Registers the ARM_SPI_SignalEvent callback function.


**Example:**
 - see spi_interface_gr - Driver Functions

*************************************************************************************************************************
