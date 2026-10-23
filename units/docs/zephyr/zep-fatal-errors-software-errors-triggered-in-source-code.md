---
id: "zep-fatal-errors-software-errors-triggered-in-source-code"
type: "concept"
domain: "rtos"
title: "Fatal Errors: Software Errors Triggered in Source Code"
summary: "Zephyr provides several methods for inducing fatal error conditions through either build-time checks, conditionally compiled assertions, or deliberately invoked panic or oops conditions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/fatal.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/fatal.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides several methods for inducing fatal error conditions through
either build-time checks, conditionally compiled assertions, or deliberately
invoked panic or oops conditions.

Failed runtime assertions (`ZASSERT() and the legacy ASSERT()`) induce
a fatal error. See assert for details on the assertion APIs and how
their failure behavior is configured.


### Kernel Oops


A kernel oops is a software triggered fatal error invoked by
`k_oops()`.  This should be used to indicate an unrecoverable condition
in application logic.

The fatal error reason code generated will be `K_ERR_KERNEL_OOPS`.


### Kernel Panic


A kernel error is a software triggered fatal error invoked by
`k_panic()`.  This should be used to indicate that the Zephyr kernel is
in an unrecoverable state. Implementations of
`k_sys_fatal_error_handler()` should not return if the kernel
encounters a panic condition, as the entire system needs to be reset.

Threads running in user mode are not permitted to invoke `k_panic()`,
and doing so will generate a kernel oops instead. Otherwise, the fatal error
reason code generated will be `K_ERR_KERNEL_PANIC`.
