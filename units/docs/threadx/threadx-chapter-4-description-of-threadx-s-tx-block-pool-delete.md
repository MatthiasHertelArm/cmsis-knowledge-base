---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-pool-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_pool_delete"
summary: "This service deletes the specified block-memory pool. All threads suspended waiting for a memory block from this pool are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-pool-delete"
license: "MIT"
mode: "V"
---

Delete memory block pool

### Prototype

```c
UINT tx_block_pool_delete(TX_BLOCK_POOL *pool_ptr);
```

### Description

This service deletes the specified block-memory pool. All threads suspended waiting for a memory block from this pool are resumed and given a **TX_DELETED** return status.

> **Note:** *It is the application's responsibility to manage the memory area associated with the pool, which is available after this service completes. In addition, the application must prevent the use of a deleted pool or its former memory blocks.*

### Parameters

- *pool_ptr*: Pointer to a previously created memory block pool.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory block pool deletion.
- **TX_POOL_ERROR** (0x02) Invalid memory block pool pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_BLOCK_POOL my_pool;

UINT           status;

/* Delete entire memory block
pool. Assume that the pool has already been created with a call to
tx_block_pool_create. */
status = tx_block_pool_delete(&my_pool);

/* If status equals TX_SUCCESS, the memory block pool is deleted.*/
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
