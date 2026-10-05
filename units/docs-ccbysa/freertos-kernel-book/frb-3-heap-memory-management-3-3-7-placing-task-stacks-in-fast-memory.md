---
id: "frb-3-heap-memory-management-3-3-7-placing-task-stacks-in-fast-memory"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.7 Placing Task Stacks in Fast Memory"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-7-placing-task-stacks-in-fast-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

Because stacks are written to and read from at a high rate, they should
be placed in fast memory, but that might not be where you want the heap to
reside. FreeRTOS uses the `pvPortMallocStack()` and `vPortFreeStack()`
macros to optionally enable stacks that are allocated within the FreeRTOS API
code to have their own memory allocator. If you want the stack to come
from the heap managed by `pvPortMalloc()` then leave `pvPortMallocStack()`
and `vPortFreeStack()` undefined as they default to calling
`pvPortMalloc()` and `vPortFree()`, respectively. Otherwise, define the
macros to call application-provided functions as shown in Listing 3.13.





```c
/* Functions provided by the application writer than allocate and free
   memory from a fast area of RAM. */

void *pvMallocFastMemory( size_t xWantedSize );

void vPortFreeFastMemory( void *pvBlockToFree );

/* Add the following to FreeRTOSConfig.h to map the pvPortMallocStack()
   and vPortFreeStack() macros to the functions that use fast memory. */

#define pvPortMallocStack( x ) pvMallocFastMemory( x )

#define vPortFreeStack( x ) vPortFreeFastMemory( x )
```
***Listing 3.13*** *Mapping the pvPortMallocStack() and vPortFreeStack() macros to an application defined memory allocator*
