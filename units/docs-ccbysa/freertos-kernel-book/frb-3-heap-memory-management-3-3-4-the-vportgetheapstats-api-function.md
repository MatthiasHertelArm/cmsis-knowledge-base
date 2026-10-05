---
id: "frb-3-heap-memory-management-3-3-4-the-vportgetheapstats-api-function"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.4 The vPortGetHeapStats() API Function"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-4-the-vportgetheapstats-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

Heap\_4 and heap\_5 implement `vPortGetHeapStats()`, which completes the
`HeapStats_t` structure pass by reference as the function's only parameter.

Listing 3.9 shows the `vPortGetHeapStats()` function prototype. Listing 3.10
shows the `HeapStats_t` structure members.





```c
void vPortGetHeapStats( HeapStats_t *xHeapStats );
```
***Listing 3.9*** *The vPortGetHeapStatus() API function prototype*






```c
/* Prototype of the vPortGetHeapStats() function. */
void vPortGetHeapStats( HeapStats_t *xHeapStats );

/* Definition of the HeapStats_t structure. All sizes specified in bytes. */
typedef struct xHeapStats
{
    /* The total heap size currently available - this is the sum of all the
       free blocks, not the largest available block. */
    size_t xAvailableHeapSpaceInBytes;

    /* The size of the largest free block within the heap at the time
       vPortGetHeapStats() is called. */
    size_t xSizeOfLargestFreeBlockInBytes;

    /* The size of the smallest free block within the heap at the time
       vPortGetHeapStats() is called. */
    size_t xSizeOfSmallestFreeBlockInBytes;

    /* The number of free memory blocks within the heap at the time
       vPortGetHeapStats() is called. */
    size_t xNumberOfFreeBlocks;

    /* The minimum amount of total free memory (sum of all free blocks)
       there has been in the heap since the system booted. */
    size_t xMinimumEverFreeBytesRemaining;

    /* The number of calls to pvPortMalloc() that have returned a valid
       memory block. */
    size_t xNumberOfSuccessfulAllocations;

    /* The number of calls to vPortFree() that has successfully freed a
       block of memory. */
    size_t xNumberOfSuccessfulFrees;
} HeapStats_t;
```
***Listing 3.10*** *The HeapStatus\_t() structure*
