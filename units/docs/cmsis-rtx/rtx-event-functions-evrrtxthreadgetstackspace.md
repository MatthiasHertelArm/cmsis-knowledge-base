---
id: "rtx-event-functions-evrrtxthreadgetstackspace"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetStackSpace"
summary: "The event ThreadGetStackSpace is generated when the function osThreadGetStackSpace is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetStackSpace (osThreadId_t thread_id, uint32_t stack_space)
```


The event **ThreadGetStackSpace** is generated when the function osThreadGetStackSpace is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **stack_space** : retrieved remaining stack space in bytes (0 in case of a failure).
