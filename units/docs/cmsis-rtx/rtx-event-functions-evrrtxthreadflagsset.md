---
id: "rtx-event-functions-evrrtxthreadflagsset"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsSet"
summary: "The event ThreadFlagsSet is generated when the function osThreadFlagsSet is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsSet (osThreadId_t thread_id, uint32_t flags)
```


The event **ThreadFlagsSet** is generated when the function osThreadFlagsSet is called.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **flags** : flags that shall be set.
