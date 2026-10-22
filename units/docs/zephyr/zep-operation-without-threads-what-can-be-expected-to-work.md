---
id: "zep-operation-without-threads-what-can-be-expected-to-work"
type: "concept"
domain: "rtos"
title: "Operation without Threads: What Can be Expected to Work"
summary: "These core capabilities shall function correctly when CONFIG_MULTITHREADING is disabled:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/nothread.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/nothread.rst"
license: "Apache-2.0"
mode: "V"
---

These core capabilities shall function correctly when
`CONFIG_MULTITHREADING` is disabled:

* The build system

* The ability to boot the application to `main()`

* Interrupt management

* The system clock including `k_uptime_get`

* Timers, i.e. `k_timer`

* Non-sleeping delays e.g. `k_busy_wait`.

* Sleeping `k_cpu_idle`.

* Pre `main()` drivers and subsystems initialization e.g. `SYS_INIT`.

* kernel_memory_management_api

* Specifically identified drivers in certain subsystems, listed below.

The expectations above affect selection of other features; for example
`CONFIG_SYS_CLOCK_EXISTS` cannot be set to `n`.
