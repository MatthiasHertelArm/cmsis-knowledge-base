---
id: "zep-overview-constraints"
type: "concept"
domain: "rtos"
title: "Overview: Constraints"
summary: "All kernel objects, thread stacks, and device driver instances must be defined at build time if they are to be used from user mode. Dynamic use-cases for kernel objects will need to go through pre-defined pools of available objects."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/overview.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/overview.rst"
license: "Apache-2.0"
mode: "V"
---

All kernel objects, thread stacks, and device driver instances must be defined
at build time if they are to be used from user mode. Dynamic use-cases for
kernel objects will need to go through pre-defined pools of available objects.

There are some constraints if additional application binary data is loaded
for execution after the kernel starts:

- Loaded object code will not be able to define any kernel objects that will be
  recognized by the kernel. This code will instead need to use APIs for
  requesting kernel objects from pools.

- Similarly, since the loaded object code will not be part of the kernel build
  process, this code will not be able to install interrupt handlers,
  instantiate device drivers, or define system calls, regardless of what
  mode it runs in.

- Loaded object code that does not come from a verified source should always
  be entered with the CPU already in user mode.
