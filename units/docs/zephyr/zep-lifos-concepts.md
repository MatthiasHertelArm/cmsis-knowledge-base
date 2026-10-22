---
id: "zep-lifos-concepts"
type: "concept"
domain: "rtos"
title: "LIFOs: Concepts"
summary: "Any number of LIFOs can be defined (limited only by available RAM). Each LIFO is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/lifos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/lifos.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of LIFOs can be defined (limited only by available RAM). Each LIFO is
referenced by its memory address.

A LIFO has the following key properties:

* A **queue** of data items that have been added but not yet removed.
  The queue is implemented as a simple linked list.

A LIFO must be initialized before it can be used. This sets its queue to empty.

LIFO data items must be aligned as required for a pointer, as the kernel
reserves the first pointer-sized field of an item for use as a pointer to the
next data item in the queue. Consequently, a data item that holds N bytes of
application data requires N+4 (or N+8) bytes of memory. There are no alignment
or reserved space requirements for data items if they are added with
`k_lifo_alloc_put`, instead additional memory is temporarily
allocated from the calling thread's resource pool.


**Note:** LIFO data items are restricted to single active instance across all LIFO data queues. Any attempt to re-add a LIFO data item to a queue before it has been removed from the queue to which it was previously added will result in undefined behavior.

A data item may be **added** to a LIFO by a thread or an ISR.
The item is given directly to a waiting thread, if one exists;
otherwise the item is added to the LIFO's queue.
There is no limit to the number of items that may be queued.

A data item may be **removed** from a LIFO by a thread. If the LIFO's queue
is empty a thread may choose to wait for a data item to be given.
Any number of threads may wait on an empty LIFO simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.


**Note:** The kernel does allow an ISR to remove an item from a LIFO, however the ISR must not attempt to wait if the LIFO is empty.
