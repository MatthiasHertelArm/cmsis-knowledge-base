---
id: "rtx-event-functions-evrrtxsemaphorereleased"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreReleased"
summary: "The event SemaphoreReleased is generated when the function osSemaphoreRelease successfully releases the semaphore token."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreReleased (osSemaphoreId_t semaphore_id, uint32_t tokens)
```


The event **SemaphoreReleased** is generated when the function osSemaphoreRelease successfully releases the semaphore token.

**Value** in the Event Recorder shows:
  - **semaphore_id** : semaphore ID.
  - **tokens** : available tokens.
