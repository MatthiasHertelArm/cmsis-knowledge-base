---
id: "zep-single-producer-single-consumer-pa"
type: "concept"
domain: "rtos"
title: "Single Producer Single Consumer Packet Buffer"
summary: "A Single Producer Single Consumer Packet Buffer (SPSC_PBUF) is a circular buffer, whose contents are stored in first-in-first-out order. Variable size packets are stored in the buffer."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/spsc_pbuf.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/spsc_pbuf.rst"
license: "Apache-2.0"
mode: "V"
---

A `Single Producer Single Consumer Packet Buffer (SPSC_PBUF)` is a circular
buffer, whose contents are stored in first-in-first-out order. Variable size
packets are stored in the buffer. Packet buffer works under assumption that there
is a single context that produces packets and a single context that consumes the
data.

Implementation is focused on performance and memory footprint.

Packets are added to the buffer using `spsc_pbuf_write` which copies a
data into the buffer. If the buffer is full error is returned.

Packets are copied out of the buffer using `spsc_pbuf_read`.
