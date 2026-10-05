---
id: "rtx-event-functions-evrrtxtimernew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerNew"
summary: "The event TimerNew is generated when the function osTimerNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerNew (osTimerFunc_t func, osTimerType_t type, void *argument, const osTimerAttr_t *attr)
```


The event **TimerNew** is generated when the function osTimerNew is called.

**Value** in the Event Recorder shows:
  - **func** : start address of a timer call back function.
  - **type** : timer type: osTimerOnce for one-shot or osTimerPeriodic for periodic behavior.
  - **argument** : memory address of argument to the timer call back function.
  - **attr** : memory address of Timer attributes or 0 when they are not specified.
