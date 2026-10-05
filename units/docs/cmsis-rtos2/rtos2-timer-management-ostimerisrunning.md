---
id: "rtos2-timer-management-ostimerisrunning"
type: "concept"
domain: "rtos"
title: "Timer Management: osTimerIsRunning"
summary: "The function osTimerIsRunning checks whether a timer specified by parameter timer_id is running. It returns 1 if the timer is running and 0 if the timer is stopped or an error occurred."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osTimerIsRunning (osTimerId_t timer_id)
```


The function **osTimerIsRunning** checks whether a timer specified by parameter _timer_id_ is running. It returns `1`
if the timer is running and `0` if the timer is stopped or an error occurred.

**Note:** This function **cannot** be called from Interrupt Service Routines.
