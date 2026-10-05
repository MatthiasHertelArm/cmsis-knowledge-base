---
id: "frb-3-heap-memory-management-3-2-1-heap-1"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.1 Heap\\_1"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-1-heap-1"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

It is common for small, dedicated embedded systems to only create tasks
and other kernel objects before starting the FreeRTOS scheduler. When
this is the case, memory only gets (dynamically) allocated by the kernel
before the application starts to perform any real-time functionality,
and the memory remains allocated for the application's lifetime. This
means the chosen allocation scheme does not have to consider the more
complex memory allocation issues, such as determinism and fragmentation,
and can instead prioritise attributes such as code size and simplicity.

Heap\_1.c implements a very basic version of `pvPortMalloc()`, and does not
implement `vPortFree()`. Applications that never delete a task or other
kernel objects have the potential to use heap\_1. Some commercially
critical and safety-critical systems that would otherwise prohibit the
use of dynamic memory allocation also have the potential to use heap\_1.
Critical systems often prohibit dynamic memory allocation because of the
uncertainties associated with non-determinism, memory fragmentation, and
failed allocations. Heap\_1 is always deterministic and cannot fragment
memory.

Heap\_1's implementation of `pvPortMalloc()` simply subdivides a simple
`uint8_t` array called the FreeRTOS heap into smaller blocks each time
it's called. The FreeRTOSConfig.h constant `configTOTAL_HEAP_SIZE` sets
the size of the array in bytes. Implementing the heap as a statically
allocated array makes FreeRTOS appear to consume a lot of RAM because
the heap becomes part of the FreeRTOS data.

Each dynamically allocated task results in two calls to `pvPortMalloc()`.
The first allocates a task control block (TCB), and the second the
task's stack. Figure 3.1 demonstrates how heap\_1 subdivides the simple
array as tasks get created.

Referring to Figure 3.1:

- **A** shows the array before creating any tasks—the entire array is free.

- **B** shows the array after creating one task.

- **C** shows the array after creating three tasks.




* * *

***Figure 3.1*** *RAM being allocated from the heap\_1 array each time a task is created*
* * *
