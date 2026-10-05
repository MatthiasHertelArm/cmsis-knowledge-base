---
id: "frb-3-heap-memory-management-3-2-3-heap-3"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.3 Heap\\_3"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-3-heap-3"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

Heap\_3.c uses the standard library `malloc()` and `free()` functions, so the
linker configuration defines the heap size, and the
`configTOTAL_HEAP_SIZE` constant is not used.

Heap\_3 makes `malloc()` and `free()` thread-safe by temporarily suspending
the FreeRTOS scheduler for the duration of their execution. Chapter 8,
Resource Management, covers thread safety and scheduler suspension.
