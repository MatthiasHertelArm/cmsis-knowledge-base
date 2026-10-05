---
id: "rtx-event-functions-evrrtxthreadflagsget"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsGet"
summary: "The event ThreadFlagsGet is generated when the function osThreadFlagsGet is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsGet (uint32_t thread_flags)
```


The event **ThreadFlagsGet** is generated when the function osThreadFlagsGet is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **thread_flags** : current thread flags.
