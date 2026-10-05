---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-pool-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_pool_create"
summary: "This service creates a pool of fixed-size memory blocks. The memory area specified is divided into as many fixed-size memory blocks as possible using the formula:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-pool-create"
license: "MIT"
mode: "V"
---

Create pool of fixed-size memory blocks

### Prototype

```c
UINT tx_block_pool_create(
    TX_BLOCK_POOL pool_ptr,
    CHAR name_ptr, 
    ULONG block_size,
    VOID pool_start, 
    ULONG pool_size);
```

### Description

This service creates a pool of fixed-size memory blocks. The memory area specified is divided into as many fixed-size memory blocks as possible using the formula:

**total blocks** = (**total bytes**) /
(**block size** + sizeof(void *))

> **Note:** *Each memory block contains one pointer of overhead that is invisible to the user and is represented by the "sizeof(void *)" in the preceding formula.*

### Parameters

- **pool_ptr**: Pointer to a memory block pool control block.
- **name_ptr**: Pointer to the name of the memory block pool.
- **block_size**: Number of bytes in each memory block.
- **pool_start**: Starting address of the memory block pool. The starting address must be aligned to the size of the ULONG data type..
- **pool_size**: Total number of bytes available for the memory block pool.

### Return Values

- **TX_SUCCESS**	(0x00)	Successful memory block pool creation.
- **TX_POOL_ERROR**	(0x02)	Invalid memory block pool pointer. Either the pointer is NULL or the pool is already created.
- **TX_PTR_ERROR**	(0x03)	Invalid starting address of the pool.
- **TX_CALLER_ERROR**	(0x13)	Invalid caller of this service.
- **TX_SIZE_ERROR**	(0x05)	Size of pool is invalid.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_BLOCK_POOL my_pool;

UINT status;

/* Create a memory pool whose total size is 1000 bytes starting at
address 0x100000. Each block in this pool is defined to be 50 bytes
long. */
status = tx_block_pool_create(&my_pool, "my_pool_name",
  50, (VOID *) 0x100000, 1000);

/* If status equals TX_SUCCESS, my_pool contains 18 memory blocks
of 50 bytes each. The reason there are not 20 blocks in the pool is
because of the one overhead pointer associated with each block. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
