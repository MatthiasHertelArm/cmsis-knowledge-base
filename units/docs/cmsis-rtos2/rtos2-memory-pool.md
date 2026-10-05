---
id: "rtos2-memory-pool"
type: "concept"
domain: "rtos"
title: "Memory Pool"
summary: "Manage thread-safe fixed-size blocks of dynamic memory."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mem_pool.txt"
license: "Apache-2.0"
mode: "V"
---

Manage thread-safe fixed-size blocks of dynamic memory.

**Memory** **Pools** are fixed-size blocks of memory that are thread-safe. They operate much faster than the dynamically
allocated heap and do not suffer from fragmentation. Being thread-safe, they can be accessed from threads and ISRs alike.

A Memory Pool can be seen as a linked list of available (unused) memory blocks of fixed and equal size. Allocating memory
from a pool (using osMemoryPoolAlloc) simply unchains a block from the list and hands over control to the user. Freeing
memory to the pool (using osMemoryPoolFree) simply rechains the block into the list.

" "CMSIS-RTOS Memory Pools"

**Note:** One must not write to freed block. It is up to the implementation to reuse the memory of unused blocks for internal
control data, i.e. linked list pointers.

**Shared** **memory** is one of the basic models to exchange information between threads. Using memory pools for exchanging
data, you can share more complex objects between threads if compared to a CMSIS_RTOS_Message. Memory pool management
functions are used to define and manage such fixed-sized memory pools.

**Note:** The functions osMemoryPoolAlloc, osMemoryPoolFree, osMemoryPoolGetCapacity,
osMemoryPoolGetBlockSize, osMemoryPoolGetCount, osMemoryPoolGetSpace can be called from
Interrupt Service Routines.
