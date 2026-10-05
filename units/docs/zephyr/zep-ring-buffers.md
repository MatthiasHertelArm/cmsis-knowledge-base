---
id: "zep-ring-buffers"
type: "concept"
domain: "rtos"
title: "Ring Buffers"
summary: "A ring buffer is a circular buffer, whose contents are stored in first-in-first-out order."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/ring_buffers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/ring_buffers.rst"
license: "Apache-2.0"
mode: "V"
---

A `ring buffer` is a circular buffer, whose contents are stored in
first-in-first-out order.

For circumstances where an application needs to implement asynchronous
"streaming" copying of data, Zephyr provides a `struct ring_buf`
abstraction to manage copies of such data in and out of a shared
buffer of memory.
