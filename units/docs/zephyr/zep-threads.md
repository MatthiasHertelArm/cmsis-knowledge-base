---
id: "zep-threads"
type: "concept"
domain: "rtos"
title: "Threads"
summary: "This section describes kernel services for creating, scheduling, and deleting independently executable threads of instructions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

**Note:** There is also limited support for using nothread.

This section describes kernel services for creating, scheduling, and deleting
independently executable threads of instructions.

A `thread` is a kernel object that is used for application processing
that is too lengthy or too complex to be performed by an ISR.

Any number of threads can be defined by an application (limited only by
available RAM). Each thread is referenced by a `thread id` that is assigned
when the thread is spawned.

A thread has the following key properties:

* A **stack area**, which is a region of memory used for the thread's stack.
  The **size** of the stack area can be tailored to conform to the actual needs
  of the thread's processing. Special macros exist to create and work with
  stack memory regions.

* A **thread control block** for private kernel bookkeeping of the thread's
  metadata. This is an instance of type `k_thread`.

* An **entry point function**, which is invoked when the thread is started.
  Up to 3 **argument values** can be passed to this function.

* A **scheduling priority**, which instructs the kernel's scheduler how to
  allocate CPU time to the thread. (See scheduling_v2.)

* A set of **thread options**, which allow the thread to receive special
  treatment by the kernel under specific circumstances.
  (See thread_options_v2.)

* A **start delay**, which specifies how long the kernel should wait before
  starting the thread.

* An **execution mode**, which can either be supervisor or user mode.
  By default, threads run in supervisor mode and allow access to
  privileged CPU instructions, the entire memory address space, and
  peripherals. User mode threads have a reduced set of privileges.
  This depends on the `CONFIG_USERSPACE` option. See usermode_api.
