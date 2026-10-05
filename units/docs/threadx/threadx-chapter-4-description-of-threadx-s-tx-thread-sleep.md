---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-sleep"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_sleep"
summary: "Suspend current thread for specified time"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-sleep"
license: "MIT"
mode: "V"
---

Suspend current thread for specified time

### Prototype

```c
UINT tx_thread_sleep(ULONG timer_ticks);
```

### Description

This service causes the calling thread to suspend for the specified number of timer ticks. The amount of physical time associated with a timer tick is application specific. This service can be called only from an application thread.

### Parameters

- *timer_ticks*: The number of timer ticks to suspend the calling application thread, ranging from 0 through 0xFFFFFFFF. If 0 is specified, the service returns immediately.

### Return Values

- **TX_SUCCESS** (0x00) Successful thread sleep.
- **TX_WAIT_ABORTED** (0x1A) Suspension was aborted by another thread, timer, or ISR.
- **TX_CALLER_ERROR** (0x13) Service called from a non-thread.

### Allowed From

Threads

### Preemption Possible

Yes

### Example

```c
UINT status;

/* Make the calling thread sleep for 100
timer-ticks. */
status = tx_thread_sleep(100);

/* If status equals TX_SUCCESS, the currently running
application thread slept for the specified number of
timer-ticks. */
```

### See Also

- [Thread Services](#Thread_Services)
