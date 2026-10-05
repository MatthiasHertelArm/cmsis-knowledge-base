---
id: "rtx-event-functions-evrrtxthreadsuspended"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadSuspended"
summary: "The event ThreadSuspended is generated when the function osThreadSuspend successfully suspends the specified thread."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadSuspended (osThreadId_t thread_id)
```


The event **ThreadSuspended** is generated when the function osThreadSuspend successfully suspends the specified thread.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
