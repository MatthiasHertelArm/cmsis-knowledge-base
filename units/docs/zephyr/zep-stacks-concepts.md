---
id: "zep-stacks-concepts"
type: "concept"
domain: "rtos"
title: "Stacks: Concepts"
summary: "Any number of stacks can be defined (limited only by available RAM). Each stack is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/stacks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/stacks.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of stacks can be defined (limited only by available RAM). Each stack
is referenced by its memory address.

A stack has the following key properties:

* A **queue** of integer data values that have been added but not yet removed.
  The queue is implemented using an array of stack_data_t values
  and must be aligned on a native word boundary.
  The stack_data_t type corresponds to the native word size i.e. 32 bits or
  64 bits depending on the CPU architecture and compilation mode.

* A **maximum quantity** of data values that can be queued in the array.

A stack must be initialized before it can be used. This sets its queue to empty.

A data value can be **added** to a stack by a thread or an ISR.
The value is given directly to a waiting thread, if one exists;
otherwise the value is added to the LIFO's queue.


**Note:** If `CONFIG_NO_RUNTIME_CHECKS` is enabled, the kernel will *not* detect and prevent attempts to add a data value to a stack that has already reached its maximum quantity of queued values. Adding a data value to a stack that is already full will result in array overflow, and lead to unpredictable behavior.

A data value may be **removed** from a stack by a thread.
If the stack's queue is empty a thread may choose to wait for it to be given.
Any number of threads may wait on an empty stack simultaneously.
When a data item is added, it is given to the highest priority thread
that has waited longest.


**Note:** The kernel does allow an ISR to remove an item from a stack, however the ISR must not attempt to wait if the stack is empty.
