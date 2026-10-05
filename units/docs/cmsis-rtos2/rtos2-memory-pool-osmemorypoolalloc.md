---
id: "rtos2-memory-pool-osmemorypoolalloc"
type: "concept"
domain: "rtos"
title: "Memory Pool: osMemoryPoolAlloc"
summary: "The blocking function osMemoryPoolAlloc allocates the memory pool parameter mpid and returns a pointer to the address of the allocated memory or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void *osMemoryPoolAlloc (osMemoryPoolId_t mp_id, uint32_t timeout)
```


The blocking function **osMemoryPoolAlloc** allocates the memory pool parameter _mp_id_ and returns a pointer to the address
of the allocated memory or `0` in case of an error.

The parameter _timeout_ specifies how long the system waits to allocate the memory. While the system waits, the thread
that is calling this function is put into the BLOCKED state. The thread will become READY
as soon as at least one block of memory gets available.

The parameter timeout can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the memory is allocated (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

The result is the pointer to the memory block allocated, or NULL if no memory is available.

**Note:** It is in the responsibility of the user to respect the block size, i.e. not access memory beyond the blocks limit.
 
**Note:** May be called from Interrupt Service Routines if the parameter _timeout_ is set to
`0`.

**Code** **Example**

Refer to osMemoryPoolNew.
