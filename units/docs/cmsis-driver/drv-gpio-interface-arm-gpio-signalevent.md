---
id: "drv-gpio-interface-arm-gpio-signalevent"
type: "concept"
domain: "drivers"
title: "GPIO Interface: ARM_GPIO_SignalEvent"
summary: "The function ARM_GPIO_SignalEvent is a callback functions registered by the function ARM_GPIO_Setup. It is called by the GPIO driver to notify the application about GPIO_events occurred during operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_GPIO_SignalEvent (ARM_GPIO_Pin_t pin, uint32_t event)
```


The function **ARM_GPIO_SignalEvent** is a callback functions registered by the function ARM_GPIO_Setup. 
It is called by the GPIO driver to notify the application about GPIO_events occurred during operation.

The parameter **pin** indicates on which pin the event occurred and parameter **event** indicates one or more events that occurred.

The following events can be generated:



| Parameter **event** | Bit | Description |
|---|---|---|
| ARM_GPIO_EVENT_RISING_EDGE | 0 | Occurs when rising-edge is detected on the indicated pin. |
| ARM_GPIO_EVENT_FALLING_EDGE | 1 | Occurs when falling-edge is detected on the indicated pin. |
| ARM_GPIO_EVENT_EITHER_EDGE | 2 | Occurs when either edge is detected on the indicated pin when trigger is configured as ARM_GPIO_TRIGGER_EITHER_EDGE and hardware is not able to distinguish between rising and falling edge. |


*************************************************************************************************************************
