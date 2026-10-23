---
id: "zep-pipes-suggested-uses"
type: "concept"
domain: "rtos"
title: "Pipes: Suggested Uses"
summary: "Pipes are useful for sending streams of data between threads. Typical applications include:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/pipes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/pipes.rst"
license: "Apache-2.0"
mode: "V"
---

Pipes are useful for sending streams of data between threads. Typical
applications include:

- Implementing producer-consumer patterns.
- Streaming logs or packets between threads.
- Handling variable-length message passing in real-time systems.
