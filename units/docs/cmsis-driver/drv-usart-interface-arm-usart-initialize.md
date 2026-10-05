---
id: "drv-usart-interface-arm-usart-initialize"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Initialize"
summary: "The function ARMUSARTInitialize initializes the USART interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Initialize (ARM_USART_SignalEvent_t cb_event)
```


The function **ARM_USART_Initialize** initializes the USART interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the USART interface.
  - Registers the ARM_USART_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_USART_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

**Example:**
 - see usart_interface_gr - Driver Functions

****************************************************************************************************************
