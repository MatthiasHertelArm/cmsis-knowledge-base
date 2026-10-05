---
id: "drv-gpio-interface-arm-gpio-setoutputmode"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SetOutputMode"
summary: "The function ARM_GPIO_SetOutputMode configures the output mode of the specified pin."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_GPIO_SetOutputMode (ARM_GPIO_Pin_t pin, ARM_GPIO_OUTPUT_MODE mode)
```


The function **ARM_GPIO_SetOutputMode** configures the output mode of the specified **pin.**

Output mode is specified with parameter **mode:**
 - ARM_GPIO_PUSH_PULL : Push-pull (default),
 - ARM_GPIO_OPEN_DRAIN : Open-drain.

**Note:** Output mode is relevant only when the pin is configured as output.
*************************************************************************************************************************
