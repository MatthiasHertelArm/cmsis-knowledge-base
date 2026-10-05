---
id: "rtx-event-functions-evrrtxeventflagswaitcompleted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsWaitCompleted"
summary: "The event EventFlagsWaitCompleted is generated when waiting for event flags ends because requested flags were signaled."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsWaitCompleted (osEventFlagsId_t ef_id, uint32_t flags, uint32_t options, uint32_t event_flags)
```


The event **EventFlagsWaitCompleted** is generated when waiting for event flags ends because requested flags were signaled.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **flags** : flags to wait for.
  - **options** : flags option (refer to event flags options).
  - **event_flags** : event flags before clearing or 0 if specified flags have not been set.
