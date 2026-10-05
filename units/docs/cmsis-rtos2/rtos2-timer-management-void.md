---
id: "rtos2-timer-management-void"
type: "concept"
domain: "rtos"
title: "Timer Management: void"
summary: "The timer callback function is called every time the timer elapses."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void (*osTimerFunc_t) (void *argument)
```


The timer callback function is called every time the timer elapses.

The callback might be executed either in a dedicated timer thread or in interrupt context. Thus it is recommended to only
use ISR callable functions from the timer callback.

- `argument` (in): The argument provided to osTimerNew.
