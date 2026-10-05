---
id: "rtx-event-functions-evrrtxsemaphoregetname"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreGetName"
summary: "The event SemaphoreGetName is generated when the function osSemaphoreGetName is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreGetName (osSemaphoreId_t semaphore_id, const char *name)
```


The event **SemaphoreGetName** is generated when the function osSemaphoreGetName is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **name** : retrieved memory address of name string (0 in case of a failure).
