---
id: "drv-usart-interface-arm-usart-getcapabilities"
type: "concept"
domain: "drivers"
title: "USART Interface: ARM_USART_GetCapabilities"
summary: "The function ARMUSARTGetCapabilities returns information about capabilities in this driver implementation. The data fields of the structure ARMUSARTCAPABILITIES encode various capabilities, for example: supported modes, if hardware and driver are capable of signaling events using the ARMUSARTSignalEvent callback function ..."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USART.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_USART_CAPABILITIES ARM_USART_GetCapabilities (void)
```


The function **ARM_USART_GetCapabilities** returns information about capabilities in this driver implementation.
The data fields of the structure ARM_USART_CAPABILITIES encode various capabilities, for example: 
supported modes, if hardware and driver are capable of signaling events using the ARM_USART_SignalEvent 
callback function ...
 
Example:
```
extern ARM_DRIVER_USART Driver_USART0;
ARM_DRIVER_USART *drv_info;
  
void read_capabilities (void)  {
  ARM_USART_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_USART0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
****************************************************************************************************************
