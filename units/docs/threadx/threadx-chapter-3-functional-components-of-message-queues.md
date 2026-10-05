---
id: "threadx-chapter-3-functional-components-of-message-queues"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Message Queues"
summary: "Message queues are the primary means of inter-thread communication in ThreadX. One or more messages can reside in a message queue. A message queue that holds a single message is commonly called a mailbox."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#message-queues"
license: "MIT"
mode: "V"
---

Message queues are the primary means of inter-thread communication in ThreadX. One or more messages can reside in a message queue. A message queue that holds a single message is commonly called a *mailbox*.

Messages are copied to a queue by ***tx_queue_send*** and are copied from a queue by ***tx_queue_receive***. The only exception to this is when a thread is suspended while waiting for a message on an empty queue. In this case, the next message sent to the queue is placed directly into the thread's destination area.

Each message queue is a public resource. ThreadX places no constraints on how message queues are used.

### Creating Message Queues

Message queues are created either during initialization or during run-time by application threads. There is no limit on the number of message queues in an application.

### Message Size

Each message queue supports a number of fixed-sized messages. The available message sizes are 1 through 16 32-bit words inclusive. The message size is specified when the queue is created. Application messages greater than 16 words must be passed by pointer. This is accomplished by creating a queue with a message size of 1 word (enough to hold a pointer) and then sending and receiving message pointers instead of the entire message.

### Message Queue Capacity

The number of messages a queue can hold is a function of its message size and the size of the memory area supplied during creation. The total message capacity of the queue is calculated by dividing the number of bytes in each message into the total number of bytes in the supplied memory area.

For example, if a message queue that supports a message size of 1 32-bit word (4 bytes) is created with a 100-byte memory area, its capacity is 25 messages.

### Queue Memory Area

As mentioned previously, the memory area for buffering messages is specified during queue creation. Like other memory areas in ThreadX, it can be located anywhere in the target's address space.

This is an important feature because it gives the application considerable flexibility. For example, an application might locate the memory area of an important queue in high-speed RAM to improve performance.

### Thread Suspension

Application threads can suspend while attempting to send or receive a message from a queue. Typically, thread suspension involves waiting for a message from an empty queue. However, it is also possible for a thread to suspend trying to send a message to a full queue.

After the condition for suspension is resolved, the service requested is completed and the waiting thread is resumed. If multiple threads are suspended on the same queue, they are resumed in the order they were suspended (FIFO).

However, priority resumption is also possible if the application calls ***tx_queue_prioritize*** prior to the queue service that lifts thread suspension. The queue prioritize service places the highest priority thread at the front of the suspension list, while leaving all other suspended threads in the same FIFO order.

Time-outs are also available for all queue suspensions. Basically, a time-out specifies the maximum number of timer ticks the thread will stay suspended. If a time-out occurs, the thread is resumed and the service returns with the appropriate error code.

### Queue Send Notification

Some applications may find it advantageous to be notified whenever a message is placed on a queue. ThreadX provides this ability through the ***tx_queue_send_notify*** service. This service registers the supplied application notification function with the specified queue. ThreadX will subsequently invoke this application notification function whenever a message is sent to the queue. The exact processing within the application notification function is determined by the application; however, it typically consists of resuming the appropriate thread for processing the new message.

### Queue Event chaining

The notification capabilities in ThreadX can be used to chain various synchronization events together. This is typically useful when a single thread must process multiple synchronization events.

For example, suppose a single thread is responsible for processing messages from five different queues and must also suspend when no messages are available. This is easily accomplished by registering an application notification function for each queue and introducing an additional counting semaphore. Specifically, the application notification function performs a *tx_semaphore_put* whenever it is called (the semaphore count represents the total number of messages in all five queues). The processing thread suspends on this semaphore via the
*tx_semaphore_get* service. When the semaphore is available (in this case, when a message is available!), the processing thread is resumed. It then interrogates each queue for a message, processes the found message, and performs another ***tx_semaphore_get*** to wait for the next message. Accomplishing this without event-chaining is quite difficult and likely would require more threads and/or additional application code.

In general, *event-chaining* results in fewer threads, less overhead, and smaller RAM requirements. It also provides a highly flexible mechanism to handle synchronization requirements of more complex systems.

### Run-time Queue Performance Information
ThreadX provides optional run-time queue performance information. If the ThreadX library and application is built with
***TX_QUEUE_ENABLE_PERFORMANCE_INFO*** defined, ThreadX accumulates the following information.

Total number for the overall system:

  - messages sent

  - messages received

  - queue empty suspensions

  - queue full suspensions

  - queue full error returns (suspension not specified)

  - queue timeouts

Total number for each queue:

  - messages sent

  - messages received

  - queue empty suspensions

  - queue full suspensions

  - queue full error returns (suspension not specified)

  - queue timeouts

This information is available at run-time through the services ***tx_queue_performance_info_get*** and ***tx_queue_performance_system_info_get***. Queue performance
information is useful in determining if the application is behaving properly. It is also useful in optimizing the application. For example, a relatively high number of "queue full suspensions" suggests an increase in the queue size might be beneficial.

### Queue Control Block TX_QUEUE

The characteristics of each message queue are found in its control block. It contains interesting information such as the number of messages in the queue. This structure is defined in the ***tx_api.h*** file.

Message queue control blocks can also be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.

### Message Destination Pitfall

As mentioned previously, messages are copied between the queue area and application data areas. It is important to ensure the destination for a received message is large enough to hold the entire message. If not, the memory following the message destination will likely be corrupted.

> **Note:** *This is especially lethal when a too-small message destination is on the stack—nothing like corrupting the return address of a function!*
