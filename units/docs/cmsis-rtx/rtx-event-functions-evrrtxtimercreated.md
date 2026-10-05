---
id: "rtx-event-functions-evrrtxtimercreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerCreated"
summary: "The event TimerCreated is generated when the function osTimerNew successfully creates a timer object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerCreated (osTimerId_t timer_id, const char *name)
```


The event **TimerCreated** is generated when the function osTimerNew successfully creates a timer object.

**Value** in the Event Recorder shows:
  - **timer_id** : timer ID.
