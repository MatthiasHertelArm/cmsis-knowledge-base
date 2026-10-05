---
id: "rtx-event-functions-evrrtxmutexnotacquired"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexNotAcquired"
summary: "The event MutexNotAcquired is generated when the function osMutexAcquire returns without timeout and mutex was not acquired."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexNotAcquired (osMutexId_t mutex_id)
```


The event **MutexNotAcquired** is generated when the function osMutexAcquire returns without timeout and mutex was not acquired.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
