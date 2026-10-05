---
id: "drv-gpio-events"
type: "concept"
domain: "drivers"
title: "GPIO Events"
summary: "The GPIO driver generates call back events that are notified via the function ARM_GPIO_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

The GPIO driver generates call back events that are notified via the function ARM_GPIO_SignalEvent.
 
This section provides the event values for the ARM_GPIO_SignalEvent callback function.

The following call back notification events are generated:

### ARM_GPIO_EVENT_RISING_EDGE

```c
ARM_GPIO_EVENT_RISING_EDGE
```


### ARM_GPIO_EVENT_FALLING_EDGE

```c
ARM_GPIO_EVENT_FALLING_EDGE
```


### ARM_GPIO_EVENT_EITHER_EDGE

```c
ARM_GPIO_EVENT_EITHER_EDGE
```
