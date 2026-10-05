---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_info_get"
summary: "This service retrieves information from the specified mutex."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about mutex

### Prototype

```c
UINT tx_mutex_info_get(
    TX_MUTEX *mutex_ptr, 
    CHAR **name,
    ULONG *count, 
    TX_THREAD **owner,
    TX_THREAD **first_suspended,
    ULONG *suspended_count, 
    TX_MUTEX **next_mutex);
```

### Description

This service retrieves information from the specified mutex.

### Parameters

- *mutex_ptr*: Pointer to mutex control block.
- *name*: Pointer to destination for the pointer to the mutex's name.
- *count*: Pointer to destination for the ownership count of the mutex.
- *owner*: Pointer to destination for the owning thread's pointer.
- *first_suspended*: Pointer to destination for the pointer to the thread that is first on the suspension list of this mutex.
- *suspended_count*: Pointer to destination for the number of threads currently suspended on this mutex.
- *next_mutex*: Pointer to destination for the pointer of the next created mutex.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex information retrieval.
- **TX_MUTEX_ERROR** (0x1C) Invalid mutex pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_MUTEX my_mutex;
CHAR *name;
ULONG count;
TX_THREAD *owner;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_MUTEX *next_mutex;
UINT status;

/* Retrieve information about the previously created
mutex "my_mutex." */
status = tx_mutex_info_get(&my_mutex, &name,
    &count, &owner,
    &first_suspended, &suspended_count,
    &next_mutex);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Mutex Services](#Mutex_Services)
