---
id: "threadx-chapter-4-description-of-threadx-s-tx-mutex-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_mutex_create"
summary: "This service creates a mutex for inter-thread mutual exclusion for resource protection."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-mutex-create"
license: "MIT"
mode: "V"
---

Create mutual exclusion mutex

### Prototype

```c
UINT tx_mutex_create(
    TX_MUTEX *mutex_ptr,
    CHAR *name_ptr, 
    UINT priority_inherit);
```

### Description

This service creates a mutex for inter-thread mutual exclusion for resource protection.

### Parameters

- *mutex_ptr*: Pointer to a mutex control block.
- *name_ptr*: Pointer to the name of the mutex.
- *priority_inherit*: Specifies whether or not this mutex supports priority inheritance. If this value is TX_INHERIT, then priority inheritance is supported. However, if TX_NO_INHERIT is specified, priority inheritance is not supported by this mutex.

### Return Values

- **TX_SUCCESS** (0x00) Successful mutex creation.
- **TX_MUTEX_ERROR** (0x1C) Invalid mutex pointer. Either the pointer is NULL or the mutex is already created.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.
- **TX_INHERIT_ERROR** (0x1F) Invalid priority inherit parameter.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_MUTEX my_mutex;
UINT status;

/* Create a mutex to provide protection over a
common resource. */
status = tx_mutex_create(&my_mutex,"my_mutex_name",
    TX_NO_INHERIT);

/* If status equals TX_SUCCESS, my_mutex is ready for
use. */
```

### See Also

- [Mutex Services](#Mutex_Services)
