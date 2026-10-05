---
id: "rtx-event-functions-evrrtxthreaddestroyed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadDestroyed"
summary: "The event ThreadDestroyed is generated when the function osThreadExit or osThreadTerminate successfully terminates the thread."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadDestroyed (osThreadId_t thread_id)
```


The event **ThreadDestroyed** is generated when the function osThreadExit or osThreadTerminate successfully terminates the thread.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
