---
id: "rtx-event-functions-evrrtxdelayuntil"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxDelayUntil"
summary: "The event DelayUntil is generated when the function osDelayUntil is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxDelayUntil (uint32_t ticks)
```


The event **DelayUntil** is generated when the function osDelayUntil is called.

**Value** in the Event Recorder shows:
  - **ticks** : absolute delay time in ticks.
