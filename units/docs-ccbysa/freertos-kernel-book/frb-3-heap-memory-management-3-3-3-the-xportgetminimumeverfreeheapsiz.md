---
id: "frb-3-heap-memory-management-3-3-3-the-xportgetminimumeverfreeheapsiz"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.3 The xPortGetMinimumEverFreeHeapSize() API Function"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-3-the-xportgetminimumeverfreeheapsize-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

The `xPortGetMinimumEverFreeHeapSize()` API function returns the minimum
number of unallocated bytes that have ever existed in the heap since the
FreeRTOS application started executing.

The value returned by `xPortGetMinimumEverFreeHeapSize()` indicates how
close the application has ever come to running out of heap space. For
example, if `xPortGetMinimumEverFreeHeapSize()` returns 200, then, at some
time since the application started executing, it came within 200 bytes
of running out of heap space.

`xPortGetMinimumEverFreeHeapSize()` can also be used to optimise the heap
size. For example, if `xPortGetMinimumEverFreeHeapSize()` returns 2000
after executing the code that you know has the highest heap usage,
`configTOTAL_HEAP_SIZE` can be reduced by up to 2000 bytes.

`xPortGetMinimumEverFreeHeapSize()` is only implemented in heap\_4 and heap\_5.





```c
size_t xPortGetMinimumEverFreeHeapSize( void );
```
***Listing 3.8*** *The xPortGetMinimumEverFreeHeapSize() API function prototype*


**Return value:**

- `xPortGetMinimumEverFreeHeapSize()` returns the minimum number of unallocated
  bytes that existed in the heap since the FreeRTOS application started executing.
