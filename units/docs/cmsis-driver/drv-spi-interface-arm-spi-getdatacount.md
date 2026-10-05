---
id: "drv-spi-interface-arm-spi-getdatacount"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_GetDataCount"
summary: "The function ARMSPIGetDataCount returns the number of currently transferred data items during ARMSPISend, ARMSPIReceive and ARMSPITransfer operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_SPI_GetDataCount (void)
```


The function **ARM_SPI_GetDataCount** returns the number of currently transferred data items 
during ARM_SPI_Send, ARM_SPI_Receive and ARM_SPI_Transfer operation.
****************************************************************************************************************
