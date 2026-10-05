---
id: "rtx-event-functions-evrrtxmemorypoolallocated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolAllocated"
summary: "The event MemoryPoolAllocated is generated when the function osMemoryPoolAlloc successfully allocates the memory block."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolAllocated (osMemoryPoolId_t mp_id, void *block)
```


The event **MemoryPoolAllocated** is generated when the function osMemoryPoolAlloc successfully allocates the memory block.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **block** : memory address of the allocated memory block.
