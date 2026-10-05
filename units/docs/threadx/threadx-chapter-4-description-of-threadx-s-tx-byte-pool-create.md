---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_create"
summary: "This service creates a memory byte pool in the area specified. Initially the pool consists of basically one very large free block. However, the pool is broken into smaller blocks as allocations are made."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-create"
license: "MIT"
mode: "V"
---

Create memory pool of bytes

### Prototype

```c
UINT tx_byte_pool_create(
    TX_BYTE_POOL *pool_ptr,
    CHAR *name_ptr, 
    VOID *pool_start,
    ULONG pool_size);
```

### Description

This service creates a memory byte pool in the area specified. Initially the pool consists of basically one very large free block. However, the pool is broken into smaller blocks as allocations are made.

### Parameters

- *pool_ptr*: Pointer to a memory pool control block.
- *name_ptr*: Pointer to the name of the memory pool.
- *pool_start*: Starting address of the memory pool. The starting address must be aligned to the size of the ULONG data type.
- *pool_size*: Total number of bytes available for the memory pool.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory pool creation.
- **TX_POOL_ERROR** (0x02) Invalid memory pool pointer. Either the pointer is NULL or the pool is already created.
- **TX_PTR_ERROR** (0x03) Invalid starting address of the pool.
- **TX_SIZE_ERROR** (0x05) Size of pool is invalid.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_BYTE_POOL my_pool;
UINT status;
/* Create a memory pool whose total size is 2000 bytes
starting at address 0x500000. */
status = tx_byte_pool_create(&my_pool, "my_pool_name",
    (VOID *) 0x500000, 2000);

/* If status equals TX_SUCCESS, my_pool is available for
allocating memory. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
