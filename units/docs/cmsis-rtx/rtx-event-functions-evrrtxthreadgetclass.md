---
id: "rtx-event-functions-evrrtxthreadgetclass"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetClass"
summary: "The event ThreadGetClass is generated when the function osThreadGetClass is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetClass (osThreadId_t thread_id, uint32_t safety_class)
```


The event **ThreadGetClass** is generated when the function osThreadGetClass is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **safety_class** : retrieved safety class value (osErrorId in case of a failure).
