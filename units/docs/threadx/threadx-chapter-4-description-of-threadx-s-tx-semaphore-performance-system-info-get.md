---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-performance-system-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_performance_system_info_get"
summary: "Get semaphore system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get semaphore system performance information

### Prototype

```c
UINT tx_semaphore_performance_system_info_get(
    ULONG *puts,
    ULONG *gets, 
    ULONG *suspensions, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about all the semaphores in the system.

> **Important:** *The ThreadX library and application must be built with* ***TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO*** *defined for this service to return performance information*

### Parameters

- *puts*: Pointer to destination for the total number of put requests performed on all semaphores.
- *gets*: Pointer to destination for the total number of get requests performed on all semaphores.
- *suspensions*: Pointer to destination for the total number of thread suspensions on all semaphores.
- *timeouts*: Pointer to destination for the total number of thread suspension timeouts on all semaphores.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) system performance get.
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

/* Retrieve performance information on all previously created
semaphores. */
status = tx_semaphore_performance_system_info_get(&puts, &gets,
    &suspensions, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
