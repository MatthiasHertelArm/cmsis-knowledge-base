---
id: "frb-3-heap-memory-management-3-2-4-heap-4"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.4 Heap\\_4"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-4-heap-4"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

Like heap\_1 and heap\_2, heap\_4 works by subdividing an array into
smaller blocks. As before, the array is statically allocated and
dimensioned by `configTOTAL_HEAP_SIZE`, which makes FreeRTOS appear to use
a lot of RAM as the heap becomes part of the FreeRTOS data.

Heap\_4 uses a first-fit algorithm to allocate memory. Unlike heap\_2,
heap\_4 combines (coalesces) adjacent free blocks of memory into a
single larger block, which minimizes the risk of memory fragmentation.

The first fit algorithm ensures `pvPortMalloc()` uses the first free block
of memory that is large enough to hold the number of bytes requested.
For example, consider the scenario where:

- The heap contains three blocks of free memory that, in the order in
  which they appear in the array, are 5 bytes, 200 bytes, and 100
  bytes, respectively.
- `pvPortMalloc()` requests 20 bytes of RAM.

The first free block of RAM that the requested number of bytes fits is
the 200-byte block, so `pvPortMalloc()` splits the 200-byte block into one
block of 20 bytes and one of 180 bytes[^3], before returning a pointer
to the 20-byte block. The new 180-byte block remains available to future
calls to `pvPortMalloc()`.

[^3]: This is an oversimplification, because heap\_4 stores information
on the block sizes within the heap area, so the sum of the two split
blocks will actually be less than 200 bytes.

Heap\_4 combines (coalesces) adjacent free blocks into a single larger
block, minimizing the risk of fragmentation, and making it suitable for
applications that repeatedly allocate and free different-sized blocks of
RAM.




* * *

***Figure 3.3*** *RAM being allocated and freed from the heap\_4 array*
* * *

Figure 3.3 demonstrates how the heap\_4 first-fit algorithm with memory
coalescence works. Referring to Figure 3.3:

- **A** shows the array after creating three tasks. A large free
  block remains at the top of the array.

- **B** shows the array after deleting one of the tasks. The large
  free block at the top of the array remains. There is now another
  free block where the TCB and stack of the deleted task used to be.
  Unlike in the heap\_2 example, heap\_4 merges the two memory blocks
  that previously held the TCB and stack of the deleted task,
  respectively, into a larger single free block.

- **C** shows the situation after creating a FreeRTOS queue.
  Section 5.3 of this book describes the `xQueueCreate()` API function
  used to allocate queues dynamically. `xQueueCreate()` calls
  `pvPortMalloc()` to allocate the RAM used by the queue. As heap\_4 uses
  a first-fit algorithm, `pvPortMalloc()` allocates RAM from the first
  free RAM block that is large enough to hold the queue, which in
  Figure 3.3, was the RAM freed by deleting the task. The queue does not
  consume all the RAM in the free block, so the block is split into
  two, and the unused portion remains available to future calls to
  `pvPortMalloc()`.

- **D** shows the situation after calling `pvPortMalloc()` directly
  from application code, rather than indirectly by calling a FreeRTOS
  API function. The user allocated block was small enough to fit in
  the first free block, which was the block between the memory
  allocated to the queue, and the memory allocated to the TCB
  following it.

  The memory freed by deleting the task has now split into three
  separate blocks; the first block holds the queue, the second block
  holds the user allocated memory, and the third block remains free.

- **E** shows the situation after deleting the queue, which
  automatically frees the memory allocated to the deleted queue. There
  is now free memory on either side of the user allocated block.

- **F** shows the situation after freeing the user allocated
  memory. The memory previously used by the user allocated block has
  been combined with the free memory on either side to create a larger
  single free block.

Heap\_4 is not deterministic but is faster than most standard library
implementations of `malloc()` and `free()`.
