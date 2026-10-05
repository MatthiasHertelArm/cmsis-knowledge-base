---
id: "drv-spi-status-error-codes"
type: "concept"
domain: "drivers"
title: "SPI Status Error Codes"
summary: "Negative values indicate errors (SPI has specific codes in addition to common executionstatus)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

Negative values indicate errors (SPI has specific codes in addition to common execution_status). 
 
The SPI driver has additional status error codes that are listed below.
Note that the SPI driver also returns the common execution_status. 
  

### ARM_SPI_ERROR_MODE

```c
ARM_SPI_ERROR_MODE
```

The **mode** requested with the function ARM_SPI_Control is not supported by this driver.


### ARM_SPI_ERROR_FRAME_FORMAT

```c
ARM_SPI_ERROR_FRAME_FORMAT
```

The **frame format** requested with the function ARM_SPI_Control is not supported by this driver.


### ARM_SPI_ERROR_DATA_BITS

```c
ARM_SPI_ERROR_DATA_BITS
```

The number of **data bits** requested with the function ARM_SPI_Control is not supported by this driver.


### ARM_SPI_ERROR_BIT_ORDER

```c
ARM_SPI_ERROR_BIT_ORDER
```

The **bit order** requested with the function ARM_SPI_Control is not supported by this driver.


### ARM_SPI_ERROR_SS_MODE

```c
ARM_SPI_ERROR_SS_MODE
```

The **slave select mode** requested with the function ARM_SPI_Control is not supported by this driver.
