---
id: "drv-usart-interface-arm-usart-setmodemcontrol"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_SetModemControl"
summary: "The function ARMUSARTSetModemControl activates or deactivates the selected USART modem control line."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USART_SetModemControl (ARM_USART_MODEM_CONTROL control)
```


The function **ARM_USART_SetModemControl** activates or deactivates the selected USART modem control line. 

The function ARM_USART_GetModemStatus returns information about status of the modem lines.

****************************************************************************************************************
