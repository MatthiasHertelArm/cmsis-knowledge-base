---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-prioritize"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_prioritize"
summary: "This service places the highest priority thread suspended for memory on this pool at the front of the suspension list. All other threads remain in the same FIFO order they were suspended in."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-prioritize"
license: "MIT"
mode: "V"
---

Prioritize byte pool suspension list

### Prototype

```c
UINT tx_byte_pool_prioritize(TX_BYTE_POOL *pool_ptr);
```
### Description

This service places the highest priority thread suspended for memory on this pool at the front of the suspension list. All other threads remain in the same FIFO order they were suspended in.

### Parameters

- *pool_ptr*: Pointer to a memory pool control block.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory pool prioritize.
- **TX_POOL_ERROR** (0x02) Invalid memory pool pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_BYTE_POOL my_pool;
UINT status;

/* Ensure that the highest priority thread will receive
the next free memory from this pool. */
status = tx_byte_pool_prioritize(&my_pool);

/* If status equals TX_SUCCESS, the highest priority
suspended thread is at the front of the list. The
next tx_byte_release call will wake up this thread,
if there is enough memory to satisfy its request. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
