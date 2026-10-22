---
id: "zep-kernel-objects-supervisor-thread-access-permission"
type: "concept"
domain: "rtos"
title: "Kernel Objects: Supervisor Thread Access Permission"
summary: "Supervisor threads can access any kernel object. However, permissions for supervisor threads are still tracked for two reasons:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

Supervisor threads can access any kernel object. However, permissions for
supervisor threads are still tracked for two reasons:

* If a supervisor thread calls `k_thread_user_mode_enter`, the
  thread will then run in user mode with any permissions it had been granted
  (in many cases, by itself) when it was a supervisor thread.

* If a supervisor thread creates a user thread with the
  `K_INHERIT_PERMS` option, the child thread will be granted the
  same permissions as the parent thread, except the parent thread object.
