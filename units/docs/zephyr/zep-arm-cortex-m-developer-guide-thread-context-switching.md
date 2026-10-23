---
id: "zep-arm-cortex-m-developer-guide-thread-context-switching"
type: "concept"
domain: "rtos"
title: "Arm Cortex-M Developer Guide: OS features / Thread context switching"
summary: "In Arm Cortex-M builds, the PendSV exception is used in order to trigger a context switch to a different thread. PendSV exception is always present in Cortex-M implementations."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/arm_cortex_m.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/arm_cortex_m.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: OS features_

In Arm Cortex-M builds, the PendSV exception is used in order to trigger a context switch to a different thread.
PendSV exception is always present in Cortex-M implementations. PendSV is configured with the lowest possible
interrupt priority level, in all Cortex-M variants. The main reasons for that design are

* to utilize the tail chaining feature of Cortex-M processors, and thus limit the number of context switch
  operations that occur.
* to not impact the interrupt latency observed by HW interrupts.

As a result, context switch in Cortex-M is non-atomic, i.e. it may be *preempted* by HW interrupts,
however, a context-switch operation must be completed before a new thread context-switch may start.

Typically a thread context-switch will perform the following operations

* When switching-out the current thread, the processor stores

   * the callee-saved registers (R4 - R11) in the thread's container for callee-saved registers,
     which is located in kernel memory
   * the thread's current operation *mode*

        * user or privileged execution mode
        * presence of an active floating point context
        * the EXC_RETURN value of the current handler context (PendSV)

   * the floating point callee-saved registers (S16 - S31) in the thread's container for FP
     callee-saved registers, if the current thread has an active FP context
   * the PSP of the current thread which points to the beginning of the current thread's exception
     stack frame. The latter contains the caller-saved context and the return address of the switched-out
     thread.

* When switching-in a new thread the processor

   * restores the new thread's callee-saved registers from the thread's
     container for callee-saved registers
   * restores the new thread's operation *mode*
   * restores the FP callee-saved registers if the switched-in thread had
     an active FP context before being switched-out
   * re-programs the dynamic MPU regions to allow a user thread access its stack and application
     memories, and/or programs a stack-overflow MPU guard at the bottom of the thread's
     privileged stack
   * restores the PSP for the incoming thread and re-programs the stack pointer limit
     register (if applicable, see `CONFIG_BUILTIN_STACK_GUARD`)
   * optionally does a stack limit checking for the switched-in thread, if
     sentinel-based stack limit checking is enabled (see `CONFIG_STACK_SENTINEL`).

PendSV exception return sequence restores the new thread's caller-saved registers and the
return address, as part of unstacking the exception stack frame.

The implementation of the context-switch mechanism is present in
`arch/arm/core/cortex_m/swap_helper.S`.


#### Stack limit checking (Arm v8-M)


Armv8-M and Armv8.1-M variants support stack limit checking using the MSPLIM and PSPLIM
core registers. The feature is enabled when `CONFIG_BUILTIN_STACK_GUARD` is set.
When stack limit checking is enabled, both the thread's privileged or user stack, as well
as the interrupt stack are guarded by PSPLIM and MSPLIM registers, respectively. MSPLIM is
configured *once* during kernel boot, while PSLIM is re-programmed during every thread
context-switch or during system calls, when the thread switches from using its default
stack to using its privileged stack, and vice versa. PSPLIM re-programming

* has a relatively low runtime overhead (programming is done with MSR instructions)
* does not impact interrupt latency
* does not require any memory areas to be reserved for stack guards
* does not make use of MPU regions

It is, therefore, considered as a lightweight but very efficient stack overflow
detection mechanism in Cortex-M applications.

Stack overflows trigger the dedicated UsageFault exception provided by Arm v8-M.
