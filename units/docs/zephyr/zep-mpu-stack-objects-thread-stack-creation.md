---
id: "zep-mpu-stack-objects-thread-stack-creation"
type: "concept"
domain: "rtos"
title: "MPU Stack Objects: Thread Stack Creation"
summary: "Thread stacks are declared statically with K_THREAD_STACK_DEFINE()."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/mpu_stack_objects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/mpu_stack_objects.rst"
license: "Apache-2.0"
mode: "V"
---

Thread stacks are declared statically with `K_THREAD_STACK_DEFINE()`.

For architectures which utilize memory protection unit (MPU) hardware,
stacks are physically contiguous allocations.  This contiguous allocation
has implications for the placement of stacks in memory, as well as the
implementation of other features such as stack protection and userspace.  The
implications for placement are directly attributed to the alignment
requirements for MPU regions.  This is discussed in the memory placement
section below.
