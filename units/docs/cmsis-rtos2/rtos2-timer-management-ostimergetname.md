---
id: "rtos2-timer-management-ostimergetname"
type: "concept"
domain: "rtos"
title: "Timer Management: osTimerGetName"
summary: "The function osTimerGetName returns the pointer to the name string of the timer identified by parameter timerid or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osTimerGetName (osTimerId_t timer_id)
```


The function **osTimerGetName** returns the pointer to the name string of the timer identified by parameter _timer_id_ or
`NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
