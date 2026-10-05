---
id: "rtx-event-functions-evrrtxtimerstopped"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerStopped"
summary: "The event TimerStopped is generated when the function osTimerStop successfully stops the timer operation."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerStopped (osTimerId_t timer_id)
```


The event **TimerStopped** is generated when the function osTimerStop successfully stops the timer operation.

**Value** in the Event Recorder shows:
  - **timer_id** : timer ID.
