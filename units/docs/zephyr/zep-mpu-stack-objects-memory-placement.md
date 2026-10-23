---
id: "zep-mpu-stack-objects-memory-placement"
type: "concept"
domain: "rtos"
title: "MPU Stack Objects: Memory Placement"
summary: "During stack creation, a set of constraints are enforced on the allocation of memory. These constraints include determining the alignment of the stack and the correct sizing of the stack."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/mpu_stack_objects.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/mpu_stack_objects.rst"
license: "Apache-2.0"
mode: "V"
---

During stack creation, a set of constraints are enforced on the allocation of
memory.  These constraints include determining the alignment of the stack and
the correct sizing of the stack.  During linking of the binary, these
constraints are used to place the stacks properly.

The main source of the memory constraints is the MPU design for the SoC.  The
MPU design may require specific constraints on the region definition.  These
can include alignment of beginning and end addresses, sizes of allocations,
or even interactions between overlapping regions.

Some MPUs require that each region be aligned to a power of two.  These SoCs
will have `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT` defined.
This means that a 1500 byte stack should be aligned to a 2kB boundary and the
stack size should also be adjusted to 2kB to ensure that nothing else is
placed in the remainder of the region.  SoCs which include the unmodified ARM
v7m MPU will have these constraints.

Some ARM MPUs use start and end addresses to define MPU regions and both the
start and end addresses require 32 byte alignment.  An example of this kind of
MPU is found in the NXP FRDM K64F.

MPUs may have a region priority mechanisms that use the highest priority region
that covers the memory access to determine the enforcement policy.  Others may
logically OR regions to determine enforcement policy.

Size and alignment constraints may result in stack allocations being larger
than the requested size.  Region priority mechanisms may result in
some added complexity when implementing stack guards.
