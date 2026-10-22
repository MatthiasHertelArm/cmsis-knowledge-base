---
id: "zep-system-calls-verification-function"
type: "concept"
domain: "rtos"
title: "System Calls: Verification Function"
summary: "The verification function runs on the kernel side when a user thread makes a system call."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

The verification function runs on the kernel side when a user thread makes
a system call. When the user thread makes a software interrupt to elevate to
supervisor mode, the common system call entry point uses the system call ID
provided by the user to look up the appropriate unmarshalling function for that
system call and jump into it. This in turn calls the verification function.

Verification and unmarshalling functions only run when system call APIs are
invoked from user mode. If an API is invoked from supervisor mode, the
implementation is simply called and there is no software trap.

The purpose of the verification function is to validate all the arguments
passed in.  This includes:

* Any kernel object pointers provided. For example, the semaphore APIs must
  ensure that the semaphore object passed in is a valid semaphore and that
  the calling thread has permission on it.

* Any memory buffers passed in from user mode. Checks must be made that the
  calling thread has read or write permissions on the provided buffer.

* Any other arguments that have a limited range of valid values.

Verification functions involve a great deal of boilerplate code which has been
made simpler by some macros in `include/zephyr/internal/syscall_handler.h`.
Verification functions should be declared using these macros.
