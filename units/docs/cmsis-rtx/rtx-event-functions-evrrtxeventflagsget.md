---
id: "rtx-event-functions-evrrtxeventflagsget"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsGet"
summary: "The event EventFlagsGet is generated when the function osEventFlagsGet is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsGet (osEventFlagsId_t ef_id, uint32_t event_flags)
```


The event **EventFlagsGet** is generated when the function osEventFlagsGet is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **event_flags** : retrieved current event flags.
