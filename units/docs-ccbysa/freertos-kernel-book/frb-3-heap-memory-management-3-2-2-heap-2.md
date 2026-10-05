---
id: "frb-3-heap-memory-management-3-2-2-heap-2"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.2 Heap\\_2"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-2-heap-2"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

Heap\_2 is superseded by heap\_4, which includes enhanced functionality.
Heap\_2 is kept in the FreeRTOS distribution for backward compatibility
and is not recommended for new designs.

Heap\_2.c also works by subdividing an array dimensioned by the
`configTOTAL_HEAP_SIZE` constant. It uses a best-fit algorithm to allocate
memory, and, unlike heap\_1, it does implement `vPortFree()`. Again,
implementing the heap as a statically allocated array makes FreeRTOS
appear to consume a lot of RAM because the heap becomes part of the
FreeRTOS data.

The best-fit algorithm ensures that `pvPortMalloc()` uses the free block
of memory that is closest in size to the number of bytes requested. For
example, consider the scenario where:

- The heap contains three blocks of free memory that are 5 bytes, 25
  bytes, and 100 bytes, respectively.
- `pvPortMalloc()` requests 20 bytes of RAM.

The smallest free block of RAM into which the requested number of bytes
fits is the 25-byte block, so `pvPortMalloc()` splits the 25-byte block
into one block of 20 bytes and one block of 5 bytes before returning
a pointer to the 20-byte block[^2]. The new 5-byte block remains available
for future calls to `pvPortMalloc()`.

[^2]: This is an oversimplification, because heap\_2 stores information
on the block sizes within the heap area, so the sum of the two split
blocks will actually be less than 25.

Unlike heap\_4, heap\_2 does not combine adjacent free blocks into a
single larger block, so it is more susceptible to fragmentation than
heap\_4. However, fragmentation is not an issue if the allocated and
subsequently freed blocks are always the same size.



* * *

***Figure 3.2*** *RAM being allocated and freed from the heap\_2 array as tasks are created and deleted*
* * *

Figure 3.2 demonstrates how the best-fit algorithm works when a task is
created, deleted, and created again. Referring to Figure 3.2:

- **A** shows the array after allocating three tasks. A large free
  block remains at the top of the array.

- **B** shows the array after deleting one of the tasks. The large
  free block at the top of the array remains. There are now also two
  smaller free blocks that previously held the TCB and stack of the
  deleted task.

- **C** shows the situation after creating another task. Creating
  the task resulted in two calls to `pvPortMalloc()` from within the
  `xTaskCreate()` API function, one to allocate a new TCB and the other
  to allocate the task stack. Section 3.4 of this book describes
  `xTaskCreate()`.

  Every TCB is the same size, so the best-fit algorithm reuses the block
  of RAM that held the TCB of the deleted task to hold the TCB of the
  created task.

  If the size of the stack allocated to the newly created task is the
  same size as that allocated to the previously deleted task, then the
  best-fit algorithm reuses the block of RAM that held the stack of the
  deleted task to hold the stack of the created task.

  The larger unallocated block at the top of the array remains
  untouched.

Heap\_2 is not deterministic but is faster than most standard library
implementations of `malloc()` and `free()`.
