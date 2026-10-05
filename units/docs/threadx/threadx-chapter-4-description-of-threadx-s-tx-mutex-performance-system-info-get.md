---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-performance-system-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_performance_system_info_get"
summary: "Get mutex system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get mutex system performance information

### Prototype

```c
UINT tx_mutex_performance_system_info_get(
    ULONG *puts, 
    ULONG *gets,
    ULONG *suspensions, 
    ULONG *timeouts,
    ULONG *inversions, 
    ULONG *inheritances);
```

### Description

This service retrieves performance information about all the mutexes in the system.

> **Important:** *The ThreadX library and application must be built with* **TX_MUTEX_ENABLE_PERFORMANCE_INFO** *defined for this service to return performance information.*

### Parameters

- *puts*: Pointer to destination for the total number of put requests performed on all mutexes.
- *gets*: Pointer to destination for the total number of get requests performed on all mutexes.
- *suspensions*: Pointer to destination for the total number of thread mutex get suspensions on all mutexes.
- *timeouts*: Pointer to destination for the total number of mutex get suspension timeouts on all mutexes.
- *inversions*: Pointer to destination for the total number of thread priority inversions on all mutexes.
- *inheritances*: Pointer to destination for the total number of thread priority inheritance operations on all mutexes.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex system performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG puts;
ULONG gets;
ULONG suspensions;
ULONG timeouts;
ULONG inversions;
ULONG inheritances;

/* Retrieve performance information on all previously created
mutexes. */
status = tx_mutex_performance_system_info_get(&puts, &gets,
    &suspensions, &timeouts,
    &inversions, &inheritances);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Mutex Services](#Mutex_Services)
