---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-preemption-change"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_preemption_change"
summary: "Change preemption-threshold of application thread"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-preemption-change"
license: "MIT"
mode: "V"
---

Change preemption-threshold of application thread

### Prototype

```c
UINT tx_thread_preemption_change(
    TX_THREAD *thread_ptr,
    UINT new_threshold, 
    UINT *old_threshold);
```

### Description

This service changes the preemption-threshold of the specified thread. The preemption-threshold prevents preemption of the specified thread by threads equal to or less than the preemption-threshold value.

> **Note:** *Using preemption-threshold disables time-slicing for the specified thread.*

### Parameters
- *thread_ptr*: Pointer to a previously created application thread.
- *new_threshold*: New preemption-threshold priority level (0 through (TX_MAX_PRIORITIES-1)).
- *old_threshold*: Pointer to a location to return the previous preemption-threshold.

### Return Values

- **TX_SUCCESS** (0x00) Successful preemption-threshold change.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_THRESH_ERROR** (0x18) Specified new preemption-threshold is not a valid thread priority (a value other than (0 through (**TX_MAX_PRIORITIES**-1)) or is greater than (lower priority) than the current thread priority.
- **TX_PTR_ERROR** (0x03) Invalid pointer to previous preemption threshold storage location.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads and timers

### Preemption Possible

Yes

### Example

```c
TX_THREAD my_thread;
UINT my_old_threshold;
UINT status;

/* Disable all preemption of the specified thread. The
current preemption-threshold is returned in
"my_old_threshold". Assume that "my_thread" has
already been created. */

status = tx_thread_preemption_change(&my_thread,
    0, &my_old_threshold);

/* If status equals TX_SUCCESS, the application thread is
non-preemptable by another thread. Note that ISRs are
not prevented by preemption disabling. */
```

### See Also

- [Thread Services](#Thread_Services)
