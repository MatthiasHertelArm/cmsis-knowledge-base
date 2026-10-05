---
id: "rtx-event-functions-evrrtxthreadnew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadNew"
summary: "The event ThreadNew is generated when the function osThreadNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadNew (osThreadFunc_t func, void *argument, const osThreadAttr_t *attr)
```


The event **ThreadNew** is generated when the function osThreadNew is called.

**Value** in the Event Recorder shows:
  - **func** : memory address of thread function. 
  - **argument** : memory address of thread function start argument.
  - **attr** : memory address of Thread attributes or 0 when they are not specified.
