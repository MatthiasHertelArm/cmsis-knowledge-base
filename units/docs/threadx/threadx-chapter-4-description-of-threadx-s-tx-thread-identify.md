---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-identify"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_identify"
summary: "Retrieves pointer to currently executing thread"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-identify"
license: "MIT"
mode: "V"
---

Retrieves pointer to currently executing thread

### Prototype

```c
TX_THREAD* tx_thread_identify(VOID);
```
### Description

This service returns a pointer to the currently executing thread. If no thread is executing, this service returns a null pointer.

> **Note:** *If this service is called from an ISR, the return value represents the thread running prior to the executing interrupt handler.*

### Parameters

None

### Return Values

- *thread pointer*: Pointer to the currently executing thread. If no thread is executing, the return value is **TX_NULL**.

### Allowed From

Threads and ISRs

### Preemption Possible

No

### Example
```c
TX_THREAD *my_thread_ptr;

/* Find out who we are! */
my_thread_ptr = tx_thread_identify();

/* If my_thread_ptr is non-null, we are currently executing
from that thread or an ISR that interrupted that thread.
Otherwise, this service was called
from an ISR when no thread was running when the
interrupt occurred. */
```

### See Also

- [Thread Services](#Thread_Services)
