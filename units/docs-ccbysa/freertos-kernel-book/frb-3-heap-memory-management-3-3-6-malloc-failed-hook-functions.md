---
id: "frb-3-heap-memory-management-3-3-6-malloc-failed-hook-functions"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.6 Malloc Failed Hook Functions"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-6-malloc-failed-hook-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

Like the standard library `malloc()` function, `pvPortMalloc()` returns NULL
if it cannot allocate the requested amount of RAM. The malloc failed hook
(or callback) is an application-provided function that gets called if
`pvPortMalloc()` returns NULL. You must set `configUSE_MALLOC_FAILED_HOOK` to
1 in FreeRTOSConfig.h in order for the callback to occur. If the malloc failed
hook gets called inside a FreeRTOS API function that uses dynamic memory
allocation to create a kernel object, the object is not created.

If `configUSE_MALLOC_FAILED_HOOK` is set to 1 in FreeRTOSConfig.h, then
the application must provide a malloc failed hook function with the name
and prototype shown in Listing 3.12. The application can implement the
function in any way appropriate for the application. Many of the
provided FreeRTOS demo applications treat an allocation failure as a
fatal error, but that is not the best practice for production systems,
which should gracefully recover from allocation failures.





```c
void vApplicationMallocFailedHook( void );
```
***Listing 3.12*** *The malloc failed hook function name and prototype*
