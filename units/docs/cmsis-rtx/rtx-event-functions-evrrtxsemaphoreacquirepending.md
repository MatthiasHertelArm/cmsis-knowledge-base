---
id: "rtx-event-functions-evrrtxsemaphoreacquirepending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreAcquirePending"
summary: "The event SemaphoreAcquirePending is generated when the function osSemaphoreAcquire blocks current running thread and waits for semaphore token to become available."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreAcquirePending (osSemaphoreId_t semaphore_id, uint32_t timeout)
```


The event **SemaphoreAcquirePending** is generated when the function osSemaphoreAcquire blocks current running thread and waits for semaphore token to become available.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
