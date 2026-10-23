---
id: "zep-kernel-objects-user-thread-access-permission"
type: "concept"
domain: "rtos"
title: "Kernel Objects: User Thread Access Permission"
summary: "By default, when a user thread is created, it will only have access permissions on its own thread object. Other kernel objects by default are not usable. Access to them needs to be explicitly or implicitly granted."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

By default, when a user thread is created, it will only have access permissions
on its own thread object. Other kernel objects by default are not usable.
Access to them needs to be explicitly or implicitly granted. There are several
ways to do this.

* If a thread is created with the `K_INHERIT_PERMS`, that thread
  will inherit all the permissions of the parent thread, except the parent
  thread object.

* A thread that has permission on an object, or is running in supervisor mode,
  may grant permission on that object to another thread via the
  `k_object_access_grant` API. The convenience pseudo-function
  `k_thread_access_grant` may also be used, which accepts an arbitrary
  number of pointers to kernel objects and calls
  `k_object_access_grant` on each of them. The thread being granted
  permission, or the object whose access is being granted, do not need to be
  in an initialized state. If the caller is from user mode, the caller must
  have permissions on both the kernel object and the target thread object.

* Supervisor threads may declare a particular kernel object to be a public
  object, usable by all current and future threads with the
  `k_object_access_all_grant` API. You must assume that any
  untrusted or exploited code will then be able to access the object. Use
  this API with caution!

* If a thread was declared statically with `K_THREAD_DEFINE()`,
  then the `K_THREAD_ACCESS_GRANT()` may be used to grant that thread
  access to a set of kernel objects at boot time.

Once a thread has been granted access to an object, such access may be
removed with the `k_object_access_revoke` API. This API is not
available to user threads, however user threads may use
`k_object_release` to relinquish their own permissions on an
object.

Supervisor threads may use `k_object_access_revoke_others` to revoke
access from all threads except the caller. This is useful to reset the
permissions of an object in cases where access was previously given to an
untrusted user thread, which may have in turn given it to others.
This API also reverts a public access state which may have been set previously
via `k_object_access_all_grant`.

API calls from supervisor mode to set permissions on kernel objects that are
not being tracked by the kernel will be no-ops. Doing the same from user mode
will result in a fatal error for the calling thread.

Objects allocated with `k_object_alloc` implicitly grant
permission on the allocated object to the calling thread.
