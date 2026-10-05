---
id: "zep-memory-slabs-suggested-uses"
type: "concept"
domain: "rtos"
title: "Memory Slabs: Suggested Uses"
summary: "Use a memory slab to allocate and free memory in fixed-size blocks."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/memory_management/slabs.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/memory_management/slabs.rst"
license: "Apache-2.0"
mode: "V"
---

Use a memory slab to allocate and free memory in fixed-size blocks.

Use memory slab blocks when sending large amounts of data from one thread
to another, to avoid unnecessary copying of the data.
