---
id: "rtx-event-functions-evrrtxeventflagscleardone"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsClearDone"
summary: "The event EventFlagsClearDone is generated when the function osEventFlagsClear successfully clears the event flags."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsClearDone (osEventFlagsId_t ef_id, uint32_t event_flags)
```


The event **EventFlagsClearDone** is generated when the function osEventFlagsClear successfully clears the event flags.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **event_flags** : event flags before clearing.
