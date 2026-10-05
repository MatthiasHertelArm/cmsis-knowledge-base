---
id: "rtx-event-functions-evrrtxthreadpreempted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadPreempted"
summary: "The event ThreadPreempted is generated when current running thread execution is preempted."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadPreempted (osThreadId_t thread_id)
```


The event **ThreadPreempted** is generated when current running thread execution is preempted.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
