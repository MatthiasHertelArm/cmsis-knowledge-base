---
id: "drv-status-error-codes"
type: "concept"
domain: "drivers"
title: "Status Error Codes"
summary: "Negative return values of functions indicate errors occurred during execution."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_Common.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_Common.c"
license: "Apache-2.0"
mode: "V"
---

Negative return values of functions indicate errors occurred during execution. 
 
Most functions return a status information using negative return values.
The following list provides the status error codes that are common in all drivers.
The drivers may return also status error codes that are specific to the peripheral.
\sa
spi_execution_status for SPI driver;
usart_execution_status for USART driver;
nand_execution_status for NAND driver;

### ARM_DRIVER_OK

```c
ARM_DRIVER_OK
```

The value 0 or positive values indicate that the function execution is completed without any errors.
Note that positive values are used to provide for example the number of data items.


### ARM_DRIVER_ERROR

```c
ARM_DRIVER_ERROR
```

The function did not execute correct and an unspecified error occurred during execution.


### ARM_DRIVER_ERROR_BUSY

```c
ARM_DRIVER_ERROR_BUSY
```

The function cannot be executed because the driver is busy with the execution of a conflicting operation.


### ARM_DRIVER_ERROR_TIMEOUT

```c
ARM_DRIVER_ERROR_TIMEOUT
```

The function execution is terminated because a peripheral did not react within a specific timeout limit.


### ARM_DRIVER_ERROR_UNSUPPORTED

```c
ARM_DRIVER_ERROR_UNSUPPORTED
```

The function requested an operation (for example by using an illegal control code) that is not supported.


### ARM_DRIVER_ERROR_PARAMETER

```c
ARM_DRIVER_ERROR_PARAMETER
```

A function parameter is incorrect.


### ARM_DRIVER_ERROR_SPECIFIC

```c
ARM_DRIVER_ERROR_SPECIFIC
```

This value indicates the start of status error codes that are specific to the peripheral driver.
\sa
spi_execution_status for SPI driver;
usart_execution_status for USART driver;
