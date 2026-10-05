---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-performance-system-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_performance_system_info_get"
summary: "Get thread system performance information"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-performance-system-info-get"
license: "MIT"
mode: "V"
---

Get thread system performance information

### Prototype

```c
UINT tx_thread_performance_system_info_get(
    ULONG *resumptions,
    ULONG *suspensions, 
    ULONG *solicited_preemptions,
    ULONG *interrupt_preemptions, 
    ULONG *priority_inversions,
    ULONG *time_slices, 
    ULONG *relinquishes, 
    ULONG *timeouts,
    ULONG *wait_aborts, 
    ULONG *non_idle_returns,
    ULONG *idle_returns);
```

### Description

This service retrieves performance information about all the threads
in the system.

*The ThreadX library and application must be built with*

***TX_THREAD_ENABLE_PERFORMANCE_INFO*** *defined in order for this service to return performance information.*

### Parameters

- *resumptions*: Pointer to destination for the total number of thread resumptions.
- *suspensions*: Pointer to destination for the total number of thread suspensions.
- *solicited_preemptions*: Pointer to destination for the total number of thread preemptions as a result of a thread calling a ThreadX API service.
- *interrupt_preemptions*: Pointer to destination for the total number of thread preemptions as a result of interrupt processing.
- *priority_inversions*: Pointer to destination for the total number of thread priority inversions.
- *time_slices*: Pointer to destination for the total number of thread time-slices.
- *relinquishes*: Pointer to destination for the total number of thread relinquishes.
- *timeouts*: Pointer to destination for the total number of thread suspension timeouts.
- *wait_aborts*: Pointer to destination for the total number of thread wait aborts.
- *non_idle_returns*: Pointer to destination for the number of times a thread returns to the system when another thread is ready to execute.
- *idle_returns*: Pointer to destination for the number of times a thread returns to the system when no other thread is ready to execute (idle system).

> **Note:** *Supplying a **TX_NULL** for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful thread system performance get.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was not compiled with performance information enabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
ULONG resumptions;
ULONG suspensions;
ULONG solicited_preemptions;
ULONG interrupt_preemptions;
ULONG priority_inversions;
ULONG time_slices;
ULONG relinquishes;
ULONG timeouts;
ULONG wait_aborts;
ULONG non_idle_returns;
ULONG idle_returns;

/* Retrieve performance information on all previously created
thread. */

status = tx_thread_performance_system_info_get(&resumptions,
    &suspensions,
    &solicited_preemptions, &interrupt_preemptions,
    &priority_inversions, &time_slices, &relinquishes,
    &timeouts, &wait_aborts, &non_idle_returns,
    &idle_returns);

/* If status is TX_SUCCESS the performance information was
successfully retrieved. */
```

### See Also

- [Thread Services](#Thread_Services)
