---
id: "threadx-chapter-4-description-of-threadx-s-tx-semaphore-info-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_semaphore_info_get"
summary: "This service retrieves information about the specified semaphore."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-semaphore-info-get"
license: "MIT"
mode: "V"
---

Retrieve information about semaphore

### Prototype

```c
UINT tx_semaphore_info_get(
    TX_SEMAPHORE *semaphore_ptr,
    CHAR **name, ULONG *current_value,
    TX_THREAD **first_suspended,
    ULONG *suspended_count,
    TX_SEMAPHORE **next_semaphore);
```

### Description

This service retrieves information about the specified semaphore.

### Parameters

- *semaphore_ptr*: Pointer to semaphore control block.
- *name*: Pointer to destination for the pointer to the semaphore's name.
- *current_value*: Pointer to destination for the current semaphore's count.
- *first_suspended*: Pointer to destination for the pointer to the thread that is first on the suspension list of this semaphore.
- *suspended_count*: Pointer to destination for the number of threads currently suspended on this semaphore.
- *next_semaphore*: Pointer to destination for the pointer of the next created semaphore.

> **Note:** *Supplying a TX_NULL for any parameter indicates that the parameter is not required.*

### Return Values

- **TX_SUCCESS** (0x00) information retrieval.

- **TX_SEMAPHORE_ERROR** (0x0C) Invalid semaphore pointer.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_SEMAPHORE my_semaphore;
CHAR *name;
ULONG current_value;
TX_THREAD *first_suspended;
ULONG suspended_count;
TX_SEMAPHORE *next_semaphore;
UINT status;

/* Retrieve information about the previously created
semaphore "my_semaphore." */
status = tx_semaphore_info_get(&my_semaphore, &name,
    &current_value,
    &first_suspended, &suspended_count,
    &next_semaphore);

/* If status equals TX_SUCCESS, the information requested is
valid. */
```

### See Also

- [Semaphore Services](#Semaphore_Services)
