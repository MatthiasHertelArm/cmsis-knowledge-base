---
id: "rtx-event-functions-evrrtxmutexacquirepending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexAcquirePending"
summary: "The event MutexAcquirePending is generated when the function osMutexAcquire blocks current running thread and waits for mutex to become available."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexAcquirePending (osMutexId_t mutex_id, uint32_t timeout)
```


The event **MutexAcquirePending** is generated when the function osMutexAcquire blocks current running thread and waits for mutex to become available.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
