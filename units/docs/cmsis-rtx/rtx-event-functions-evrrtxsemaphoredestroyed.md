---
id: "rtx-event-functions-evrrtxsemaphoredestroyed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreDestroyed"
summary: "The event SemaphoreDestroyed is generated when the function osSemaphoreDelete successfully deletes the semaphore object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreDestroyed (osSemaphoreId_t semaphore_id)
```


The event **SemaphoreDestroyed** is generated when the function osSemaphoreDelete successfully deletes the semaphore object.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
