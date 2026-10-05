---
id: "rtx-event-functions-evrrtxthreadgetzone"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadGetZone"
summary: "The event ThreadGetZone is generated when the function osThreadGetZone is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadGetZone (osThreadId_t thread_id, uint32_t zone)
```


The event **ThreadGetZone** is generated when the function osThreadGetZone is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **zone** : retrieved MPU Protected Zone value (osErrorId in case of a failure).
