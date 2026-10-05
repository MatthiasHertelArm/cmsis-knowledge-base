---
id: "threadx-chapter-4-description-of-threadx-s-tx-queue-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_queue_performance_info_get"
summary: "This service retrieves performance information about the specified queue."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-queue-performance-info-get"
license: "MIT"
mode: "V"
---

Get queue performance information

### Prototype

```c
UINT tx_queue_performance_info_get(
    TX_QUEUE *queue_ptr,
    ULONG *messages_sent, 
    ULONG *messages_received,
    ULONG *empty_suspensions, 
    ULONG *full_suspensions,
    ULONG *full_errors, 
    ULONG *timeouts);
```

### Description

This service retrieves performance information about the specified queue.

> **Important:** *The ThreadX library and application must be built with* ***TX_QUEUE_ENABLE_PERFORMANCE_INFO**: *defined for this service to return performance information.*

### Parameters

- *queue_ptr*: Pointer to previously created queue.
- *messages_sent*: Pointer to destination for the number of send requests performed on this queue.
- *messages_received*: Pointer to destination for the number of receive requests performed on this queue.
- *empty_suspensions*: Pointer to destination for the number of queue empty suspensions on this queue.
- *full_suspensions*: Pointer to destination for the number of queue full suspensions on this queue.
- *full_errors*: Pointer to destination for the number of queue full errors on this queue.
- *timeouts*: Pointer to destination for the number of thread suspension timeouts on this queue.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful queue performance get.
- **TX_PTR_ERROR** (0x03) Invalid queue pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_QUEUE my_queue;
ULONG messages_sent;
ULONG messages_received;
ULONG empty_suspensions;
ULONG full_suspensions;
ULONG full_errors;
ULONG timeouts;

/* Retrieve performance information on the previously created
queue. */
status = tx_queue_performance_info_get(&my_queue, &messages_sent,
    &messages_received, &empty_suspensions,
    &full_suspensions, &full_errors, &timeouts);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Queue Services](#Queue_Services)
