---
id: "rtx-event-functions-evrrtxmemorypooldelete"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolDelete"
summary: "The event MemoryPoolDelete is generated when the function osMemoryPoolDelete is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolDelete (osMemoryPoolId_t mp_id)
```


The event **MemoryPoolDelete** is generated when the function osMemoryPoolDelete is called.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
