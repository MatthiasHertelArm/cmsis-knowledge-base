---
id: "zep-ring-buffers-concepts"
type: "concept"
domain: "rtos"
title: "Ring Buffers: Concepts"
summary: "Any number of ring buffers can be defined (limited only by available RAM). Each ring buffer is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/ring_buffers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/ring_buffers.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of ring buffers can be defined (limited only by available RAM). Each
ring buffer is referenced by its memory address.

A ring buffer has the following key properties:

* A **data buffer** of bytes. The data buffer contains the raw
  bytes that have been added to the ring buffer but not yet
  removed.

* A **data buffer size**, measured in bytes. This governs
  the maximum amount of data the ring buffer can hold.

A ring buffer must be initialized before it can be used. This sets its
data buffer to empty.

A `struct ring_buf` may be placed anywhere in user-accessible
memory, and must be initialized with `ring_buf_init` before use.
This must be provided a region of user-controlled memory for use as the buffer itself.
Note carefully that the units of the size of the buffer passed change (either bytes or words)
depending on how the ring buffer will be used later. Macros for combining these steps in a
single static declaration exist for convenience.
`RING_BUF_DECLARE` will declare and statically initialize a ring
buffer with a specified byte count, where

"Bytes" data may be copied into the ring buffer using
`ring_buf_put`, passing a data pointer and byte count.  These
bytes will be copied into the buffer in order, as many as will fit in
the allocated buffer. The total number of bytes copied (which may be
fewer than provided) will be returned.  Likewise `ring_buf_get`
will copy bytes out of the ring buffer in the order that they were
written, into a user-provided buffer, returning the number of bytes
that were transferred.

To avoid multiply-copied-data situations, a zero-copy "pointer" API exists.
`ring_buf_put_ptr` returns a pointer to memory internal to the ring
buffer that can be used to receive bytes, along with the size of the
contiguous internal region available for writing (which may be smaller than
the total free space if the region wraps). The user can then write data
directly into that region (e.g. via DMA) without assembling all the bytes
in a single region first.  When complete, `ring_buf_commit` is used
to signal the buffer that the transfer is complete, passing the number of
bytes actually transferred. At this point a new transfer can be initiated.
Similarly, `ring_buf_get_ptr` returns a pointer to internal ring
buffer data from which the user can read without making a verbatim
copy, and `ring_buf_consume` signals the buffer with how many
bytes have been consumed and allows for a new transfer to begin.

The legacy `ring_buf_put_claim` / `ring_buf_put_finish` and
`ring_buf_get_claim` / `ring_buf_get_finish` APIs provide
similar functionality but reserve the claimed region until finished, which
incurs additional code size and runtime cost. These APIs are deprecated
and will be removed in a future release; new code should use the
`_ptr` / `_commit` / `_consume` variants described above.

The user can manage the capacity of a ring buffer without modifying it
using either `ring_buf_space_get` which returns the number of free bytes,
or by testing the `ring_buf_is_empty` predicate.

Finally, a `ring_buf_reset` call exists to immediately empty a
ring buffer, discarding the tracking of any bytes already
written to the buffer. It does not modify the memory contents of the
buffer itself, however.



### Instantiation and Usage


A ring buffer instance is declared using
`RING_BUF_DECLARE()` and accessed using:
`ring_buf_put_ptr`, `ring_buf_commit`,
`ring_buf_get_ptr`, `ring_buf_consume`,
`ring_buf_put` and `ring_buf_get`.

Data can be copied into the ring buffer (see
`ring_buf_put`) or ring buffer memory can be used
directly by the user. In the latter case, the operation is split into three stages:

1. Accessing the ring buffers internal buffer (`ring_buf_put_ptr`)
   to get a pointer to the next location where data can be written, and the
   amount of contiguous space available at that location.
#. writing the data by the user (e.g. buffer written by DMA).
#. indicating the amount of data written to the provided buffer
   (`ring_buf_commit`). The amount committed can be less than or equal to the amount
   provided by `ring_buf_put_ptr`.


Data can be retrieved from a ring buffer through copying
(see `ring_buf_get`) or accessed directly by address. In the latter
case, the operation is split into three stages:

1. Accessing the ring buffers internal buffer (see `ring_buf_get_ptr`) to get a pointer to
   the next location where data can be read, and the amount of contiguous data available at that
   location.
#. Processing data
#. Signal to the ring buffer that the data has been consumed (see `ring_buf_consume`).
   The amount consumed can be less than or equal to the amount provided by `ring_buf_get_ptr`.


### Concurrency


The ring buffer APIs do not provide any internal concurrency control.
Depending on usage (particularly with respect to number of concurrent
readers/writers) applications may need to protect the ring buffer with
mutexes and/or use semaphores to notify consumers that there is data to
read.

A single producer and a single consumer running in separate execution
contexts (for example two threads, or one thread and one ISR) may use
the same ring buffer concurrently without additional locking. The
producer side only updates the `put` indices and the consumer side
only updates the `get` indices, so the two sides never write the
same fields. This holds for both the copying APIs
(`ring_buf_put` / `ring_buf_get`) and the zero-copy
"claim" APIs (`ring_buf_put_claim` /
`ring_buf_put_finish` and `ring_buf_get_claim` /
`ring_buf_get_finish`).

When the producer and consumer run on different CPUs (SMP), the
application must still ensure that data writes are visible before the
index update that publishes them. In practice this happens for free
when the producer and consumer use a kernel synchronization primitive
to coordinate (for example a `k_sem` signaled by the
producer and waited on by the consumer), since those primitives
include the necessary memory barriers.

Any use case with more than one concurrent producer, or more than one
concurrent consumer, must serialize those accesses externally
(for example with a mutex or by disabling preemption).


### Internal Operation


Data streamed through a ring buffer is always written to the next byte
within the buffer, wrapping around to the first element after reaching
the end, thus the "ring" structure.  Internally, the ``struct
ring_buf`` contains its own buffer pointer and its size, and also a
set of "head" and "tail" indices representing where the next read and write
operations may occur.

This boundary is invisible to the user using the normal put/get APIs,
but becomes a barrier to the "claim" API, because obviously no
contiguous region can be returned that crosses the end of the buffer.
This can be surprising to application code, and produce performance
artifacts when transfers need to happen close to the end of the
buffer, as the number of calls to claim/finish needs to double for such
transfers.
