---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_performance_info_get"
summary: "This service retrieves performance information about the specified memory byte pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-performance-info-get"
license: "MIT"
mode: "V"
---

Get byte pool performance information

### Prototype

```c
UINT tx_byte_pool_performance_info_get(
    TX_BYTE_POOL *pool_ptr,
    ULONG *allocates, 
    ULONG *releases,
    ULONG *fragments_searched, 
    ULONG *merges, 
    ULONG *splits,
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about the specified memory byte pool.

> **Important:** *The ThreadX library and application must be built with* **TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- *pool_ptr*: Pointer to previously created memory byte pool.
- *allocates*: Pointer to destination for the number of allocate requests performed on this pool.
- *releases*: Pointer to destination for the number of release requests performed on this pool.
- *fragments_searched*: Pointer to destination for the number of internal memory fragments searched during allocation requests on this pool.
- *merges*: Pointer to destination for the number of internal memory blocks merged during allocation requests on this pool.
- *splits*: Pointer to destination for the number of internal memory blocks split (fragments) created during allocation requests on this pool.
- *suspensions*: Pointer to destination for the number of thread allocation suspensions on this pool.
- *timeouts*: Pointer to destination for the number of allocate suspension timeouts on this pool.

> **Note:** *Supplying a TX_NULL for any parameter indicates the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful byte pool performance get.
- **TX_PTR_ERROR** (0x03) Invalid byte pool pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_BYTE_POOL my_pool;
ULONG fragments_searched;
ULONG merges;
ULONG splits;
ULONG allocates;
ULONG releases;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on the previously created byte
pool. */
status = tx_byte_pool_performance_info_get(&my_pool,
  &fragments_searched,
  &merges, &splits,
  &allocates, &releases,
  &suspensions,&timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```
### See Also

- [Block Pool Services](#Block_Pool_Services)
