---
id: "zep-tracing-transport-backends"
type: "concept"
domain: "debug"
title: "Tracing: Transport Backends"
summary: "The following backends are currently supported:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tracing/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tracing/index.rst"
license: "Apache-2.0"
mode: "V"
---

The following backends are currently supported:

* UART
* USB
* File (Using the native port with POSIX architecture based targets)
* RTT (With SystemView)
* RAM (buffer to be retrieved by a debugger)
