---
id: "frb-3-heap-memory-management-3-3-2-the-xportgetfreeheapsize-api-funct"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.2 The xPortGetFreeHeapSize() API Function"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-2-the-xportgetfreeheapsize-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

The `xPortGetFreeHeapSize()` API function returns the number of free bytes
in the heap at the time the function is called. It does not provide
information on heap fragmentation.

`xPortGetFreeHeapSize()` is not implemented for heap\_3.





```c
size_t xPortGetFreeHeapSize( void );
```
***Listing 3.7*** *The xPortGetFreeHeapSize() API function prototype*


**Return value:**

- `xPortGetFreeHeapSize()` returns the number of bytes that remain unallocated in the heap at
   the time it is called.
