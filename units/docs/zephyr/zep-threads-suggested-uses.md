---
id: "zep-threads-suggested-uses"
type: "concept"
domain: "rtos"
title: "Threads: Suggested Uses"
summary: "Use threads to handle processing that cannot be handled in an ISR."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

Use threads to handle processing that cannot be handled in an ISR.

Use separate threads to handle logically distinct processing operations
that can execute in parallel.
