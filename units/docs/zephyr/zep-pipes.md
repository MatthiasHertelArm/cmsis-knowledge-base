---
id: "zep-pipes"
type: "concept"
domain: "rtos"
title: "Pipes"
summary: "A pipe is a kernel object that allows a thread to send a byte stream to another thread. Pipes enable efficient inter-thread communication and can be used to synchronously transfer chunks of data in whole or in part."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/pipes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/pipes.rst"
license: "Apache-2.0"
mode: "V"
---

A `pipe` is a kernel object that allows a thread to send a byte stream
to another thread. Pipes enable efficient inter-thread communication and can
be used to synchronously transfer chunks of data in whole or in part.
