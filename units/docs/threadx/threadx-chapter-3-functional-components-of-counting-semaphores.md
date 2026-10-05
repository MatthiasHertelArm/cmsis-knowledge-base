---
id: "threadx-chapter-3-functional-components-of-counting-semaphores"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Counting Semaphores"
summary: "ThreadX provides 32-bit counting semaphores that range in value between 0 and 4,294,967,295. There are two operations for counting semaphores: tx_semaphore_get and tx_semaphore_put. The get operation decreases the semaphore by one."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#counting-semaphores"
license: "MIT"
mode: "V"
---

ThreadX provides 32-bit counting semaphores that range in value between 0 and 4,294,967,295. There are two operations for counting semaphores: *tx_semaphore_get* and *tx_semaphore_put*. The get operation decreases the semaphore by one. If the semaphore is 0, the get operation is not successful. The inverse of the get operation is the put operation.
It increases the semaphore by one.

Each counting semaphore is a public resource. ThreadX places no constraints on how counting semaphores are used.

Counting semaphores are typically used for *mutual exclusion*. However, counting semaphores can also be used as a method for event notification.

### Mutual Exclusion

 Mutual exclusion pertains to controlling the access of threads to certain application areas (also called *critical sections* or *application resources*). When used for mutual exclusion, the "current count" of a semaphore represents the total number of threads that are allowed access. In most cases, counting semaphores used for mutual exclusion will have an initial value of 1, meaning that only one thread can access the associated resource at a time. Counting semaphores that only have values of 0 or 1 are commonly called *binary semaphores*.

> **Important:** *If a binary semaphore is being used, the user must prevent the same thread from performing a get operation on a semaphore it already owns. A second get would be unsuccessful and could cause indefinite suspension of the calling thread and permanent unavailability of the resource.*

### Event Notification

It is also possible to use counting semaphores as event notification, in a producer-consumer fashion. The consumer attempts to get the counting semaphore while the producer increases
the semaphore whenever something is available. Such semaphores usually have an initial value of 0 and will not increase until the producer has something ready for the consumer. Semaphores used for event notification may also benefit from use of the ***tx_semaphore_ceiling_put*** service call. This service ensures that the semaphore count never exceeds the value supplied in the call.

### Creating Counting Semaphores

Counting semaphores are created either during initialization or during run-time by application threads. The initial count of the semaphore is specified during creation. There is no limit on the number of counting semaphores in an application.

### Thread Suspension

Application threads can suspend while attempting to perform a get operation on a semaphore with a current count of 0.

After a put operation is performed, the suspended thread's get operation is performed and the thread is resumed. If multiple threads are suspended on the same counting semaphore, they are resumed in the same order they were suspended (FIFO).

However, priority resumption is also possible if the application calls ***tx_semaphore_prioritize*** prior to the semaphore put call that lifts thread suspension. The semaphore prioritize service places the highest priority thread at the front of the suspension list, while leaving all other suspended threads in the same FIFO order.

### Semaphore Put Notification

Some applications may find it advantageous to be notified whenever a semaphore is put. ThreadX provides this ability through the ***tx_semaphore_put_notify*** service. This service registers the supplied application notification function with the specified semaphore. ThreadX will subsequently invoke this application notification function whenever the semaphore is put. The exact processing within the application notification function is determined by the application; however, it typically consists of resuming the appropriate thread for processing the new semaphore put event.

### Semaphore Event chaining

The notification capabilities in ThreadX can be used to chain various synchronization events together. This is typically useful when a single thread must process multiple synchronization events.

For example, instead of having separate threads suspend for a queue message, event flags, and a semaphore, the application can register a notification routine for each object. When invoked, the application notification routine can then resume a single thread, which can interrogate each object to find and process the new event.

In general, *event-chaining* results in fewer threads, less overhead, and smaller RAM requirements. It also provides a highly flexible mechanism to handle synchronization requirements of more complex systems.

### Run-time Semaphore Performance Information

ThreadX provides optional run-time semaphore performance information. If the ThreadX library and application is built with **TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO** defined, ThreadX accumulates the following information.

Total number for the overall system:

  - semaphore puts

  - semaphore gets

  - semaphore get suspensions

  - semaphore get timeouts

Total number for each semaphore:

  - semaphore puts

  - semaphore gets

  - semaphore get suspensions

  - semaphore get timeouts

This information is available at run-time through the services ***tx_semaphore_performance_info_get*** and ***tx_semaphore_performance_system_info_get***. Semaphore performance
information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of "semaphore get timeouts" might suggest that other threads are holding resources too long.

### Semaphore Control Block TX_SEMAPHORE

The characteristics of each counting semaphore are found in its control block. It contains information such as the current semaphore count. This structure is defined in the ***tx_api.h*** file.

Semaphore control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Deadly Embrace

One of the most interesting and dangerous pitfalls associated with semaphores used for mutual exclusion is the *deadly embrace*. A deadly embrace, or *deadlock*, is a condition in which two or more threads are suspended indefinitely while attempting to get semaphores already owned by each other.

This condition is best illustrated by a two thread, two semaphore example. Suppose the first thread owns the first semaphore and the second thread owns the second semaphore. If the first thread attempts to get the second semaphore and at the same time the second thread attempts to get the first semaphore, both threads enter a deadlock condition. In addition, if these threads stay suspended forever, their associated resources are locked-out forever as well. Figure 8 illustrates this example.

**Deadly Embrace** (example)

(figure: Example of Suspended Threads)

**FIGURE 8. Example of Suspended Threads**

For real-time systems, deadly embraces can be prevented by placing certain restrictions on how threads obtain semaphores. Threads can only have one semaphore at a time. Alternatively, threads can own multiple semaphores if they gather them in the same order. In the previous example, if the first and second thread obtain the first and second semaphore in order, the deadly embrace is prevented.

> **Tip:** *It is also possible to use the suspension time-out associated with the get operation to recover from a deadly embrace.*

### Priority Inversion

Another pitfall associated with mutual exclusion semaphores is priority inversion. This topic is discussed more fully in "[Thread Priority Pitfalls](#thread-priority-pitfalls)".

The basic problem results from a situation in which a lower-priority thread has a semaphore that a higher priority thread needs. This in itself is normal. However, threads with priorities in between them may cause the priority inversion to last a nondeterministic amount of time. This can be handled through careful selection of thread priorities, using preemption-threshold, and temporarily raising the priority of the thread that owns the resource to that of the high priority thread.
