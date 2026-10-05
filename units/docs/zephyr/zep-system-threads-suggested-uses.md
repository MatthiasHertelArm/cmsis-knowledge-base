---
id: "zep-system-threads-suggested-uses"
type: "concept"
domain: "rtos"
title: "System Threads: Suggested Uses"
summary: "Use the main thread to perform thread-based processing in an application that only requires a single thread, rather than defining an additional application-specific thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/system_threads.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/system_threads.rst"
license: "Apache-2.0"
mode: "V"
---

Use the main thread to perform thread-based processing in an application
that only requires a single thread, rather than defining an additional
application-specific thread.
