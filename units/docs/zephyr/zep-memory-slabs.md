---
id: "zep-memory-slabs"
type: "concept"
domain: "rtos"
title: "Memory Slabs"
summary: "A memory slab is a kernel object that allows memory blocks to be dynamically allocated from a designated memory region."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/memory_management/slabs.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/memory_management/slabs.rst"
license: "Apache-2.0"
mode: "V"
---

A `memory slab` is a kernel object that allows memory blocks
to be dynamically allocated from a designated memory region.
All memory blocks in a memory slab have a single fixed size,
allowing them to be allocated and released efficiently
and avoiding memory fragmentation concerns.
