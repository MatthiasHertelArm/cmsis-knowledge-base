---
id: "rtx-event-functions-evrrtxtimerstart"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerStart"
summary: "The event TimerStart is generated when the function osTimerStart is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerStart (osTimerId_t timer_id, uint32_t ticks)
```


The event **TimerStart** is generated when the function osTimerStart is called.

**Value** in the Event Recorder shows:
  - **timer_id** : timer ID.
  - **ticks** : time ticks value of the timer.
