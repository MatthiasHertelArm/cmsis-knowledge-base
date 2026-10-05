---
id: "rtx-event-functions-evrrtxmemorypoolgetcapacity"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolGetCapacity"
summary: "The event MemoryPoolGetCapacity is generated when the function osMemoryPoolGetCapacity is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolGetCapacity (osMemoryPoolId_t mp_id, uint32_t capacity)
```


The event **MemoryPoolGetCapacity** is generated when the function osMemoryPoolGetCapacity is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **capacity** : retrieved maximum number of memory blocks (0 in case of a failure).
