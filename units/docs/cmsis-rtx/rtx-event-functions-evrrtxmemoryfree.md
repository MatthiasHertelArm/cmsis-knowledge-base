---
id: "rtx-event-functions-evrrtxmemoryfree"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryFree"
summary: "The event MemoryFree is generated when deallocation of a variable size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryFree (void *mem, void *block, uint32_t result)
```


The event **MemoryFree** is generated when deallocation of a variable size memory block completes.

**Value** in the Event Recorder shows:
  - **mem** : memory address of memory pool.
  - **block** : memory address of block to be returned to the memory pool.
  - **result** : execution status: 1 - success, 0 - failure.
