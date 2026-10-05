---
id: "rtx-event-functions-evrrtxthreadflagsclear"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsClear"
summary: "The event ThreadFlagsClear is generated when the function osThreadFlagsClear is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsClear (uint32_t flags)
```


The event **ThreadFlagsClear** is generated when the function osThreadFlagsClear is called.

**Value** in the Event Recorder shows:
  - **flags** : flags that shall be cleared.
