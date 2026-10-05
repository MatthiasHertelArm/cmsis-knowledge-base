---
id: "zep-threads-thread-options"
type: "concept"
domain: "rtos"
title: "Threads: Thread Options"
summary: "The kernel supports a small set of thread options that allow a thread to receive special treatment under specific circumstances. The set of options associated with a thread are specified when the thread is spawned."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel supports a small set of `thread options` that allow a thread
to receive special treatment under specific circumstances. The set of options
associated with a thread are specified when the thread is spawned.

A thread that does not require any thread option has an option value of zero.
A thread that requires a thread option specifies it by name, using the
`|` character as a separator if multiple options are needed
(i.e. combine options using the bitwise OR operator).

The following thread options are supported.

`K_ESSENTIAL`
    This option tags the thread as an `essential thread`. This instructs
    the kernel to treat the termination or aborting of the thread as a fatal
    system error.

    By default, the thread is not considered to be an essential thread.

`K_SSE_REGS`
    This x86-specific option indicate that the thread uses the CPU's
    SSE registers. Also see `K_FP_REGS`.

    By default, the kernel does not attempt to save and restore the contents
    of these registers when scheduling the thread.

`K_FP_REGS`
    This option indicate that the thread uses the CPU's floating point
    registers. This instructs the kernel to take additional steps to save
    and restore the contents of these registers when scheduling the thread.
    (For more information see float_v2.)

    By default, the kernel does not attempt to save and restore the contents
    of this register when scheduling the thread.

`K_USER`
    If `CONFIG_USERSPACE` is enabled, this thread will be created in
    user mode and will have reduced privileges. See usermode_api. Otherwise
    this flag does nothing.

`K_INHERIT_PERMS`
    If `CONFIG_USERSPACE` is enabled, this thread will inherit all
    kernel object permissions that the parent thread had, except the parent
    thread object.  See usermode_api.
