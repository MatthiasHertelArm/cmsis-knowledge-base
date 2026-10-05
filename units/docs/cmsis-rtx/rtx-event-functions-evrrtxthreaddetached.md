---
id: "rtx-event-functions-evrrtxthreaddetached"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadDetached"
summary: "The event ThreadDetached is generated when the function osThreadDetach successfully detaches the specified thread."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadDetached (osThreadId_t thread_id)
```


The event **ThreadDetached** is generated when the function osThreadDetach successfully detaches the specified thread.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
