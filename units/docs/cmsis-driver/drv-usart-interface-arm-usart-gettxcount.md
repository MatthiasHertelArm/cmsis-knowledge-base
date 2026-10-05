---
id: "drv-usart-interface-arm-usart-gettxcount"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_GetTxCount"
summary: "The function ARMUSARTGetTxCount returns the number of the currently transmitted data items during ARMUSARTSend and ARMUSARTTransfer operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_USART_GetTxCount (void)
```


The function **ARM_USART_GetTxCount** returns the number of the currently transmitted data items during ARM_USART_Send and ARM_USART_Transfer operation.
****************************************************************************************************************
