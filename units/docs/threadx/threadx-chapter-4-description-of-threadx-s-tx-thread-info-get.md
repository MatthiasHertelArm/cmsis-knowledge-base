---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_info_get"
summary: "This service retrieves information about the specified thread."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about thread

### Prototype

```c
UINT tx_thread_info_get(
    TX_THREAD *thread_ptr, 
    CHAR **name,
    UINT *state, 
    ULONG *run_count,
    UINT *priority,
    UINT *preemption_threshold,
    ULONG *time_slice,
    TX_THREAD **next_thread,
    TX_THREAD **suspended_thread);
```

### Description

This service retrieves information about the specified thread.

### Parameters
- *thread_ptr*: Pointer to thread control block.
- *name*: Pointer to destination for the pointer to the thread's name.
- *state*: Pointer to destination for the thread's current execution state. Possible values are as follows.
    - **TX_READY** (0x00)
    - **TX_COMPLETED** (0x01)
    - **TX_TERMINATED** (0x02)
    - **TX_SUSPENDED** (0x03)
    - **TX_SLEEP** (0x04)
    - **TX_QUEUE_SUSP** (0x05)
    - **TX_SEMAPHORE_SUSP** (0x06)
    - **TX_EVENT_FLAG** (0x07)
    - **TX_BLOCK_MEMORY** (0x08)
    - **TX_BYTE_MEMORY** (0x09)
    - **TX_MUTEX_SUSP** (0x0D)  

- *run_count*: Pointer to destination for the thread's run count.
- *priority*: Pointer to destination for the thread's priority.
- *preemption_threshold*: Pointer to destination for the thread's preemption-threshold.
- *time_slice*: Pointer to destination for the thread's time-slice.
- *next_thread*: Pointer to destination for next created thread pointer.
- *suspended_thread*: Pointer to destination for pointer to next
thread in suspension list.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful thread information retrieval.
- **TX_THREAD_ERROR** (0x0E) Invalid thread control pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_THREAD my_thread;
CHAR *name;
UINT state;
ULONG run_count;
UINT priority;
UINT preemption_threshold;
UINT time_slice;
TX_THREAD *next_thread;
TX_THREAD *suspended_thread;
UINT status;

/* Retrieve information about the previously created
thread "my_thread." */

status = tx_thread_info_get(&my_thread, &name,
    &state, &run_count,
    &priority, &preemption_threshold,
    &time_slice, &next_thread,&suspended_thread);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Thread Services](#Thread_Services)
