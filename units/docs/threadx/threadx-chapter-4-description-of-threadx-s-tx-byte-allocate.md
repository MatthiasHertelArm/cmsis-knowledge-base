---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-allocate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_allocate"
summary: "This service allocates the specified number of bytes from the specified memory byte pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-allocate"
license: "MIT"
mode: "V"
---

Allocate bytes of memory

### Prototype

```c
UINT tx_byte_allocate(
    TX_BYTE_POOL *pool_ptr,
    VOID **memory_ptr, 
    ULONG memory_size,
    ULONG wait_option);
```

### Description

This service allocates the specified number of bytes from the specified memory byte pool.

> **Important:** *It is important to ensure application code does not write outside the allocated memory block. If this happens, the behavior is undefined. Likewise, if the destination is not large enough, the behavior is undefined. That said, a typical consequence is memory corruption of an adjacent (usually subsequent) memory area. The results are unpredictable and often fatal!*

> **Note:** *The performance of this service is a function of the block size and the amount of fragmentation in the pool. Hence, this service should not be used during time-critical threads of execution.*

### Parameters

- **pool_ptr**: Pointer to a previously created memory pool.
- **memory_ptr**: Pointer to a destination memory pointer. On successful allocation, the address of the allocated memory area is placed where this parameter points to.
- **memory_size**: Number of bytes requested.
- **wait_option**: Defines how the service behaves if there is not enough memory available. The wait options are defined as follows:
    - **TX_NO_WAIT**: (0x00000000)
    - **TX_WAIT_FOREVER**: (0xFFFFFFFF)
    - timeout value: (0x00000001 through 0xFFFFFFFE)

    Selecting TX_NO_WAIT results in an immediate return from this service regardless of whether or not it was successful. *This is the only valid option if the service is called from initialization.*

    Selecting TX_WAIT_FOREVER causes the calling thread to suspend indefinitely until enough memory is available.

    Selecting a numeric value (1-0xFFFFFFFE) specifies the maximum number of timer-ticks to stay suspended while waiting for the memory.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory allocation.
- **TX_DELETED** (0x01) Memory pool was deleted while thread was suspended.
- **TX_NO_MEMORY** (0x10) Service was unable to allocate the memory within the specified time to wait.
- **TX_WAIT_ABORTED** (0x1A) Suspension was aborted by another thread, timer, or ISR.
- **TX_POOL_ERROR** (0x02) Invalid memory pool pointer.
- **TX_PTR_ERROR** (0x03) Invalid pointer to destination pointer.
- **TX_SIZE_ERROR** (0X05) Requested size is zero or larger than the pool.
- **TX_WAIT_ERROR** (0x04) A wait option other than TX_NO_WAIT was specified on a call from a nonthread.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

Yes

### Example
```c
TX_BYTE_POOL my_pool;
unsigned char*memory_ptr;
UINT status;
/* Allocate a 112 byte memory area from my_pool. Assume
that the pool has already been created with a call to
tx_byte_pool_create. */
status = tx_byte_allocate(&my_pool, (VOID **) &memory_ptr,
    112, TX_NO_WAIT);

/* If status equals TX_SUCCESS, memory_ptr contains the
address of the allocated memory area. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
