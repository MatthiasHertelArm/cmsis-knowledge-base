---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-allocate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_allocate"
summary: "This service allocates a fixed-size memory block from the specified memory pool. The actual size of the memory block is determined during memory pool creation."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-allocate"
license: "MIT"
mode: "V"
---

Allocate fixed-size block of memory

### Prototype

```c
UINT tx_block_allocate(
    TX_BLOCK_POOL *pool_ptr, 
    VOID **block_ptr,
    ULONG wait_option);
```

### Description

This service allocates a fixed-size memory block from the specified memory pool. The actual size of the memory block is determined during memory pool creation.

> **Important:** *It is important to ensure application code does not write outside the allocated memory block. If this happens, the behavior is undefined. Likewise, if the destination is not large enough, the behavior is undefined. That said, a typical consequence is memory corruption of an adjacent (usually subsequent) memory area. The results are unpredictable and often fatal!*

### Parameters

- *pool_ptr*: 
Pointer to a previously created memory block pool.
- *block_ptr*: 
Pointer to a destination block pointer. On successful allocation, the address of the allocated memory block is placed where this parameter points.
- *wait_option*: 
Defines how the service behaves if there are no memory blocks available. The wait options are defined as follows:
  - **TX_NO_WAIT** (0x00000000) - Selecting **TX_NO_WAIT** results in an immediate return from this service regardless if it was successful or not. *This is the only valid option if the service is called from a non-thread; e.g., Initialization, timer, or ISR*.
  - **TX_WAIT_FOREVER** (0xFFFFFFF) - Selecting **TX_WAIT_FOREVER** causes the calling thread to suspend indefinitely until a memory block is available.
  - *timeout value* (0x00000001 through 0xFFFFFFFE) - Selecting a numeric value (1-0xFFFFFFFE) specifies the maximum number of timer-ticks to stay suspended while waiting for a memory block.

### Return Values

- **TX_SUCCESS**	(0x00)	Successful memory block allocation.
- **TX_DELETED**	(0x01)	Memory block pool was deleted while thread was suspended.
- **TX_NO_MEMORY**	(0x10)	Service was unable to allocate a block of memory within the specified time to wait.
- **TX_WAIT_ABORTED**	(0x1A)	Suspension was aborted by another thread, timer or ISR.
- **TX_POOL_ERROR**	(0x02)	Invalid memory block pool pointer.
- **TX_WAIT_ERROR**	(0x04)	A wait option other than TX_NO_WAIT was specified on a call from a nonthread.
- **TX_PTR_ERROR**	(0x03)	Invalid pointer to destination pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_BLOCK_POOL my_pool;
unsigned char *memory_ptr;

UINT status;

/* Allocate a memory block from my_pool. Assume that the pool has
already been created with a call to tx_block_pool_create. */

status = tx_block_allocate(&my_pool, (VOID **) &memory_ptr,
  TX_NO_WAIT);

/* If status equals TX_SUCCESS, memory_ptr contains the address of
the allocated block of memory. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
