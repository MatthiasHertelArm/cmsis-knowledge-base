---
id: "rtx-event-functions-evrrtxsemaphoregetcount"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreGetCount"
summary: "The event SemaphoreGetCount is generated when the function osSemaphoreGetCount is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreGetCount (osSemaphoreId_t semaphore_id, uint32_t count)
```


The event **SemaphoreGetCount** is generated when the function osSemaphoreGetCount is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **count** : retrieved current number of available tokens.
