---
id: "zep-message-queues-concepts"
type: "concept"
domain: "rtos"
title: "Message Queues: Concepts"
summary: "Any number of message queues can be defined (limited only by available RAM). Each message queue is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/data_passing/message_queues.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/data_passing/message_queues.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of message queues can be defined (limited only by available RAM).
Each message queue is referenced by its memory address.

A message queue has the following key properties:

* A **ring buffer** of data items that have been sent but not yet received.

* A **data item size**, measured in bytes.

* A **maximum quantity** of data items that can be queued in the ring buffer.

A message queue must be initialized before it can be used.
This sets its ring buffer to empty.

A data item can be **sent** to a message queue by a thread or an ISR.
The data item pointed at by the sending thread is copied to a waiting thread,
if one exists; otherwise the item is copied to the message queue's ring buffer,
if space is available. In either case, the size of the data area being sent
*must* equal the message queue's data item size.

If a thread attempts to send a data item when the ring buffer is full,
the sending thread may choose to wait for space to become available.
Any number of sending threads may wait simultaneously when the ring buffer
is full; when space becomes available
it is given to the highest priority sending thread that has waited the longest.

A data item can be **received** from a message queue by a thread.
The data item is copied to the area specified by the receiving thread;
the size of the receiving area *must* equal the message queue's data item size.

If a thread attempts to receive a data item when the ring buffer is empty,
the receiving thread may choose to wait for a data item to be sent.
Any number of receiving threads may wait simultaneously when the ring buffer
is empty; when a data item becomes available it is given to
the highest priority receiving thread that has waited the longest.

A thread can also **peek** at the message on the head of a message queue without
removing it from the queue.
The data item is copied to the area specified by the receiving thread;
the size of the receiving area *must* equal the message queue's data item size.


**Note:** The kernel does allow an ISR to receive an item from a message queue, however the ISR must not attempt to wait if the message queue is empty.


**Note:** Alignment of the message queue's ring buffer is not necessary. The underlying implementation uses `memcpy` (which is alignment-agnostic) and does not expose any internal pointers.
