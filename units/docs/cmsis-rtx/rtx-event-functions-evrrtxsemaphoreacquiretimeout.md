---
id: "rtx-event-functions-evrrtxsemaphoreacquiretimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreAcquireTimeout"
summary: "The event SemaphoreAcquireTimeout is generated when wait for semaphore to become available is aborted due to expired wait timeout."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreAcquireTimeout (osSemaphoreId_t semaphore_id)
```


The event **SemaphoreAcquireTimeout** is generated when wait for semaphore to become available is aborted due to expired wait timeout.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
