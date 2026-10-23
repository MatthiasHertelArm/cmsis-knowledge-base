---
id: "zep-mutexes-user-mode-mutex-api-reference"
type: "concept"
domain: "rtos"
title: "Mutexes: User Mode Mutex API Reference"
summary: "sys_mutex behaves almost exactly like k_mutex, with the added advantage that a sys_mutex instance can reside in user memory. When user mode isn't enabled, sys_mutex behaves like k_mutex."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/mutexes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/mutexes.rst"
license: "Apache-2.0"
mode: "V"
---

`sys_mutex` behaves almost exactly like `k_mutex`, with the added advantage
that a `sys_mutex` instance can reside in user memory. When user mode isn't
enabled, `sys_mutex` behaves like `k_mutex`.
