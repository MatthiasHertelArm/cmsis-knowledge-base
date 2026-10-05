---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-time-slice-change"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_time_slice_change"
summary: "Changes time-slice of application thread"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-time-slice-change"
license: "MIT"
mode: "V"
---

Changes time-slice of application thread

### Prototype

```c
UINT tx_thread_time_slice_change(
    TX_THREAD *thread_ptr,
    ULONG new_time_slice, 
    ULONG *old_time_slice);
```

### Description

This service changes the time-slice of the specified application thread. Selecting a time-slice for a thread insures that it won't execute more than the specified number of timer ticks before other threads of the same or higher priorities have a chance to execute.

> **Note:** *Using preemption-threshold disables time-slicing for the specified thread.*

### Parameters

- *thread_ptr*: Pointer to application thread.
- *new_time_slice*: New time slice value. Legal values include TX_NO_TIME_SLICE and numeric values from 1 through 0xFFFFFFFF.
- *old_time_slice*: Pointer to location for storing the previous timeslice value of the specified thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful time-slice chance.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_PTR_ERROR** (0x03) Invalid pointer to previous time-slice storage location.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads and timers

### Preemption Possible

No

### Example

```c
TX_THREAD my_thread;
ULONG my_old_time_slice;
UINT status;

/* Change the time-slice of the thread associated with
"my_thread" to 20. This will mean that "my_thread"
can only run for 20 timer-ticks consecutively before
other threads of equal or higher priority get a chance
to run. */
status = tx_thread_time_slice_change(&my_thread, 20,
    &my_old_time_slice);

/* If status equals TX_SUCCESS, the thread's time-slice
has been changed to 20 and the previous time-slice is
in "my_old_time_slice." */
```

### See Also

- [Thread Services](#Thread_Services)
