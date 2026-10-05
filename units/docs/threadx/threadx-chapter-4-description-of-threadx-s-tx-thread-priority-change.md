---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-priority-change"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_priority_change"
summary: "This service changes the priority of the specified thread. Valid priorities range from 0 through (TX_MAX_PRIORITIES-1), where 0 represents the highest priority level."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-priority-change"
license: "MIT"
mode: "V"
---

Change priority of application thread

### Prototype

```c
UINT tx_thread_priority_change(
    TX_THREAD *thread_ptr,
    UINT new_priority, 
    UINT *old_priority);
```

### Description

This service changes the priority of the specified thread. Valid priorities range from 0 through (TX_MAX_PRIORITIES-1), where 0 represents the highest priority level.

> **Important:** *The preemption-threshold of the specified thread is automatically set to the new priority. If a new threshold is desired, the ***tx_thread_preemption_change*** service must be used after this call.*

### Parameters

- *thread_ptr*: Pointer to a previously created application thread.
- *new_priority*: New thread priority level (0 through (TX_MAX_PRIORITIES-1)).
- *old_priority*: Pointer to a location to return the thread's previous priority.

### Return Values

- **TX_SUCCESS** (0x00) Successful priority change.
- **TX_THREAD_ERROR** (0x0E) Invalid application thread pointer.
- **TX_PRIORITY_ERROR** (0x0F) Specified new priority is not valid (a value other than (0 through (TX_MAX_PRIORITIES-1)).
- **TX_PTR_ERROR** (0x03) Invalid pointer to previous priority storage location.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Threads and timers

### Preemption Possible

Yes

### Example

```c
TX_THREAD my_thread;
UINT my_old_priority;
UINT status;

/* Change the thread represented by "my_thread" to priority
0. */

status = tx_thread_priority_change(&my_thread,
    0, &my_old_priority);

/* If status equals TX_SUCCESS, the application thread is
now at the highest priority level in the system. */
```
### See Also

- [Thread Services](#Thread_Services)
