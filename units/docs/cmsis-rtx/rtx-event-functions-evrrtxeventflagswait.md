---
id: "rtx-event-functions-evrrtxeventflagswait"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsWait"
summary: "The event EventFlagsWait is generated when the function osEventFlagsWait is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsWait (osEventFlagsId_t ef_id, uint32_t flags, uint32_t options, uint32_t timeout)
```


The event **EventFlagsWait** is generated when the function osEventFlagsWait is called.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **flags** : flags to wait for. 
  - **options** : flags options (refer to event flags options).
  - **timeout** : CMSIS_RTOS_TimeOutValue.
