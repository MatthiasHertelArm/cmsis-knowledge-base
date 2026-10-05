---
id: "rtx-event-functions-evrrtxthreadresumed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadResumed"
summary: "The event ThreadResumed is generated when the function osThreadResume successfully resumes the specified thread."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadResumed (osThreadId_t thread_id)
```


The event **ThreadResumed** is generated when the function osThreadResume successfully resumes the specified thread.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
