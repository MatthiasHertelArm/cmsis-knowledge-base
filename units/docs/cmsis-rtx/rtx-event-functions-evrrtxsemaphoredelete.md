---
id: "rtx-event-functions-evrrtxsemaphoredelete"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreDelete"
summary: "The event SemaphoreDelete is generated when the function osSemaphoreDelete is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreDelete (osSemaphoreId_t semaphore_id)
```


The event **SemaphoreDelete** is generated when the function osSemaphoreDelete is called.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
