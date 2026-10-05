---
id: "rtx-event-functions-evrrtxeventflagswaitnotcompleted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsWaitNotCompleted"
summary: "The event EventFlagsWaitNotCompleted is generated when the function osEventFlagsWait returns without timeout and specified event flags were not signaled."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsWaitNotCompleted (osEventFlagsId_t ef_id, uint32_t flags, uint32_t options)
```


The event **EventFlagsWaitNotCompleted** is generated when the function osEventFlagsWait returns without timeout and specified event flags were not signaled.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **flags** : flags to wait for.
  - **options** : flags options (refer to event flags options).
