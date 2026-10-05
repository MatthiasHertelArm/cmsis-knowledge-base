---
id: "rtx-event-functions-evrrtxtimerisrunning"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxTimerIsRunning"
summary: "The event TimerIsRunning is generated when the function osTimerIsRunning is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxTimerIsRunning (osTimerId_t timer_id, uint32_t running)
```


The event **TimerIsRunning** is generated when the function osTimerIsRunning is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **timer_id** : timer ID.
  - **running** : timer running state: 0 not running, 1 running.
