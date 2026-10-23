---
id: "zep-scheduling-busy-waiting"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Busy Waiting"
summary: "A thread can call k_busy_wait to perform a busy wait that delays its processing for a specified time period without relinquishing the CPU to another ready thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

A thread can call `k_busy_wait` to perform a `busy wait`
that delays its processing for a specified time period
*without* relinquishing the CPU to another ready thread.

A busy wait is typically used instead of thread sleeping
when the required delay is too short to warrant having the scheduler
context switch from the current thread to another thread and then back again.
