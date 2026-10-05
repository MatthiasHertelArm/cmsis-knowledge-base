---
id: "rtx-event-functions-evrrtxmutexcreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexCreated"
summary: "The event MutexCreated is generated when the function osMutexNew successfully creates a mutex object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexCreated (osMutexId_t mutex_id, const char *name)
```


The event **MutexCreated** is generated when the function osMutexNew successfully creates a mutex object.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
