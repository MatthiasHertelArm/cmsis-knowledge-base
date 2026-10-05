---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-release"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_release"
summary: "This service releases a previously allocated block back to its associated memory pool. If there are one or more threads suspended waiting for memory blocks from this pool, the first thread suspended is given this memory block and resumed."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-release"
license: "MIT"
mode: "V"
---

Release fixed-size block of memory

### Prototype

```c
UINT tx_block_release(VOID *block_ptr);
```

### Description

This service releases a previously allocated block back to its associated memory pool. If there are one or more threads suspended waiting for memory blocks from this pool, the first thread suspended is given this memory block and resumed.

> **Note:** *The application may want to clear the memory block before releasing it to prevent data leaks.*

> **Important:** *The application must prevent using a memory block area after it has been released back to the pool.*

### Parameters

- *block_ptr*: Pointer to the previously allocated memory block.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory block release.
- **TX_PTR_ERROR** (0x03) Invalid pointer to memory block.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

Yes

### Example

```c
TX_BLOCK_POOL my_pool;
unsigned char *memory_ptr;
UINT status;

/* Release a memory block back to my_pool. Assume that the
pool has been created and the memory block has been
allocated. */
status = tx_block_release((VOID *) memory_ptr);

/* If status equals TX_SUCCESS, the block of memory pointed
to by memory_ptr has been returned to the pool. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
