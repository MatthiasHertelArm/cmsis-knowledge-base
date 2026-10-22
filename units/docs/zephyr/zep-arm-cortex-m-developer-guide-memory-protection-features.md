---
id: "zep-arm-cortex-m-developer-guide-memory-protection-features"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Memory protection features"
summary: "This section describes certain aspects around memory protection features in Arm Cortex-M applications."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

This section describes certain aspects around memory protection features
in Arm Cortex-M applications.


#### User mode system calls


User mode is supported in Cortex-M platforms that implement the standard (Arm) MPU
or a similar core peripheral logic for memory access policy configuration and
control, such as the NXP MPU for Kinetis platforms. (Currently,
`CONFIG_ARCH_HAS_USERSPACE` is selected if `CONFIG_ARM_MPU` is enabled
by the user in the board default Kconfig settings).

A thread performs a system call by triggering a (synchronous) SVC exception, where

* up to 5 arguments are placed on registers R1 - R5
* system call ID is placed on register R6.

The SVC Handler will branch to the system call preparation logic, which will perform
the following operations

* switch the thread's PSP to point to the beginning of the thread's privileged
  stack area, optionally reprogramming the PSPLIM if stack limit checking is enabled
* modify CONTROL register to switch to privileged mode
* modify the return address in the SVC exception stack frame, so that after exception
  return the system call dispatcher is executed (in thread privileged mode)

Once the system call execution is completed the system call dispatcher will restore the
user's original PSP and PSPLIM and switch the CONTROL register back to unprivileged mode
before returning back to the caller of the system call.

System calls execute in thread mode and can be preempted by interrupts at any time. A
thread may also be context-switched-out while doing a system call; the system call will
resume as soon as the thread is switched-in again.

The system call dispatcher executes at SVC priority, therefore it cannot be preempted
by HW interrupts (with the exception of ZLIs), which may observe some additional interrupt
latency if they occur during a system call preparation.


#### MPU-assisted stack overflow detection


Cortex-M platforms with MPU may enable `CONFIG_MPU_STACK_GUARD` to enable the MPU-based
stack overflow detection mechanism. The following points need to be considered when enabling the
MPU stack guards

* stack overflows are triggering processor faults as soon as they occur
* the mechanism is essential for detecting stack overflows in supervisor threads, or
  user threads in privileged mode; stack overflows in threads in user mode will always be
  detected regardless of `CONFIG_MPU_STACK_GUARD` being set.
* stack overflows are always detected, however, the mechanism does not guarantee that
  no memory corruption occurs when supervisor threads overflow their stack memory
* `CONFIG_MPU_STACK_GUARD` will normally reserve one MPU region for programming
  the stack guard (in certain Arm v8-M configurations with `CONFIG_MPU_GAP_FILLING`
  enabled 2 MPU regions are required to implement the guard feature)
* MPU guards are re-programmed at every context-switch, adding a small overhead to the
  thread swap routine. Compared, however, to the `CONFIG_BUILTIN_STACK_GUARD` feature,
  no re-programming occurs during system calls.
* When `CONFIG_HW_STACK_PROTECTION` is enabled on Arm v8-M platforms the native
  stack limit checking mechanism is used by default instead of the MPU-based stack overflow
  detection mechanism; users may override this setting by manually enabling `CONFIG_MPU_STACK_GUARD`
  in these scenarios.
