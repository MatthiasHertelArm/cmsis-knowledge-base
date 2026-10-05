---
id: "threadx-chapter-4-description-of-threadx-s-tx-block-pool-performance-system-info-ge"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_block_pool_performance_system_info_get"
summary: "Get block pool system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-block-pool-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get block pool system performance information

### Prototype

```c
UINT tx_block_pool_performance_system_info_get(
    ULONG *allocates,
    ULONG *releases, 
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about all memory block pools in the application.

> **Important:** *The ThreadX library and application must be built with* **TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- **allocates**: Pointer to destination for the total number of allocate requests performed on all block pools.
- **releases**: Pointer to destination for the total number of release requests performed on all block pools.
- **suspensions**: Pointer to destination for the total number of thread allocation suspensions on all block pools.
- **timeouts**: Pointer to destination for the total number of allocate suspension timeouts on all block pools.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful block pool system performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG       allocates;
ULONG       releases;
ULONG       suspensions;
ULONG       timeouts;

/* Retrieve performance information on all the block pools in
the system. */
status = tx_block_pool_performance_system_info_get(&allocates,
    &releases,&suspensions, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
