---
id: "rtx-event-functions-evrrtxthreadflagswaitnotcompleted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsWaitNotCompleted"
summary: "The event ThreadFlagsWaitNotCompleted is generated when the function osThreadFlagsWait returns without timeout and specified thread flags were not signaled."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsWaitNotCompleted (uint32_t flags, uint32_t options)
```


The event **ThreadFlagsWaitNotCompleted** is generated when the function osThreadFlagsWait returns without timeout and specified thread flags were not signaled.

**Value** in the Event Recorder shows:
  - **flags** : flags thread was waiting for.
  - **options** : flags options (refer to thread flags options).
