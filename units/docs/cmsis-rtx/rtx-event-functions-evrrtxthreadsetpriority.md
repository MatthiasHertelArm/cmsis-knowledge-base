---
id: "rtx-event-functions-evrrtxthreadsetpriority"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadSetPriority"
summary: "The event ThreadSetPriority is generated when the function osThreadSetPriority is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadSetPriority (osThreadId_t thread_id, osPriority_t priority)
```


The event **ThreadSetPriority** is generated when the function osThreadSetPriority is called.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **priority** : new priority value for the thread function.
