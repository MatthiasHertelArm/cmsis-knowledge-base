---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-create"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_create"
summary: "This service creates a counting semaphore for inter-thread synchronization. The initial semaphore count is specified as an input parameter."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-create"
license: "MIT"
mode: "V"
---

Create counting semaphore

### Prototype

```c
UINT tx_semaphore_create(
    TX_SEMAPHORE *semaphore_ptr,
    CHAR *name_ptr, 
    ULONG initial_count);
```

### Description

This service creates a counting semaphore for inter-thread synchronization. The initial semaphore count is specified as an input parameter.

### Parameters

- *semaphore_ptr*: Pointer to a semaphore control block.
- *name_ptr*: Pointer to the name of the semaphore.
- *initial_count*: Specifies the initial count for this semaphore. Legal values range from 0x00000000 through 0xFFFFFFFF.

### Return Values

- **TX_SUCCESS** (0x00) Successful semaphore creation.
- **TX_SEMAPHORE_ERROR** (0x0C) Invalid semaphore pointer. Either the pointer is NULL or the semaphore is already created.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

No

### Example

```c
TX_SEMAPHORE my_semaphore;
UINT status;

/* Create a counting semaphore whose initial value is 1.
This is typically the technique used to make a binary
semaphore. Binary semaphores are used to provide
protection over a common resource. */
status = tx_semaphore_create(&my_semaphore,
    "my_semaphore_name", 1);

/* If status equals TX_SUCCESS, my_semaphore is ready for
use. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
