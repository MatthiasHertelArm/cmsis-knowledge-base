---
id: "zep-mpu-stack-objects-stack-guards"
type: "concept"
domain: "rtos"
title: "MPU Stack Objects: Stack Guards"
summary: "Stack protection mechanisms require hardware support that can restrict access to memory. Memory protection units can provide this kind of support. The MPU provides a fixed number of regions."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/mpu_stack_objects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/mpu_stack_objects.rst"
license: "Apache-2.0"
mode: "V"
---

Stack protection mechanisms require hardware support that can restrict access
to memory.  Memory protection units can provide this kind of support.
The MPU provides a fixed number of regions.  Each region contains information
about the start, end, size, and access attributes to be enforced on that
particular region.

Stack guards are implemented by using a single MPU region and setting the
attributes for that region to not allow write access.  If invalid accesses
occur, a fault ensues.  The stack guard is defined at the bottom (the lowest
address) of the stack.
