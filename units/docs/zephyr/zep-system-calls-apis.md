---
id: "zep-system-calls-apis"
type: "concept"
domain: "rtos"
title: "System Calls: APIs"
summary: "Helper macros for creating system call verification functions are provided in include/zephyr/internal/syscall_handler.h:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

Helper macros for creating system call verification functions are provided in
`include/zephyr/internal/syscall_handler.h`:

* `K_SYSCALL_OBJ()`
* `K_SYSCALL_OBJ_INIT()`
* `K_SYSCALL_OBJ_NEVER_INIT()`
* `K_OOPS()`
* `K_SYSCALL_MEMORY_READ()`
* `K_SYSCALL_MEMORY_WRITE()`
* `K_SYSCALL_MEMORY_ARRAY_READ()`
* `K_SYSCALL_MEMORY_ARRAY_WRITE()`
* `K_SYSCALL_VERIFY_MSG()`
* `K_SYSCALL_VERIFY`

Functions for invoking system calls are defined in
`include/zephyr/syscall.h`:

* `_arch_syscall_invoke0`
* `_arch_syscall_invoke1`
* `_arch_syscall_invoke2`
* `_arch_syscall_invoke3`
* `_arch_syscall_invoke4`
* `_arch_syscall_invoke5`
* `_arch_syscall_invoke6`
