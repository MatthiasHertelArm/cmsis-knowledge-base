---
id: "rtx-event-functions-evrrtxkerneldestroyclass"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelDestroyClass"
summary: "The event KernelDestroyClass is generated when the function osKernelDestroyClass is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelDestroyClass (uint32_t safety_class, uint32_t mode)
```


The event **KernelDestroyClass** is generated when the function osKernelDestroyClass is called.

**Value** in the Event Recorder shows:
  - **safety_class** : safety class value. 
  - **mode** : operation mode.
