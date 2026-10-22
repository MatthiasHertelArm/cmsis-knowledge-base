---
id: "zep-system-calls-argument-validation"
type: "concept"
domain: "rtos"
title: "System Calls: Verification Function / Argument Validation"
summary: "Several macros exist to validate arguments:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/syscalls.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/syscalls.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Verification Function_

Several macros exist to validate arguments:

* `K_SYSCALL_OBJ()` Checks a memory address to assert that it is
  a valid kernel object of the expected type, that the calling thread
  has permissions on it, and that the object is initialized.

* `K_SYSCALL_OBJ_INIT()` is the same as
  `K_SYSCALL_OBJ()`, except that the provided object may be
  uninitialized. This is useful for verifiers of object init functions.

* `K_SYSCALL_OBJ_NEVER_INIT()` is the same as
  `K_SYSCALL_OBJ()`, except that the provided object must be
  uninitialized. This is not used very often, currently only for
  `k_thread_create()`.

* `K_SYSCALL_MEMORY_READ()` validates a memory buffer of a particular
  size. The calling thread must have read permissions on the entire buffer.

* `K_SYSCALL_MEMORY_WRITE()` is the same as
  `K_SYSCALL_MEMORY_READ()` but the calling thread must additionally
  have write permissions.

* `K_SYSCALL_MEMORY_ARRAY_READ()` validates an array whose total size
  is expressed as separate arguments for the number of elements and the
  element size. This macro correctly accounts for multiplication overflow
  when computing the total size. The calling thread must have read permissions
  on the total size.

* `K_SYSCALL_MEMORY_ARRAY_WRITE()` is the same as
  `K_SYSCALL_MEMORY_ARRAY_READ()` but the calling thread must
  additionally have write permissions.

* `K_SYSCALL_VERIFY_MSG()` does a runtime check of some boolean
  expression which must evaluate to true otherwise the check will fail.
  A variant `K_SYSCALL_VERIFY` exists which does not take
  a message parameter, instead printing the expression tested if it
  fails. The latter should only be used for the most obvious of tests.

* `K_SYSCALL_DRIVER_OP()` checks at runtime if a driver
  instance is capable of performing a particular operation.  While this
  macro can be used by itself, it's mostly a building block for macros
  that are automatically generated for every driver subsystem.  For
  instance, to validate the GPIO driver, one could use the
  `K_SYSCALL_DRIVER_GPIO()` macro.

* `K_SYSCALL_SPECIFIC_DRIVER()` is a runtime check to verify that
  a provided pointer is a valid instance of a specific device driver, that
  the calling thread has permissions on it, and that the driver has been
  initialized. It does this by checking the API structure pointer that
  is stored within the driver instance and ensuring that it matches the
  provided value, which should be the address of the specific driver's
  API structure.

If any check fails, the macros will return a nonzero value. The macro
`K_OOPS()` can be used to induce a kernel oops which will kill the
calling thread. This is done instead of returning some error condition to
keep the APIs the same when calling from supervisor mode.
