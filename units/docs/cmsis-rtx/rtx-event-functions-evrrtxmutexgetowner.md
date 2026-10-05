---
id: "rtx-event-functions-evrrtxmutexgetowner"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexGetOwner"
summary: "The event MutexGetOwner is generated when the function osMutexGetOwner is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexGetOwner (osMutexId_t mutex_id, osThreadId_t thread_id)
```


The event **MutexGetOwner** is generated when the function osMutexGetOwner is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
  - **thread_id** : retrieved owner thread ID (0 in case of a failure or when mutex is not locked)
