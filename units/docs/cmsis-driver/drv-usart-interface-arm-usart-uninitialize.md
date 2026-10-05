---
id: "drv-usart-interface-arm-usart-uninitialize"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_Uninitialize"
summary: "The function ARM_USART_Uninitialize de-initializes the resources of USART interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_Uninitialize (void)
```


The function **ARM_USART_Uninitialize** de-initializes the resources of USART interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
****************************************************************************************************************
