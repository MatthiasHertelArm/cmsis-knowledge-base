---
id: "rtx-event-functions-evrrtxmutexacquire"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexAcquire"
summary: "The event MutexAcquire is generated when the function osMutexAcquire is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexAcquire (osMutexId_t mutex_id, uint32_t timeout)
```


The event **MutexAcquire** is generated when the function osMutexAcquire is called.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
