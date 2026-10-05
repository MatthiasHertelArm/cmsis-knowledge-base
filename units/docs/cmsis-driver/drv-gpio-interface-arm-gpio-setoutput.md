---
id: "drv-gpio-interface-arm-gpio-setoutput"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SetOutput"
summary: "The function ARMGPIOSetOutput sets the level of the specified pin defined as output to the value specified by val."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_GPIO_SetOutput (ARM_GPIO_Pin_t pin, uint32_t val)
```


The function **ARM_GPIO_SetOutput** sets the level of the specified **pin** defined as output to the value specified by **val.**

**Note:**
When a pin is configured as input, the level is latched and will be driven once the pin is configured as output.
*************************************************************************************************************************
