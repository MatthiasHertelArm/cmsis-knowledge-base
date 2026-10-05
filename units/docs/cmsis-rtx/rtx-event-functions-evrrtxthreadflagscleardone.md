---
id: "rtx-event-functions-evrrtxthreadflagscleardone"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsClearDone"
summary: "The event ThreadFlagsClearDone is generated when the function osThreadFlagsClear successfully clears thread flags."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsClearDone (uint32_t thread_flags)
```


The event **ThreadFlagsClearDone** is generated when the function osThreadFlagsClear successfully clears thread flags.

**Value** in the Event Recorder shows:
  - **thread_flags** : thread flags before clearing.
