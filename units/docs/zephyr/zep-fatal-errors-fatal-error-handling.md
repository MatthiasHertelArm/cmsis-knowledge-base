---
id: "zep-fatal-errors-fatal-error-handling"
type: "concept"
domain: "rtos"
title: "Fatal Errors: Fatal Error Handling"
summary: "The policy for what to do when encountering a fatal error is determined by the implementation of the k_sys_fatal_error_handler() function."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/fatal.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/fatal.rst"
license: "Apache-2.0"
mode: "V"
---

The policy for what to do when encountering a fatal error is determined by the
implementation of the `k_sys_fatal_error_handler()` function.  This
function has a default implementation with weak linkage that calls
`LOG_PANIC()` to dump all pending logging messages and then unconditionally
halts the system with `k_fatal_halt()`.

Applications are free to implement their own error handling policy by
overriding the implementation of `k_sys_fatal_error_handler()`.
If the implementation returns, the faulting thread will be aborted and
the system will otherwise continue to function. See the documentation for
this function for additional details and constraints.
