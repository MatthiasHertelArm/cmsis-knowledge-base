---
id: "rtx-event-functions-evrrtxsemaphorerelease"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreRelease"
summary: "The event SemaphoreRelease is generated when the function osSemaphoreRelease is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreRelease (osSemaphoreId_t semaphore_id)
```


The event **SemaphoreRelease** is generated when the function osSemaphoreRelease is called.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
