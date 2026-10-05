---
id: "rtx-event-functions-evrrtxthreadgetid"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetId"
summary: "The event ThreadGetId is generated when the function osThreadGetId is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetId (osThreadId_t thread_id)
```


The event **ThreadGetId** is generated when the function osThreadGetId is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : retrieved thread (0 in case of a failure).
