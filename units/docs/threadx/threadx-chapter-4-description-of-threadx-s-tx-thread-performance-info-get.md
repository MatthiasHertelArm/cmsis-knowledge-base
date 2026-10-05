---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-performance-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_performance_info_get"
summary: "This service retrieves performance information about the specified thread."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-performance-info-get"
license: "MIT"
mode: "V"
---

Get thread performance information

### Prototype

```c
UINT tx_thread_performance_info_get(
    TX_THREAD *thread_ptr,
    LONG *resumptions, 
    ULONG *suspensions,
    ULONG *solicited_preemptions, 
    ULONG *interrupt_preemptions,
    ULONG *priority_inversions, 
    ULONG *time_slices,
    ULONG *relinquishes, 
    ULONG *timeouts, 
    ULONG *wait_aborts,
    TX_THREAD **last_preempted_by);
```

### Description

This service retrieves performance information about the specified thread.

> **Important:** *The ThreadX library and application must be built with* ***TX_THREAD_ENABLE_PERFORMANCE_INFO*** *defined in order for this service to return performance information.*

### Parameters
- *thread_ptr*: Pointer to previously created thread.
- *resumptions*: Pointer to destination for the number of resumptions of this thread.
- *suspensions*: Pointer to destination for the number of suspensions of this thread.
- *solicited_preemptions*: Pointer to destination for the number of preemptions as a result of a ThreadX API service call made by this thread.
- *interrupt_preemptions*: Pointer to destination for the number of preemptions of this thread as a result of interrupt processing.
- *priority_inversions*: Pointer to destination for the number of priority inversions of this thread.
- *time_slices*: Pointer to destination for the number of time-slices of this thread.
- *relinquishes*: Pointer to destination for the number of thread relinquishes performed by this thread.
- *timeouts*: Pointer to destination for the number of suspension timeouts on this thread.
- *wait_aborts*: Pointer to destination for the number of wait aborts performed on this thread.
- *last_preempted_by*: Pointer to destination for the thread pointer that last preempted this thread.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful thread performance get.
- **TX_PTR_ERROR** (0x03) Invalid thread pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_THREAD my_thread;
ULONG resumptions;
ULONG suspensions;
ULONG solicited_preemptions;
ULONG interrupt_preemptions;
ULONG priority_inversions;
ULONG time_slices;
ULONG relinquishes;
ULONG timeouts;
ULONG wait_aborts;
TX_THREAD *last_preempted_by;

/* Retrieve performance information on the previously created
thread. */

status = tx_thread_performance_info_get(&my_thread, &resumptions,
    &suspensions,
    &solicited_preemptions, &interrupt_preemptions,
    &priority_inversions, &time_slices,
    &relinquishes, &timeouts,
    &wait_aborts, &last_preempted_by);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Thread Services](#Thread_Services)
