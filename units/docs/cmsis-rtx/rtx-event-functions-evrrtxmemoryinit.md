---
id: "rtx-event-functions-evrrtxmemoryinit"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryInit"
summary: "The event MemoryInit is generated when initialization of a variable size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryInit (void *mem, uint32_t size, uint32_t result)
```


The event **MemoryInit** is generated when initialization of a variable size memory block completes.

**Value** in the Event Recorder shows:
  - **mem** : memory address of memory pool.
  - **size** : size of a memory pool in bytes.
  - **result** : execution status: 1 - success, 0 - failure.
