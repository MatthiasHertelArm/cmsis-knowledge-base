---
id: "rtx-event-functions-evrrtxmutexreleased"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexReleased"
summary: "The event MutexReleased is generated when the function osMutexRelease successfully releases a mutex."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexReleased (osMutexId_t mutex_id, uint32_t lock)
```


The event **MutexReleased** is generated when the function osMutexRelease successfully releases a mutex.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
  - **lock** : current lock counter state.
