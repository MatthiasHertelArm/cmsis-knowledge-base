---
id: "zep-queues-cancelling-a-wait"
type: "concept"
domain: "rtos"
title: "Queues: Cancelling a Wait"
summary: "A thread that is blocked waiting to retrieve an item from a queue can be released without an item by calling k_queue_cancel_wait from another thread or an ISR."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/queues.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/queues.rst"
license: "Apache-2.0"
mode: "V"
---

A thread that is blocked waiting to retrieve an item from a queue can be released
without an item by calling `k_queue_cancel_wait` from another thread or
an ISR. The first thread pending on the queue returns from its
`k_queue_get` call with a `NULL` value, exactly as if its timeout had
expired. If the queue is instead being waited on through `k_poll`, that
call returns `-EINTR` with the poll event in the cancelled state.

This mechanism is also available to the queue-based primitives through
`k_fifo_cancel_wait` and `k_lifo_cancel_wait`.
