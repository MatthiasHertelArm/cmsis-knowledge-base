---
id: "rtx-event-functions-evrrtxthreadterminatezone"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadTerminateZone"
summary: "The event ThreadTerminateZone is generated when the function osThreadTerminateZone is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadTerminateZone (uint32_t zone)
```


The event **ThreadTerminateZone** is generated when the function osThreadTerminateZone is called.

**Value** in the Event Recorder shows:
  - **zone** : MPU Protected Zone value.
