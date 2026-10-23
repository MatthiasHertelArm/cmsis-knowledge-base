---
id: "zep-fifos-concepts"
type: "concept"
domain: "rtos"
title: "FIFOs: Concepts"
summary: "Any number of FIFOs can be defined (limited only by available RAM). Each FIFO is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/fifos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/fifos.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of FIFOs can be defined (limited only by available RAM). Each FIFO is
referenced by its memory address.

A FIFO has the following key properties:

* A **queue** of data items that have been added but not yet removed.
  The queue is implemented as a simple linked list.

A FIFO must be initialized before it can be used. This sets its queue to empty.

FIFO data items must be aligned as required for a pointer, as the kernel
reserves the first pointer-sized field of an item for use as a pointer to the
next data item in the queue. Consequently, a data item that holds N bytes of
application data requires N+4 (or N+8) bytes of memory. There are no alignment
or reserved space requirements for data items if they are added with
`k_fifo_alloc_put`, instead additional memory is temporarily
allocated from the calling thread's resource pool.


**Note:** FIFO data items are restricted to single active instance across all FIFO data queues. Any attempt to re-add a FIFO data item to a queue before it has been removed from the queue to which it was previously added will result in undefined behavior.

A data item may be **added** to a FIFO by a thread or an ISR.
The item is given directly to a waiting thread, if one exists;
otherwise the item is added to the FIFO's queue.
There is no limit to the number of items that may be queued.

A data item may be **removed** from a FIFO by a thread. If the FIFO's queue
is empty a thread may choose to wait for a data item to be given.
Any number of threads may wait on an empty FIFO simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.


**Note:** The kernel does allow an ISR to remove an item from a FIFO, however the ISR must not attempt to wait if the FIFO is empty.

If desired, **multiple data items** can be added to a FIFO in a single operation
if they are chained together into a singly-linked list. This capability can be
useful if multiple writers are adding sets of related data items to the FIFO,
as it ensures the data items in each set are not interleaved with other data
items. Adding multiple data items to a FIFO is also more efficient than adding
them one at a time, and can be used to guarantee that anyone who removes
the first data item in a set will be able to remove the remaining data items
without waiting.
