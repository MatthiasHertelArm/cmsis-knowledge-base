---
id: "drv-usart-interface-arm-usart-getrxcount"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_GetRxCount"
summary: "The function ARMUSARTGetRxCount returns the number of the currently received data items during ARMUSARTReceive and ARMUSARTTransfer operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_USART_GetRxCount (void)
```


The function **ARM_USART_GetRxCount** returns the number of the currently received data items during ARM_USART_Receive and ARM_USART_Transfer operation.
****************************************************************************************************************
