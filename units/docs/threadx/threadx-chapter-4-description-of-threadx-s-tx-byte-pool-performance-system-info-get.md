---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-pool-performance-system-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_pool_performance_system_info_get"
summary: "Get byte pool system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-pool-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get byte pool system performance information

### Prototype

```c
UINT tx_byte_pool_performance_system_info_get(
    ULONG *allocates,
    ULONG *releases, 
    ULONG *fragments_searched, 
    ULONG *merges,
    ULONG *splits, 
    ULONG *suspensions, 
    ULONG *timeouts);
```
### Description

This service retrieves performance information about all memory byte pools in the system.

> **Important:** *The ThreadX library and application must be built with* **TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- *allocates*: Pointer to destination for the number of allocate requests performed on this pool.
- *releases*: Pointer to destination for the number of release requests performed on this pool.
- *fragments_searched*: Pointer to destination for the total number of internal memory fragments searched during allocation requests on all byte pools.
- *merges*: Pointer to destination for the total number of internal memory blocks merged during allocation requests on all byte pools.
- *splits*: Pointer to destination for the total number of internal memory blocks split (fragments) created during allocation requests on all byte pools.
- *suspensions*: Pointer to destination for the total number of thread allocation suspensions on all byte pools.
- *timeouts*: Pointer to destination for the total number of allocate suspension timeouts on all byte pools.

> **Note:** *Supplying a TX_NULL for any parameter indicates the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful byte pool performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

 Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG fragments_searched;
ULONG merges;
ULONG splits;
ULONG allocates;
ULONG releases;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on all byte pools in the
system. */
status =
tx_byte_pool_performance_system_info_get(&fragments_searched,
  &merges, &splits, &allocates, &releases,
  &suspensions, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
