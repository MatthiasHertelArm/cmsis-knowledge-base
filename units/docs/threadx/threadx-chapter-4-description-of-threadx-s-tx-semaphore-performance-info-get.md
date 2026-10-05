---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_performance_info_get"
summary: "This service retrieves performance information about the specified semaphore."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-performance-info-get"
license: "MIT"
mode: "V"
---

Get semaphore performance information

### Prototype

```c
UINT tx_semaphore_performance_info_get(
    TX_SEMAPHORE *semaphore_ptr,
    ULONG *puts, 
    ULONG *gets,
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about the specified semaphore.

> **Important:** *The ThreadX library and application must be built with* ***TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO*** *defined for this service to return performance information.*

### Parameters

-  **semaphore_ptr*: Pointer to previously created semaphore.
-  **puts*: Pointer to destination for the number of put requests performed on this semaphore.
-  **gets*: Pointer to destination for the number of get requests performed on this semaphore.
-  **suspensions*: Pointer to destination for the number of thread suspensions on this semaphore.
-  **timeouts*: Pointer to destination for the number of thread suspension timeouts on this semaphore.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful semaphore performance get.
- **TX_PTR_ERROR** (0x03) Invalid semaphore pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_SEMAPHORE my_semaphore;
ULONG puts;
ULONG gets;
ULONG suspensions;
ULONG timeouts;

/* Retrieve performance information on the previously created
semaphore. */
status = tx_semaphore_performance_info_get(&my_semaphore, &puts,
    &gets, &suspensions, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
