---
id: "zep-kernel-objects"
type: "concept"
domain: "rtos"
title: "Kernel Objects"
summary: "A kernel object can be one of three classes of data:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/kernelobjects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/kernelobjects.rst"
license: "Apache-2.0"
mode: "V"
---

A kernel object can be one of three classes of data:

* A core kernel object, such as a semaphore, thread, pipe, etc.
* A thread stack, which is an array of `z_thread_stack_element`
  and declared with `K_THREAD_STACK_DEFINE()`
* A device driver instance (const struct device) that belongs to one of a defined
  set of subsystems

The set of known kernel objects and driver subsystems is defined in
`include/zephyr/sys/kobject.h` as `k_objects`.

Kernel objects are completely opaque to user threads. User threads work
with addresses to kernel objects when making API calls, but may never
dereference these addresses, doing so will cause a memory protection fault.
All kernel objects must be placed in memory that is not accessible by
user threads.

Since user threads may not directly manipulate kernel objects, all use of
them must go through system calls. In order to perform a system call on
a kernel object, checks are performed by system call handler functions
that the kernel object address is valid and that the calling thread
has sufficient permissions to work with it.

Permission on an object also has the semantics of a reference to an object.
This is significant for certain object APIs which do temporary allocations,
or objects which themselves have been allocated from a runtime memory pool.

If an object loses all references, two events may happen:

* If the object has an associated cleanup function, the cleanup function
  may be called to release any runtime-allocated buffers the object was using.

* If the object itself was dynamically allocated, the memory for the object
  will be freed.
