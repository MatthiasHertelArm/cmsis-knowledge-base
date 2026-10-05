---
id: "rtx-event-functions-evrrtxthreadblocked"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadBlocked"
summary: "The event ThreadBlocked is generated when the current running thread execution is blocked."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadBlocked (osThreadId_t thread_id, uint32_t timeout)
```


The event **ThreadBlocked** is generated when the current running thread execution is blocked.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
