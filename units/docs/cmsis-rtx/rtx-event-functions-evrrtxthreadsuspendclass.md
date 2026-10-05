---
id: "rtx-event-functions-evrrtxthreadsuspendclass"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadSuspendClass"
summary: "The event ThreadSuspendClass is generated when the function osThreadSuspendClass is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadSuspendClass (uint32_t safety_class, uint32_t mode)
```


The event **ThreadSuspendClass** is generated when the function osThreadSuspendClass is called.

**Value** in the Event Recorder shows:
  - **safety_class** : safety class value.
  - **mode** : operation mode.
