---
id: "rtx-event-functions-evrrtxmemorypoolalloc"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolAlloc"
summary: "The event MemoryPoolAlloc is generated when the function osMemoryPoolAlloc is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolAlloc (osMemoryPoolId_t mp_id, uint32_t timeout)
```


The event **MemoryPoolAlloc** is generated when the function osMemoryPoolAlloc is called.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
