---
id: "zep-operation-without-threads-what-cannot-be-expected-to-work"
type: "concept"
domain: "rtos"
title: "Operation without Threads: What Cannot be Expected to Work"
summary: "Functionality that will not work when CONFIG_MULTITHREADING is disabled includes majority of the kernel API:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/nothread.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/nothread.rst"
license: "Apache-2.0"
mode: "V"
---

Functionality that will not work when `CONFIG_MULTITHREADING`
is disabled includes majority of the kernel API:

* threads_v2

* scheduling_v2

* workqueues_v2

* polling_v2

* semaphores_v2

* mutexes_v2

* condvar

* kernel_data_passing_api
