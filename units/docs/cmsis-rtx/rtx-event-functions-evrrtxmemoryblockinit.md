---
id: "rtx-event-functions-evrrtxmemoryblockinit"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryBlockInit"
summary: "The event MemoryBlockInit is generated when initialization of a fixed size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryBlockInit (osRtxMpInfo_t *mp_info, uint32_t block_count, uint32_t block_size, void *block_mem)
```


The event **MemoryBlockInit** is generated when initialization of a fixed size memory block completes.

**Value** in the Event Recorder shows:
  - **mp_info** : memory address of memory pool info.
  - **block_count** : maximum number of memory blocks in memory pool.
  - **block_size** : size of a memory block in bytes.
  - **block_mem** : memory address of memory for block storage.
