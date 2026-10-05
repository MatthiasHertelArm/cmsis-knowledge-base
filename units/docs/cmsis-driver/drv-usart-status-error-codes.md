---
id: "drv-usart-status-error-codes"
type: "concept"
domain: "drivers"
title: "USART Status Error Codes"
summary: "Negative values indicate errors (USART has specific codes in addition to common executionstatus)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

Negative values indicate errors (USART has specific codes in addition to common execution_status). 
 
The USART driver has additional status error codes that are listed below.
Note that the USART driver also returns the common execution_status. 
  

### ARM_USART_ERROR_MODE

```c
ARM_USART_ERROR_MODE
```

The **mode** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_BAUDRATE

```c
ARM_USART_ERROR_BAUDRATE
```

The **baud rate** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_DATA_BITS

```c
ARM_USART_ERROR_DATA_BITS
```

The number of **data bits** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_PARITY

```c
ARM_USART_ERROR_PARITY
```

The **parity bit** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_STOP_BITS

```c
ARM_USART_ERROR_STOP_BITS
```

The **stop bit** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_FLOW_CONTROL

```c
ARM_USART_ERROR_FLOW_CONTROL
```

The **flow control** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_CPOL

```c
ARM_USART_ERROR_CPOL
```

The **clock polarity** requested with the function ARM_USART_Control is not supported by this driver.


### ARM_USART_ERROR_CPHA

```c
ARM_USART_ERROR_CPHA
```

The **clock phase** requested with the function ARM_USART_Control is not supported by this driver.
