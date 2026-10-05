---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-delete"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_delete"
summary: "This service deletes the specified memory byte pool. All threads suspended waiting for memory from this pool are resumed and given a TX_DELETED return status."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-delete"
license: "MIT"
mode: "V"
---

Delete memory byte pool

### Prototype

```c
UINT tx_byte_pool_delete(TX_BYTE_POOL *pool_ptr);
```

### Description

This service deletes the specified memory byte pool. All threads suspended waiting for memory from this pool are resumed and given a **TX_DELETED** return status.

> **Important:** *It is the application's responsibility to manage the memory area associated with the pool, which is available after this service completes. In addition, the application must prevent use of a deleted pool or memory previously allocated from it.*

### Parameters

- *pool_ptr*: Pointer to a previously created memory pool.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory pool deletion.
- **TX_POOL_ERROR** (0x02) Invalid memory pool pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
TX_BYTE_POOL my_pool;
UINT status;
/* Delete entire memory pool. Assume that the pool has already
been created with a call to tx_byte_pool_create. */
status = tx_byte_pool_delete(&my_pool);

/* If status equals TX_SUCCESS, memory pool is deleted. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
