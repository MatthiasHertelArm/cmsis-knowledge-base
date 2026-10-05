---
id: "threadx-chapter-3-functional-components-of-thread-control-block-tx-thread-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Thread Execution / Thread Control Block TX_THREAD"
summary: "The characteristics of each thread are contained in its control block. This structure is defined in the tx_api.h file."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#thread-control-block-tx-thread"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

The characteristics of each thread are contained in its control block. This structure is defined in the ***tx_api.h*** file.

A thread's control block can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

Locating the control block in other areas requires a bit more care, just like all dynamically allocated memory. If a control block is allocated within a C function, the memory associated with it is part of the calling thread's stack. In general, avoid using local storage for control blocks because after the function returns, all of its local variable stack space is released—regardless of whether another thread is using it for a control block!

In most cases, the application is oblivious to the contents of the thread's control block. However, there are some situations, especially during debug, in which looking at certain members is useful. The following are some of the more useful control block members:

- **tx_thread_run_count** contains a counter of the number of many times the thread has been scheduled. An increasing counter indicates the thread is being scheduled and executed.

- **tx_thread_state** contains the state of the associated thread. The following lists the possible thread states:

    - TX_READY(0x00)
    - TX_COMPLETED(0x01)
    - TX_TERMINATED(0x02)
    - TX_SUSPENDED(0x03)
    - TX_SLEEP(0x04)
    - TX_QUEUE_SUSP(0x05)
    - TX_SEMAPHORE_SUSP(0x06)
    - TX_EVENT_FLAG (0x07)
    - TX_BLOCK_MEMORY(0x08)
    - TX_BYTE_MEMORY (0x09)
    - TX_MUTEX_SUSP(0x0D)

> **Important:** Of course there are many other interesting fields in the thread control block, including the stack pointer, time-slice value, priorities, etc. Users are welcome to review control block members, but modifications are strictly prohibited!

> **Important:** There is no equate for the "executing" state mentioned earlier in this section. It is not necessary because there is only one executing thread at a given time. The state of an executing thread is also ***TX_READY***.
