---
id: "zep-operation-without-threads"
type: "concept"
domain: "rtos"
title: "Operation without Threads"
summary: "Thread support is not necessary in some applications:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/nothread.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/nothread.rst"
license: "Apache-2.0"
mode: "V"
---

Thread support is not necessary in some applications:

* Bootloaders
* Simple event-driven applications
* Examples intended to demonstrate core functionality

Thread support can be disabled by setting
`CONFIG_MULTITHREADING` to `n`.  Since this configuration has
a significant impact on Zephyr's functionality and testing of it has
been limited, there are conditions on what can be expected to work in
this configuration.
