---
id: "zep-system-calls-verification-return-value-policies"
type: "concept"
domain: "rtos"
title: "System Calls: Verification Function / Verification Return Value Policies"
summary: "When verifying system calls, it's important to note which kinds of verification failures should propagate a return value to the caller, and which should simply invoke K_OOPS() which kills the calling thread. The current conventions are as follows:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Verification Function_

When verifying system calls, it's important to note which kinds of verification
failures should propagate a return value to the caller, and which should
simply invoke `K_OOPS()` which kills the calling thread. The current
conventions are as follows:

#. For system calls that are defined but not compiled, invocations of these
   missing system calls are routed to `handler_no_syscall()` which
   invokes `K_OOPS()`.

#. Any invalid access to memory found by the set of `K_SYSCALL_MEMORY` APIs,
   `k_usermode_from_copy()`, `k_usermode_to_copy()`
   should trigger a `K_OOPS`. This happens when the caller doesn't have
   appropriate permissions on the memory buffer or some size calculation
   overflowed.

#. Most system calls take kernel object pointers as an argument, checked either
   with one of the `K_SYSCALL_OBJ` functions,  `K_SYSCALL_DRIVER_nnnnn`, or
   manually using `k_object_validate()`. These can fail for a variety
   of reasons: missing driver API, bad kernel object pointer, wrong kernel
   object type, or improper initialization state. These issues should always
   invoke `K_OOPS()`.

#. Any error resulting from a failed memory heap allocation, often from
   invoking `z_thread_malloc()`, should propagate `-ENOMEM` to the
   caller.

#. General parameter checks should be done in the implementation function,
   in most cases using `CHECKIF()`.

   * The behavior of `CHECKIF()` depends on the kernel configuration, but if
     user mode is enabled, `CONFIG_RUNTIME_ERROR_CHECKS` is enforced,
     which guarantees that these checks will be made and a return value
     propagated.

#. It is totally forbidden for any kind of kernel mode callback function to
   be registered from user mode. APIs which simply install callbacks shall not
   be exposed as system calls. Some driver subsystem APIs may take optional
   function callback pointers. User mode verification functions for these APIs
   must enforce that these are NULL and should invoke `K_OOPS()` if
   not.

#. Some parameter checks are enforced only from user mode. These should be
   checked in the verification function and propagate a return value to the
   caller if possible.

There are some known exceptions to these policies currently in Zephyr:

* `k_thread_join()` and `k_thread_abort()` are no-ops if
  the thread object isn't initialized. This is because for threads, the
  initialization bit pulls double-duty to indicate whether a thread is
  running, cleared upon exit. See #23030.

* `k_thread_create()` invokes `K_OOPS()` for parameter
  checks, due to a great deal of existing code ignoring the return value.
  This will also be addressed by #23030.

* `k_thread_abort()` invokes `K_OOPS()` if an essential
  thread is aborted, as the function has no return value.

* Various system calls related to logging invoke `K_OOPS()`
  when bad parameters are passed in as they do not propagate errors.
