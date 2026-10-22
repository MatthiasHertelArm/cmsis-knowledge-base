---
id: "drv-gpio-interface-arm-gpio-seteventtrigger"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SetEventTrigger"
summary: "The function ARM_GPIO_SetEventTrigger configures the event trigger of the specified pin."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_GPIO_SetEventTrigger (ARM_GPIO_Pin_t pin, ARM_GPIO_EVENT_TRIGGER trigger)
```


The function **ARM_GPIO_SetEventTrigger** configures the event trigger of the specified **pin.**

Event trigger is specified with parameter **trigger:**
 - ARM_GPIO_TRIGGER_NONE : None (default),
 - ARM_GPIO_TRIGGER_RISING_EDGE : Rising-edge,
 - ARM_GPIO_TRIGGER_FALLING_EDGE : Falling-edge,
 - ARM_GPIO_TRIGGER_EITHER_EDGE : Either edge (rising and falling).

**Note:** To disable event trigger use trigger parameter ARM_GPIO_TRIGGER_NONE.
*************************************************************************************************************************
