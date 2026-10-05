---
id: "rtx-event-functions-evrrtxmutexacquiretimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexAcquireTimeout"
summary: "The event MutexAcquireTimeout is generated when wait for mutex to become available is aborted due to expired wait timeout."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexAcquireTimeout (osMutexId_t mutex_id)
```


The event **MutexAcquireTimeout** is generated when wait for mutex to become available is aborted due to expired wait timeout.

**Value** in the Event Recorder shows:
  - **mutex_id** : mutex ID.
