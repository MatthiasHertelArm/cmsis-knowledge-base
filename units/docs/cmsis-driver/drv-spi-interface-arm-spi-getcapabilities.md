---
id: "drv-spi-interface-arm-spi-getcapabilities"
type: "concept"
domain: "drivers"
title: "SPI Interface: ARM_SPI_GetCapabilities"
summary: "The function ARM_SPI_GetCapabilities returns information about the capabilities in this driver implementation. The data fields of the structure ARM_SPI_CAPABILITIES encode various capabilities, for example supported modes."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_SPI_CAPABILITIES ARM_SPI_GetCapabilities (void)
```


The function **ARM_SPI_GetCapabilities** returns information about the capabilities in this driver implementation.
The data fields of the structure ARM_SPI_CAPABILITIES encode various capabilities, for example
supported modes.
 
Example:
```
extern ARM_DRIVER_SPI Driver_SPI0;
ARM_DRIVER_SPI *drv_info;
  
void read_capabilities (void)  {
  ARM_SPI_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_SPI0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```

*************************************************************************************************************************
