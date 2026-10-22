---
id: "rtos2-memory-pool-osmemorypoolgetname"
type: "concept"
domain: "rtos"
title: "Memory Pool: osMemoryPoolGetName"
summary: "The function osMemoryPoolGetName returns the pointer to the name string of the memory pool identified by parameter \\a mp_id or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osMemoryPoolGetName (osMemoryPoolId_t mp_id)
```


The function **osMemoryPoolGetName** returns the pointer to the name string of the memory pool identified by parameter \a
mp_id or `NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
