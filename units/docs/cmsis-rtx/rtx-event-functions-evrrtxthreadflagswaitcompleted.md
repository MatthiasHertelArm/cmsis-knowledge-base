---
id: "rtx-event-functions-evrrtxthreadflagswaitcompleted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsWaitCompleted"
summary: "The event ThreadFlagsWaitCompleted is generated when waiting for thread flags ends because requested flags were signaled."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsWaitCompleted (uint32_t flags, uint32_t options, uint32_t thread_flags, osThreadId_t thread_id)
```


The event **ThreadFlagsWaitCompleted** is generated when waiting for thread flags ends because requested flags were signaled.

**Value** in the Event Recorder shows:
  - **flags** : flags thread was waiting for.
  - **option** : flags options (refer to thread flags options).
  - **thread_flags** : thread flags before clearing.
  - **thread_id** : thread ID.
