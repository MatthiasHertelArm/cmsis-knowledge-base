---
id: "rtx-event-functions-evrrtxtimercallback"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerCallback"
summary: "The event TimerCallback is generated when the timer callback function is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerCallback (osTimerFunc_t func, void *argument)
```


The event **TimerCallback** is generated when the timer callback function is called.

**Value** in the Event Recorder shows:
  - **func** : start address of a timer call back function. 
  - **argument** : memory address of argument to the timer call back function.
