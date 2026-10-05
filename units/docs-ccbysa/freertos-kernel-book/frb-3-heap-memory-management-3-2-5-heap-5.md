---
id: "frb-3-heap-memory-management-3-2-5-heap-5"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.5 Heap\\_5"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-5-heap-5"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

Heap\_5 uses the same allocation algorithm as heap\_4. Unlike heap\_4,
which is limited to allocating memory from a single array, heap\_5 can
combine memory from multiple separated memory spaces into a single heap.
Heap\_5 is useful when the RAM provided by the system on which FreeRTOS
is running does not appear as a single contiguous (without space) block
in the system's memory map.
