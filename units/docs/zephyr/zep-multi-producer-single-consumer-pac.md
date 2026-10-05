---
id: "zep-multi-producer-single-consumer-pac"
type: "concept"
domain: "rtos"
title: "Multi Producer Single Consumer Packet Buffer"
summary: "A Multi Producer Single Consumer Packet Buffer (MPSC_PBUF) is a circular buffer, whose contents are stored in first-in-first-out order. Variable size packets are stored in the buffer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/mpsc_pbuf.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/mpsc_pbuf.rst"
license: "Apache-2.0"
mode: "V"
---

A `Multi Producer Single Consumer Packet Buffer (MPSC_PBUF)` is a circular
buffer, whose contents are stored in first-in-first-out order. Variable size
packets are stored in the buffer. Packet buffer works under assumption that there
is a single context that consumes the data. However, it is possible that another
context may interfere to flush the data and never come back (panic case).
Packet is produced in two steps: first requested amount of data is allocated,
producer fills the data and commits it. Consuming a packet is also performed in
two steps: consumer claims the packet, gets pointer to it and length and later
on packet is freed. This approach reduces memory copying.

A `MPSC Packet Buffer` has the following key properties:

* Allocate, commit scheme used for packet producing.
* Claim, free scheme used for packet consuming.
* Allocator ensures that contiguous memory of requested length is allocated.
* Following policies can be applied when requested space cannot be allocated:

  * **Overwrite** - oldest entries are dropped until requested amount of memory can
    be allocated. For each dropped packet user callback is called.
  * **No overwrite** - When requested amount of space cannot be allocated,
    allocation fails.
* Dedicated, optimized API for storing short packets.
* Allocation with timeout.
