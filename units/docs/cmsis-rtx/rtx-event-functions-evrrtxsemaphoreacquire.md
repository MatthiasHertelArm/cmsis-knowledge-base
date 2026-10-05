---
id: "rtx-event-functions-evrrtxsemaphoreacquire"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreAcquire"
summary: "The event SemaphoreAcquire is generated when the function osSemaphoreAcquire is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreAcquire (osSemaphoreId_t semaphore_id, uint32_t timeout)
```


The event **SemaphoreAcquire** is generated when the function osSemaphoreAcquire is called.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
