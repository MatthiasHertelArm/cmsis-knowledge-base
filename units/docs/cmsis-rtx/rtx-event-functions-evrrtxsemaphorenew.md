---
id: "rtx-event-functions-evrrtxsemaphorenew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxSemaphoreNew"
summary: "The event SemaphoreNew is generated when the function osSemaphoreNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxSemaphoreNew (uint32_t max_count, uint32_t initial_count, const osSemaphoreAttr_t *attr)
```


The event **SemaphoreNew** is generated when the function osSemaphoreNew is called.

**Value** in the Event Recorder shows:
  - **max_count** : maximum number of available tokens. 
  - **initial_count** : initial number of available tokens.
  - **attr** : memory address of Semaphore attributes or 0 when they are not specified.
