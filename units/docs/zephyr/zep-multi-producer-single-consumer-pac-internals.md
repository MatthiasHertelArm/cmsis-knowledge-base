---
id: "zep-multi-producer-single-consumer-pac-internals"
type: "concept"
domain: "rtos"
title: "Multi Producer Single Consumer Packet Buffer: Internals"
summary: "Each packet in the buffer contains MPSC_PBUF specific header which is used for internal management. Header consists of 2 bit flags."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/mpsc_pbuf.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/mpsc_pbuf.rst"
license: "Apache-2.0"
mode: "V"
---

Each packet in the buffer contains `MPSC_PBUF` specific header which is used
for internal management. Header consists of 2 bit flags. In order to optimize
memory usage, header can be added on top of the user header using
`MPSC_PBUF_HDR` and remaining bits in the first word can be application
specific. Header consists of following flags:

* valid - bit set to one when packet contains valid user packet
* busy - bit set when packet is being consumed (claimed but not free)

Header state:

+-------+------+----------------------+
| valid | busy | description          |
+-------+------+----------------------+
| 0     | 0    | space is free        |
+-------+------+----------------------+
| 1     | 0    | valid packet         |
+-------+------+----------------------+
| 1     | 1    | claimed valid packet |
+-------+------+----------------------+
| 0     | 1    | internal skip packet |
+-------+------+----------------------+

Packet buffer space contains free space, valid user packets and internal skip
packets. Internal skip packets indicates padding, e.g. at the end of the buffer.


### Allocation


Using pairs for read and write indexes, available space is determined. If
space can be allocated, temporary write index is moved and pointer to a space
within buffer is returned. Packet header is reset. If allocation required
wrapping of the write index, a skip packet is added to the end of buffer. If
space cannot be allocated and overwrite is disabled then `NULL` pointer is
returned or context blocks if allocation was with timeout.


### Allocation with overwrite


If overwrite is enabled, oldest packets are dropped until requested amount of
space can be allocated. When packets are dropped `busy` flag is checked in the
header to ensure that currently consumed packet is not overwritten. In that case,
skip packet is added before busy packet and packets following the busy packet
are dropped. When busy packet is being freed, such situation is detected and
packet is converted to skip packet to avoid double processing.
