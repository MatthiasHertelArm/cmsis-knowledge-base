---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_performance_info_get"
summary: "This service retrieves performance information about the specified mutex."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-performance-info-get"
license: "MIT"
mode: "V"
---

Get mutex performance information

### Prototype

```c
UINT tx_mutex_performance_info_get(
    TX_MUTEX *mutex_ptr, 
    ULONG *puts,
    ULONG *gets, 
    ULONG *suspensions, 
    ULONG *timeouts,
    ULONG *inversions, 
    ULONG *inheritances);
```

### Description

This service retrieves performance information about the specified mutex.

> **Important:** *The ThreadX library and application must be built with* ***TX_MUTEX_ENABLE_PERFORMANCE_INFO*** *defined for this service to return performance information.*

### Parameters

- *mutex_ptr*: Pointer to previously created mutex.
- *puts*: Pointer to destination for the number of put requests performed on this mutex.
- *gets*: Pointer to destination for the number of get requests performed on this mutex.
- *suspensions*: Pointer to destination for the number of thread mutex get suspensions on this mutex.
- *timeouts*: Pointer to destination for the number of mutex get suspension timeouts on this mutex.
- *inversions*: Pointer to destination for the number of thread priority inversions on this mutex.
- *inheritances*: Pointer to destination for the number of thread priority inheritance operations on this mutex.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex performance get.
- **TX_PTR_ERROR** (0x03) Invalid mutex pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_MUTEX my_mutex;
ULONG puts;
ULONG gets;
ULONG suspensions;
ULONG timeouts;
ULONG inversions;
ULONG inheritances;

/* Retrieve performance information on the previously created
mutex. */
status = tx_mutex_performance_info_get(&my_mutex_ptr, &puts, &gets,
    &suspensions, &timeouts, &inversions, &inheritances);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Mutex Services](#Mutex_Services)
