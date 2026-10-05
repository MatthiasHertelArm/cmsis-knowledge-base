---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-pool-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_pool_performance_info_get"
summary: "This service retrieves performance information about the specified memory block pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-pool-performance-info-get"
license: "MIT"
mode: "V"
---

Get block pool performance information

### Prototype

```c
UINT tx_block_pool_performance_info_get(
    TX_BLOCK_POOL *pool_ptr,
    ULONG *allocates, 
    ULONG *releases,
    ULONG *suspensions, 
    ULONG *timeouts));
```

### Description

This service retrieves performance information about the specified memory block pool.

> **Important:** *The ThreadX library and application must be built with* **TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- **pool_ptr**: Pointer to previously created memory block pool.
- **allocates**: Pointer to destination for the number of allocate requests performed on this pool.
- **releases**: Pointer to destination for the number of release requests performed on this pool.
- **suspensions**: Pointer to destination for the number of thread allocation suspensions on this pool.
- **timeouts**: Pointer to destination for the number of allocate suspension timeouts on this pool.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS**	(0x00)	Successful block pool performance get.
- **TX_PTR_ERROR**	(0x03)	Invalid block pool pointer.
- **TX_FEATURE_NOT_ENABLED**	(0xFF)	The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_BLOCK_POOL my_pool;
ULONG allocates;
ULONG releases;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on the previously created block
pool. */
status = tx_block_pool_performance_info_get(&my_pool, &allocates,
  &releases,
  &suspensions,
  &timeouts);

/* If status is TX_SUCCESS the performance information was successfully retrieved. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
