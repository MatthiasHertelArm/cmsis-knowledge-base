---
id: "rtx-event-functions-evrrtxthreadgetstate"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetState"
summary: "The event ThreadGetState is generated when the function osThreadGetState is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetState (osThreadId_t thread_id, osThreadState_t state)
```


The event **ThreadGetState** is generated when the function osThreadGetState is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **state** : retrieved current thread state.
