---
id: "rtx-event-functions-evrrtxeventflagsdelete"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsDelete"
summary: "The event EventFlagsDelete is generated when the function osEventFlagsDelete is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsDelete (osEventFlagsId_t ef_id)
```


The event **EventFlagsDelete** is generated when the function osEventFlagsDelete is called.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
