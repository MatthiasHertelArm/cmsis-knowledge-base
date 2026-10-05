---
id: "rtx-event-functions-evrrtxsemaphorenotacquired"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreNotAcquired"
summary: "The event SemaphoreNotAcquired is generated when the function osMutexAcquire returns without timeout and semaphore token was not acquired."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreNotAcquired (osSemaphoreId_t semaphore_id)
```


The event **SemaphoreNotAcquired** is generated when the function osMutexAcquire returns without timeout and semaphore token was not acquired.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
