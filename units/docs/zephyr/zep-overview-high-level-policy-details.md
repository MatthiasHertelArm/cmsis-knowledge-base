---
id: "zep-overview-high-level-policy-details"
type: "concept"
domain: "rtos"
title: "Overview: High-level Policy Details"
summary: "Broadly speaking, we accomplish these thread-level memory protection goals through the following mechanisms:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/overview.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/overview.rst"
license: "Apache-2.0"
mode: "V"
---

Broadly speaking, we accomplish these thread-level memory protection goals
through the following mechanisms:

- Any user thread will only have access to a subset of memory:
  typically its stack, program text, read-only data, and any partitions
  configured in the memory_domain it belongs to. Access to any other RAM
  must be done on the thread's behalf through system calls, or specifically
  granted by a supervisor thread using the memory domain APIs. Newly created
  threads inherit the memory domain configuration of the parent. Threads may
  communicate with each other by having shared membership of the same memory
  domains, or via kernel objects such as semaphores and pipes.

- User threads cannot directly access memory belonging to kernel objects.
  Although pointers to kernel objects are used to reference them, actual
  manipulation of kernel objects is done through system call interfaces. Device
  drivers and threads stacks are also considered kernel objects. This ensures
  that any data inside a kernel object that is private to the kernel cannot be
  tampered with.

- User threads by default have no permission to access any kernel object or
  driver other than their own thread object. Such access must be granted by
  another thread that is either in supervisor mode or has permission on both
  the receiving thread object and the kernel object being granted access to.
  The creation of new threads has an option to automatically inherit
  permissions of all kernel objects granted to the parent, except the parent
  thread itself.

- For performance and footprint reasons Zephyr normally does little or no
  parameter error checking for kernel object or device driver APIs. Access from
  user mode through system calls involves an extra layer of handler functions,
  which are expected to rigorously validate access permissions and type of
  the object, check the validity of other parameters through bounds checking or
  other means, and verify proper read/write access to any memory buffers
  involved.

- Thread stacks are defined in such a way that exceeding the specified stack
  space will generate a hardware fault. The way this is done specifically
  varies per architecture.
