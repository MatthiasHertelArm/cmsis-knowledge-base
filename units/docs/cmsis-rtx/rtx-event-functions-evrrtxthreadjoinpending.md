---
id: "rtx-event-functions-evrrtxthreadjoinpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadJoinPending"
summary: "The event ThreadJoinPending is generated when the function osThreadJoin suspends current running thread until the specified thread terminates."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadJoinPending (osThreadId_t thread_id)
```


The event **ThreadJoinPending** is generated when the function osThreadJoin suspends current running thread until the specified thread terminates.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
