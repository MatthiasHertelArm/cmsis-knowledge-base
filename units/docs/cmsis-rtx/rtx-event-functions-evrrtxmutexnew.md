---
id: "rtx-event-functions-evrrtxmutexnew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMutexNew"
summary: "The event MutexNew is generated when the function osMutexNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMutexNew (const osMutexAttr_t *attr)
```


The event **MutexNew** is generated when the function osMutexNew is called.

**Value** in the Event Recorder shows:
  - **attr** : memory address of Mutex attributes or 0 when they are not specified.
