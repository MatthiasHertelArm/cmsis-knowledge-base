---
id: "drv-gpio-interface-arm-gpio-setdirection"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SetDirection"
summary: "The function ARMGPIOSetDirection configures the direction of the specified pin."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_GPIO_SetDirection (ARM_GPIO_Pin_t pin, ARM_GPIO_DIRECTION direction)
```


The function **ARM_GPIO_SetDirection** configures the direction of the specified **pin.**

Direction is specified with parameter **direction:**
 - ARM_GPIO_INPUT : Input (default),
 - ARM_GPIO_OUTPUT : Output.
*************************************************************************************************************************
