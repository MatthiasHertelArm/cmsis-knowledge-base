---
id: "rtx-event-functions-evrrtxsemaphorecreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreCreated"
summary: "The event SemaphoreCreated is generated when the function osSemaphoreNew successfully creates a semaphore object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreCreated (osSemaphoreId_t semaphore_id, const char *name)
```


The event **SemaphoreCreated** is generated when the function osSemaphoreNew successfully creates a semaphore object.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
