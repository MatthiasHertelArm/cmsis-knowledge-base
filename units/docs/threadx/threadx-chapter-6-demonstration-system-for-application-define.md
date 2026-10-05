---
id: "threadx-chapter-6-demonstration-system-for-application-define"
type: "concept"
domain: "rtos"
title: "Chapter 6 - Demonstration System for ThreadX: Application Define"
summary: "The tx_application_define function executes after the basic ThreadX initialization is complete. It is responsible for setting up all of the initial system resources, including threads, queues, semaphores, mutexes, event flags, and memory pools."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter6.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter6.md#application-define"
license: "MIT"
mode: "V"
---

The ***tx_application_define*** function executes after the basic
ThreadX initialization is complete. It is responsible for setting up
all of the initial system resources, including threads, queues,
semaphores, mutexes, event flags, and memory pools.

The demonstration system's ***tx_application_define*** (*line
numbers 60-164*) creates the demonstration objects in the following
order:

- byte_pool_0
- thread_0
- thread_1
- thread_2
- thread_3
- thread_4
- thread_5
- thread_6
- thread_7
- queue_0
- semaphore_0
- event_flags_0
- mutex_0
- block_pool_0

The demonstration system does not create any other additional ThreadX
objects. However, an actual application may create system objects
during runtime inside of executing threads.

### Initial Execution

All threads are created with the **TX_AUTO_START**
option. This makes them initially ready for execution. After
***tx_application_define*** completes, control is transferred to the
thread scheduler and from there to each individual thread.

The order in which the threads execute is determined by their priority
and the order that they were created. In the demonstration system,
***thread_0*** executes first because it has the highest priority
(*it was created with a priority of 1*). After ***thread_0***
suspends, ***thread_5*** is executed, followed by the execution of
***thread_3***, ***thread_4***, ***thread_6***, ***thread_7***,
***thread_1***, and finally ***thread_2***.

> **Note:** *Even though **thread_3** and **thread_4** have the same priority
(both created with a priority of 8), **thread_3** executes first.
This is because **thread_3** was created and became ready before
**thread_4**. Threads of equal priority execute in a FIFO fashion.*
