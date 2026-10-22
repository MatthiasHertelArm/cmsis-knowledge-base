---
id: "zep-thread-local-storage-tls"
type: "concept"
domain: "rtos"
title: "Thread Local Storage (TLS)"
summary: "Thread Local Storage (TLS) allows variables to be allocated on a per-thread basis. These variables are stored in the thread stack which means every thread has its own copy of these variables."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/thread_local_storage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/thread_local_storage.rst"
license: "Apache-2.0"
mode: "V"
---

Thread Local Storage (TLS) allows variables to be allocated on a per-thread
basis. These variables are stored in the thread stack which means every
thread has its own copy of these variables.

Zephyr currently requires toolchain support for TLS.
