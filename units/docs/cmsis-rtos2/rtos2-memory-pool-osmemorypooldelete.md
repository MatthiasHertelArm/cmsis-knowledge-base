---
id: "rtos2-memory-pool-osmemorypooldelete"
type: "concept"
domain: "rtos"
title: "Memory Pool: osMemoryPoolDelete"
summary: "The function osMemoryPoolDelete deletes a memory pool object specified by parameter mpid. It releases internal memory obtained for memory pool handling. After this call, the mpid is no longer valid and cannot be used."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMemoryPoolDelete (osMemoryPoolId_t mp_id)
```


The function **osMemoryPoolDelete** deletes a memory pool object specified by parameter _mp_id._ It releases internal
memory obtained for memory pool handling. After this call, the _mp_id_ is no longer valid and cannot be used. The
memory pool may be created again using the function osMemoryPoolNew.

Possible osStatus_t return values:
 - **osOK:** the memory pool object has been deleted.
 - **osErrorParameter:** parameter _mp_id_ is `NULL` or invalid.
 - **osErrorResource:** the memory pool is in an invalid state.
 - **osErrorISR:** **osMemoryPoolDelete** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified memory pool.

**Note:** This function **cannot** be called from Interrupt Service Routines.
