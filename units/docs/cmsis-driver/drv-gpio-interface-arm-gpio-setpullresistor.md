---
id: "drv-gpio-interface-arm-gpio-setpullresistor"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SetPullResistor"
summary: "The function ARM_GPIO_SetPullResistor configures the pull resistor of the specified pin."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_GPIO_SetPullResistor (ARM_GPIO_Pin_t pin, ARM_GPIO_PULL_RESISTOR resistor)
```


The function **ARM_GPIO_SetPullResistor** configures the pull resistor of the specified **pin.**

Pull resistor is specified with parameter **resistor:**
 - ARM_GPIO_PULL_NONE : None (default),
 - ARM_GPIO_PULL_UP : Pull-up,
 - ARM_GPIO_PULL_DOWN : Pull-down.

**Note:** Pull resistor applies to the pin regardless of pin direction.
*************************************************************************************************************************
