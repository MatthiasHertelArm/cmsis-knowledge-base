---
id: "frb-3-heap-memory-management-3-3-1-defining-the-heap-start-address"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.3 Heap Related Utility Functions and Macros / 3.3.1 Defining the Heap Start Address"
summary: "Part of: 3.3 Heap Related Utility Functions and Macros"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-3-1-defining-the-heap-start-address"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.3 Heap Related Utility Functions and Macros_

Heap\_1, heap\_2 and heap\_4 allocate memory from a statically allocated
array dimensioned by `configTOTAL_HEAP_SIZE`. This section refers to these
allocation schemes collectively as heap\_n.

Sometimes the heap needs to be placed at a specific memory address. For
example, the stack allocated to a dynamically created task comes from
the heap, so it might be necessary to locate the heap in fast internal
memory rather than slow external memory. (See the sub-section Placing
Task Stacks in Fast Memory below for another method of allocating task
stacks in fast memory). The `configAPPLICATION_ALLOCATED_HEAP`
compile-time configuration constant enables the application to declare
the array in place of the declaration that would otherwise be in the
heap\_n.c source file. Declaring the array in the application code
enables the application writer to specify its start address.

If `configAPPLICATION_ALLOCATED_HEAP` is set to 1 in FreeRTOSConfig.h,
the application that uses FreeRTOS must allocate a `uint8_t` array
called `ucHeap` and dimensioned by the `configTOTAL_HEAP_SIZE` constant.

The syntax required to place a variable at a specific memory address is
dependent on the compiler in use, so refer to your compiler's
documentation. Examples for two compilers follow:

- Listing 3.5 shows the syntax required by the GCC compiler to declare
  the array and place the array in a memory section called `.my_heap`.
- Listing 3.6 shows the syntax required by the IAR compiler to declare
  the array and place the array at the absolute memory address
  0x20000000.





```c
uint8_t ucHeap[ configTOTAL_HEAP_SIZE ] __attribute__ ( ( section( ".my_heap" ) ) );
```
***Listing 3.5*** *Using GCC syntax to declare the array that will be used by heap\_4, and place the array in a memory section named .my\_heap*






```c
uint8_t ucHeap[ configTOTAL_HEAP_SIZE ] @ 0x20000000;
```
***Listing 3.6*** *Using IAR syntax to declare the array that will be used by heap\_4, and place the array at the absolute address 0x20000000*
