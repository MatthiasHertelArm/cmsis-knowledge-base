---
id: "rtx-event-functions-evrrtxthreadflagswaittimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsWaitTimeout"
summary: "The event ThreadFlagsWaitTimeout is generated when wait for thread flags to become signaled is aborted due to expired wait timeout."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsWaitTimeout (osThreadId_t thread_id)
```


The event **ThreadFlagsWaitTimeout** is generated when wait for thread flags to become signaled is aborted due to expired wait timeout.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
