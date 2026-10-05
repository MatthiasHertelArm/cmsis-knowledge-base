---
id: "rtx-event-functions-evrrtxmemoryalloc"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryAlloc"
summary: "The event MemoryAlloc is generated when allocation of a variable size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryAlloc (void *mem, uint32_t size, uint32_t type, void *block)
```


The event **MemoryAlloc** is generated when allocation of a variable size memory block completes.

**Value** in the Event Recorder shows:
  - **mem** : memory address of memory pool.
  - **size** : size of a memory block in bytes.
  - **type** : memory block type: 0 - generic, 1 - control block
  - **block** : memory address of allocated memory block or 0 in case of no memory is available.
