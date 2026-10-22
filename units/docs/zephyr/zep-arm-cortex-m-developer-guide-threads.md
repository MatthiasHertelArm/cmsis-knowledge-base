---
id: "zep-arm-cortex-m-developer-guide-threads"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Threads"
summary: "Each Zephyr thread is defined with its own stack memory. By default, Cortex-M enforces a double word thread stack alignment, see CONFIG_STACK_ALIGN_DOUBLE_WORD."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

#### Thread stack alignment


Each Zephyr thread is defined with its own stack memory. By default, Cortex-M enforces a double word thread stack alignment, see
`CONFIG_STACK_ALIGN_DOUBLE_WORD`. If MPU-based HW-assisted stack overflow detection (`CONFIG_MPU_STACK_GUARD`)
is enabled, thread stacks need to be aligned with a larger value, reflected by `CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE`.
In Arm v6-M and Arm v7-M architecture variants, thread stacks are additionally required to align with a value equal to their size,
in applications that need to support user mode (`CONFIG_USERSPACE`). The thread stack sizes in that case need to be a power
of two. This is all reflected by `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT`, that is enforced in Arm v6-M and Arm v7-M
builds with user mode support.


#### Stack pointers


While executing in thread mode the processor is using the Process Stack Pointer (PSP). The processor uses the Main Stack Pointer (MSP)
while executing in handler mode, that is, while servicing exceptions and HW interrupts. Using PSP in thread mode *facilitates thread
stack pointer manipulation* during thread context switching, without affecting the current execution context flow in
handler mode.

In Arm Cortex-M builds a single interrupt stack memory is shared among exceptions and interrupts. The size of the interrupt stack needs
to be selected taking into consideration nested interrupts, each pushing an additional stack frame. Developers can modify the interrupt
stack size using `CONFIG_ISR_STACK_SIZE`.

The interrupt stack is also used during early boot so the kernel can initialize the main thread's stack before switching to the main thread.
