---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-pool-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_pool_info_get"
summary: "This service retrieves information about the specified block memory pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-pool-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about block pool

### Prototype

```c
UINT tx_block_pool_info_get(
    TX_BLOCK_POOL *pool_ptr, 
    CHAR **name,
    ULONG *available, 
    ULONG *total_blocks,
    TX_THREAD **first_suspended,
    ULONG *suspended_count,
    TX_BLOCK_POOL **next_pool);
```

### Description

This service retrieves information about the specified block memory pool.

### Parameters

- **pool_ptr**: Pointer to previously created memory block pool.
- **name**: Pointer to destination for the pointer to the block pool's name.
- **available**: Pointer to destination for the number of available blocks in the block pool.
- **total_blocks**: Pointer to destination for the total number of blocks in the block pool.
- **first_suspended**: Pointer to destination for the pointer to the thread that is first on the suspension list of this block pool.
- **suspended_count**: Pointer to destination for the number of threads currently suspended on this block pool.
- **next_pool**: Pointer to destination for the pointer of the next created block pool.

> **Note:** *Supplying a TX_NULL for any parameter indicates the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful block pool information retrieve.
- **TX_POOL_ERROR** (0x02) Invalid memory block pool pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_BLOCK_POOL my_pool;
CHAR *name;
ULONG available;
ULONG total_blocks;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_BLOCK_POOL *next_pool;
UINT status;

/* Retrieve information about the previously created
block pool "my_pool." */
status = tx_block_pool_info_get(&my_pool, &name,
  &available,&total_blocks,
  &first_suspended, &suspended_count,
  &next_pool);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
