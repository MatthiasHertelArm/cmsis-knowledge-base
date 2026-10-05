---
id: "frb-3-heap-memory-management-3-2-6-initialising-heap-5-the-vportdefin"
type: "concept"
domain: "rtos"
title: "3 Heap Memory Management: 3.2 Example Memory Allocation Schemes / 3.2.6 Initialising heap\\_5: The vPortDefineHeapRegions() API Function"
summary: "Part of: 3.2 Example Memory Allocation Schemes"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch03.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch03.md#3-2-6-initialising-heap-5-the-vportdefineheapregions-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 3.2 Example Memory Allocation Schemes_

`vPortDefineHeapRegions()` initialises heap\_5 by specifying the start
address and size of each separate memory area that makes up the heap
managed by heap\_5. Heap\_5 is the only provided heap allocation scheme
that requires explicit initialisation and can't be used until after the
call to `vPortDefineHeapRegions()`. That means kernel objects, such as
tasks, queues, and semaphores, cannot be created dynamically until after
the call to `vPortDefineHeapRegions()`.





```c
void vPortDefineHeapRegions( const HeapRegion_t * const pxHeapRegions );
```
***Listing 3.1*** *The vPortDefineHeapRegions() API function prototype*


`vPortDefineHeapRegions()` takes an array of `HeapRegion_t` structures as
its only parameter. Each structure defines the start address and size of
a memory block that will become part of the heap—the whole array of
structures defines the entire heap space.





```c
typedef struct HeapRegion
{
    /* The start address of a block of memory that will be part of the heap.*/
    uint8_t *pucStartAddress;

    /* The size of the block of memory in bytes. */
    size_t xSizeInBytes;

} HeapRegion_t;
```
***Listing 3.2*** *The HeapRegion\_t structure*


**Parameters:**

- `pxHeapRegions`

  A pointer to the start of an array of `HeapRegion_t` structures.
  Each structure defines the start address and size of a memory block that
  will become part of the heap.

  The `HeapRegion_t` structures in the array must be ordered by start
  address; the `HeapRegion_t` structure that describes the memory area with
  the lowest start address must be the first structure in the array, and
  the `HeapRegion_t` structure that describes the memory area with the
  highest start address must be the last structure in the array.

  Mark the end of the array with a `HeapRegion_t` structure that has its
  `pucStartAddress` member set to `NULL`.

By way of example, consider the hypothetical memory map shown in Figure
3.4 **A** which contains three separate blocks of RAM: RAM1, RAM2
and RAM3. It is assumed executable code is placed in read-only memory,
which is not shown.




* * *

***Figure 3.4*** *Memory Map*
* * *

Listing 3.3 shows an array of `HeapRegion_t` structures that together
describe the three blocks of RAM in their entirety.





```c
/* Define the start address and size of the three RAM regions. */
#define RAM1_START_ADDRESS ( ( uint8_t * ) 0x00010000 )
#define RAM1_SIZE ( 64 * 1024 )

#define RAM2_START_ADDRESS ( ( uint8_t * ) 0x00020000 )
#define RAM2_SIZE ( 32 * 1024 )

#define RAM3_START_ADDRESS ( ( uint8_t * ) 0x00030000 )
#define RAM3_SIZE ( 32 * 1024 )

/* Create an array of HeapRegion_t definitions, with an index for each
   of the three RAM regions, and terminate the array with a HeapRegion_t
   structure containing a NULL address. The HeapRegion_t structures must
   appear in start address order, with the structure that contains the
   lowest start address appearing first. */
const HeapRegion_t xHeapRegions[] =
{
    { RAM1_START_ADDRESS, RAM1_SIZE },
    { RAM2_START_ADDRESS, RAM2_SIZE },
    { RAM3_START_ADDRESS, RAM3_SIZE },
    { NULL,               0         } /* Marks the end of the array. */
};

int main( void )
{
    /* Initialize heap_5. */
    vPortDefineHeapRegions( xHeapRegions );

    /* Add application code here. */
}
```
***Listing 3.3*** *An array of HeapRegion\_t structures that together describe the 3 regions of RAM in their entirety*


Although Listing 3.3 correctly describes the RAM, it does not demonstrate a
usable example because it allocates all the RAM to the heap, leaving no
RAM free for use by other variables.

The linking phase of the build process allocates a RAM address to each
variable. The RAM available for use by the linker is normally described
by a linker configuration file, such as a linker script. In Figure 3.4
**B** it is assumed the linker script included information on
RAM1, but did not include information on RAM2 or RAM3. As a result, the
linker placed variables in RAM1, leaving only the portion of RAM1 above
address 0x0001nnnn available for use by heap\_5. The actual value of
0x0001nnnn depends on the combined size of all the variables included in
the application. The linker has left all of RAM2 and all of RAM3 unused,
leaving the whole of RAM2 and the whole of RAM3 available for use by
heap\_5.

The code shown in Listing 3.3 would cause the RAM allocated to heap\_5
below address 0x0001nnnn to overlap the RAM used to hold variables.
If you set the start address of the first `HeapRegion_t` structure within the
`xHeapRegions[]` array to 0x0001nnnn, rather than a start address of
0x00010000, the heap will not overlap with RAM used by the linker.
However, that is not a recommended solution because:

- The start address might not be easy to determine.
- The amount of RAM used by the linker might change in future builds,
  which would make an update to the start address used in the
  `HeapRegion_t` structure necessary.
- The build tools will not know, and therefore cannot warn the
  application writer, if the RAM used by the linker and the RAM used
  by heap\_5 overlap.

Listing 3.4 demonstrates a more convenient and maintainable example. It
declares an array called `ucHeap`. `ucHeap` is a normal variable, so it
becomes part of the data allocated to RAM1 by the linker. The first
`HeapRegion_t` structure in the `xHeapRegions` array describes the start
address and size of `ucHeap`, so `ucHeap` becomes part of the memory managed
by heap\_5. The size of `ucHeap` can be increased until the RAM used by the
linker consumes all of RAM1, as shown in Figure 3.4 **C**.




```c
/* Define the start address and size of the two RAM regions not used by
   the linker. */
#define RAM2_START_ADDRESS ( ( uint8_t * ) 0x00020000 )
#define RAM2_SIZE ( 32 * 1024 )

#define RAM3_START_ADDRESS ( ( uint8_t * ) 0x00030000 )
#define RAM3_SIZE ( 32 * 1024 )

/* Declare an array that will be part of the heap used by heap_5. The
   array will be placed in RAM1 by the linker. */
#define RAM1_HEAP_SIZE ( 30 * 1024 )
static uint8_t ucHeap[ RAM1_HEAP_SIZE ];

/* Create an array of HeapRegion_t definitions. Whereas in Listing 3.3 the
   first entry described all of RAM1, so heap_5 will have used all of
   RAM1, this time the first entry only describes the ucHeap array, so
   heap_5 will only use the part of RAM1 that contains the ucHeap array.
   The HeapRegion_t structures must still appear in start address order,
   with the structure that contains the lowest start address appearing first. */

const HeapRegion_t xHeapRegions[] =
{
    { ucHeap,             RAM1_HEAP_SIZE },
    { RAM2_START_ADDRESS, RAM2_SIZE },
    { RAM3_START_ADDRESS, RAM3_SIZE },
    { NULL,               0 }           /* Marks the end of the array. */
};
```
***Listing 3.4*** *An array of HeapRegion\_t structures that describe all of RAM2, all of RAM3, but only part of RAM1*


The advantages of the technique demonstrated in Listing 3.4 include:

- It is not necessary to use a hard-coded start address.
- The address used in the `HeapRegion_t` structure will be set
  automatically by the linker, so it will always be correct, even if the
  amount of RAM used by the linker changes in future builds.
- It is impossible for RAM allocated to heap\_5 to overlap data placed
  into RAM1 by the linker.
- The application will not link if `ucHeap` is too big.
