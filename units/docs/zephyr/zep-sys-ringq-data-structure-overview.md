---
id: "zep-sys-ringq-data-structure-overview"
type: "concept"
domain: "rtos"
title: "sys_ringq Data Structure: Overview"
summary: "A ring queue (or circular buffer) is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end. This structure is particularly useful for buffering items in a ordered manner."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/data_structures/ringq.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/data_structures/ringq.rst"
license: "Apache-2.0"
mode: "V"
---

A ring queue (or circular buffer) is a data structure that uses a single, fixed-size buffer as if it
were connected end-to-end. This structure is particularly useful for buffering items in a ordered
manner.

The ringq is used whenever you need to decouple producers and consumers of discrete data sizes
without worrying about partial reads or variable-length payloads. This differentiation separates it
from the ring_buffer data structure, which is a streaming data structure
of bytes.


### Concurrency


The sys_ringq api do not provide any concurrency control. Depending on usage, applications
should protect the sys_ringq structure with appropriate synchronization mechanisms (e.g., mutexes,
semaphores) to ensure thread safety when accessed from multiple threads.
