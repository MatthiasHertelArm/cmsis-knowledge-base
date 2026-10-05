---
id: "rtx-event-functions-evrrtxthreadcreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadCreated"
summary: "The event ThreadCreated is generated when the function osThreadNew successfully creates a thread object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadCreated (osThreadId_t thread_id, uint32_t thread_addr, const char *name)
```


The event **ThreadCreated** is generated when the function osThreadNew successfully creates a thread object.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
