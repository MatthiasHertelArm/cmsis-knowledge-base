---
id: "rtx-event-functions-evrrtxthreadgetpriority"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetPriority"
summary: "The event ThreadGetPriority is generated when the function osThreadGetPriority is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetPriority (osThreadId_t thread_id, osPriority_t priority)
```


The event **ThreadGetPriority** is generated when the function osThreadGetPriority is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **priority** : current priority value of the specified thread.
