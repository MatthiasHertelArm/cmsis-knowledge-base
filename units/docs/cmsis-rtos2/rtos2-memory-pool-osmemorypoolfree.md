---
id: "rtos2-memory-pool-osmemorypoolfree"
type: "concept"
domain: "rtos"
title: "Memory Pool: osMemoryPoolFree"
summary: "The function osMemoryPoolFree frees the memory pool block specified by the parameter block in the memory pool object specified by the parameter mp_id. The memory block is put back to the list of available blocks."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMemoryPoolFree (osMemoryPoolId_t mp_id, void *block)
```


The function **osMemoryPoolFree** frees the memory pool block specified by the parameter _block_ in the memory pool object
specified by the parameter _mp_id._ The memory block is put back to the list of available blocks.

If another thread is waiting for memory to become available the thread is put to READY state.

Possible osStatus_t return values:
 - **osOK:** the memory has been freed.
 - **osErrorParameter:** parameter _mp_id_ is `NULL` or invalid, _block_ points to invalid memory.
 - **osErrorResource:** the memory pool is in an invalid state.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified memory pool.

**Note:** **osMemoryPoolFree** may perform certain checks on the _block_ pointer given. But using **osMemoryPoolFree** 
with a pointer other than one received from osMemoryPoolAlloc has **UNPREDICTED** behaviour.

**Note:** This function may be called from Interrupt Service Routines.

**Code** **Example**

Refer to osMemoryPoolNew.
