---
id: "rtx-event-functions-evrrtxmemorypoolgetspace"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolGetSpace"
summary: "The event MemoryPoolGetSpace is generated when the function osMemoryPoolGetSpace is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolGetSpace (osMemoryPoolId_t mp_id, uint32_t space)
```


The event **MemoryPoolGetSpace** is generated when the function osMemoryPoolGetSpace is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **space** : retrieved number of memory blocks available (0 in case of a failure).
