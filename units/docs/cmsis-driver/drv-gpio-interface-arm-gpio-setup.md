---
id: "drv-gpio-interface-arm-gpio-setup"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_Setup"
summary: "The function ARMGPIOSetup sets-up the specified pin as GPIO with default configuration. Pin is configured as input without pull-resistor and without event trigger."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_GPIO_Setup (ARM_GPIO_Pin_t pin, ARM_GPIO_SignalEvent_t cb_event)
```


The function **ARM_GPIO_Setup** sets-up the specified **pin** as GPIO with default configuration.
Pin is configured as input without pull-resistor and without event trigger.

The parameter **cb_event** specifies a pointer to the ARM_GPIO_SignalEvent callback function to register. 
Use a NULL pointer when no callback events are required or to deregister a callback function.
*************************************************************************************************************************
