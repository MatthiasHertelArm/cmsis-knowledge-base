---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-performance-system-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_performance_system_info_get"
summary: "Get queue system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get queue system performance information

### Prototype

```c
UINT tx_queue_performance_system_info_get(
    ULONG *messages_sent,
    ULONG *messages_received, 
    ULONG *empty_suspensions,
    ULONG *full_suspensions, 
    ULONG *full_errors,
    ULONG *timeouts);
```

### Description

This service retrieves performance information about all the queues in the system.

> **Important:** *The ThreadX library and application must be built with* ***TX_QUEUE_ENABLE_PERFORMANCE_INFO*** *defined for this service to return performance
information.*

### Parameters

- *messages_sent*: Pointer to destination for the total number of send requests performed on all queues.
- *messages_received*: Pointer to destination for the total number of receive requests performed on all queues.
- *empty_suspensions*: Pointer to destination for the total number of queue empty suspensions on all queues.
- *full_suspensions*: Pointer to destination for the total number of queue full suspensions on all queues.
- *full_errors*: Pointer to destination for the total number of queue full errors on all queues.
- *timeouts*: Pointer to destination for the total number of thread suspension timeouts on all queues.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful queue system performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG messages_sent;
ULONG messages_received;
ULONG empty_suspensions;
ULONG full_suspensions;
ULONG full_errors;
ULONG timeouts;

/* Retrieve performance information on all previously created
queues. */
status = tx_queue_performance_system_info_get(&messages_sent,
    &messages_received, &empty_suspensions,
    &full_suspensions, &full_errors, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Queue Services](#Queue_Services)
