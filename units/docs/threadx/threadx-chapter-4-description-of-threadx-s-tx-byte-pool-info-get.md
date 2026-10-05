---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_info_get"
summary: "This service retrieves information about the specified memory byte pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about byte pool

### Prototype

```c
UINT tx_byte_pool_info_get(
    TX_BYTE_POOL *pool_ptr, 
    CHAR **name,
    ULONG *available, 
    ULONG *fragments,
    TX_THREAD **first_suspended,
    ULONG *suspended_count,
    TX_BYTE_POOL **next_pool);
```

### Description

This service retrieves information about the specified memory byte pool.

### Parameters

- *pool_ptr*: Pointer to previously created memory pool.
- *name*: Pointer to destination for the pointer to the byte pool's name.
- *available*: Pointer to destination for the number of available bytes in the pool.
- *fragments*: Pointer to destination for the total number of memory fragments in the byte pool.
- *first_suspended*: Pointer to destination for the pointer to the thread that is first on the suspension list of this byte pool.
- *suspended_count*: Pointer to destination for the number of threads currently suspended on this byte pool.
- *next_pool*: Pointer to destination for the pointer of the next created byte pool.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful pool information retrieve.
- **TX_POOL_ERROR** (0x02) Invalid memory pool pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_BYTE_POOL my_pool;
CHAR *name;
ULONG available;
ULONG fragments;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_BYTE_POOL *next_pool;
UINT status;

/* Retrieve information about the previously created
block pool "my_pool." */
status = tx_byte_pool_info_get(&my_pool, &name,
  &available, &fragments,
  &first_suspended, &suspended_count,
  &next_pool);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
