---
id: "rtos2-memory-pool-osmemorypoolgetcapacity"
type: "concept"
domain: "rtos"
title: "Memory Pool: osMemoryPoolGetCapacity"
summary: "The function osMemoryPoolGetCapacity returns the maximum number of memory blocks in the memory pool object specified by parameter mp_id or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osMemoryPoolGetCapacity (osMemoryPoolId_t mp_id)
```


The function **osMemoryPoolGetCapacity** returns the maximum number of memory blocks in the memory pool object specified by
parameter _mp_id_ or `0` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
