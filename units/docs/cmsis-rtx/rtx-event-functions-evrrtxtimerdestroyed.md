---
id: "rtx-event-functions-evrrtxtimerdestroyed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerDestroyed"
summary: "The event TimerDestroyed is generated when the function osTimerDelete successfully deletes the timer object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerDestroyed (osTimerId_t timer_id)
```


The event **TimerDestroyed** is generated when the function osTimerDelete successfully deletes the timer object.

**Value** in the Event Recorder shows:
  - **timer_id** : timer ID.
