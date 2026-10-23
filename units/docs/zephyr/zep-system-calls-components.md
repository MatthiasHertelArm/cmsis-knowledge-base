---
id: "zep-system-calls-components"
type: "concept"
domain: "rtos"
title: "System Calls: Components"
summary: "All system calls have the following components:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

All system calls have the following components:

* A **C prototype** prefixed with `__syscall` for the API. It
  will be declared in some header under `include/` or in another
  `SYSCALL_INCLUDE_DIRS` directory. This prototype is never implemented
  manually, instead it gets created by the gen_syscalls.py script.
  What gets generated is an inline function which either calls the
  implementation function directly (if called from supervisor mode) or goes
  through privilege elevation and validation steps (if called from user
  mode).

* An **implementation function**, which is the real implementation of the
  system call. The implementation function may assume that all parameters
  passed in have been validated if it was invoked from user mode.

* A **verification function**, which wraps the implementation function
  and does validation of all the arguments passed in.

* An **unmarshalling function**, which is an automatically generated
  handler that must be included by user source code.
