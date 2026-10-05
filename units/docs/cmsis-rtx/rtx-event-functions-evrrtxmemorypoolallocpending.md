---
id: "rtx-event-functions-evrrtxmemorypoolallocpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolAllocPending"
summary: "The event MemoryPoolAllocPending is generated when the function osMemoryPoolAlloc blocks current running thread and waits for memory block to become available."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolAllocPending (osMemoryPoolId_t mp_id, uint32_t timeout)
```


The event **MemoryPoolAllocPending** is generated when the function osMemoryPoolAlloc blocks current running thread and waits for memory block to become available.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
