---
id: "rtx-event-functions-evrrtxthreadgetcount"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetCount"
summary: "The event ThreadGetCount is generated when the function osThreadGetCount is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetCount (uint32_t count)
```


The event **ThreadGetCount** is generated when the function osThreadGetCount is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **count** : retrieved number of active threads (0 in case of a failure).
