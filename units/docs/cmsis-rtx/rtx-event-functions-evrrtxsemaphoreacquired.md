---
id: "rtx-event-functions-evrrtxsemaphoreacquired"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreAcquired"
summary: "The event SemaphoreAcquired is generated when the function osSemaphoreAcquire successfully acquires the semaphore token."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreAcquired (osSemaphoreId_t semaphore_id, uint32_t tokens)
```


The event **SemaphoreAcquired** is generated when the function osSemaphoreAcquire successfully acquires the semaphore token.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **tokens** : available tokens.
