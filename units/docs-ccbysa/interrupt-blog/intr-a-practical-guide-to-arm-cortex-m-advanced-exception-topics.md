---
id: "intr-a-practical-guide-to-arm-cortex-m-advanced-exception-topics"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Advanced Exception Topics"
summary: "One of my favorite parts about ARM exception entry is that the hardware itself implements the ARM Architecture Procedure Calling Standard (AAPCS). [^5] The AAPCS specification defines a set of conventions that must be followed by compilers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#advanced-exception-topics"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Exception Entry & Exit

One of my favorite parts about ARM exception entry is that the hardware itself implements the ARM
Architecture Procedure Calling Standard (AAPCS). [^5] The AAPCS specification defines a set of conventions that must
be followed by compilers. One of these requirements is around the registers which must be saved by
a C function when calling another function. When an exception is invoked, the hardware will
automatically stack the registers that are caller-saved. The hardware will then encode in the link register (`$lr`) a value known as the `EXC_RETURN` value. This value tells the ARM core that a return from an exception is taking place and the core can then unwind the stack and return correctly to the code which was running before the exception took place

By leveraging these features, exceptions and thread mode code can share the same set of registers _and_ exception entries can be regular C functions! For other architectures, exception handlers often have to be written in assembly.

### Tail-Chaining

Usually when exiting an exception, the hardware needs to pop and
restore at least eight caller-saved registers. However, when exiting an ISR while a new exception is already
pended, this pop and subsequent push can be skipped since it would be
popping and then pushing the exact same registers! This optimization
is known as "Tail-Chaining".

For example, on a Cortex-M3, when using zero
wait state memory, it takes 12 clock cycles to start executing an ISR after it has been asserted
and 12 cycles to return from the ISR upon its completion. When the register pop and push is skipped,
it only takes 6 cycles to exit from one exception and start another one, saving 18 cycles in total!

### Late-arriving Preemption

The ARM core can detect a higher priority exception while in the "exception entry phase"
(stacking caller registers & fetching the ISR routine to execute). A "late arriving" interrupt is detected during
this period. The optimization is that the higher priority ISR can be fetched and executed but the
register state saving that has already taken place can be skipped. This reduces the latency for the
higher priority interrupt and, conveniently, upon completion of
the late arriving exception handler, the processor can then tail-chain into the initial exception
that was going to be serviced.

### Lazy State Preservation

ARMv7 & ARMv8 devices can implement an optional **Floating Point Unit** (`FPU`) for native floating
point support. This comes with the addition of 33 four-byte registers (`s0`-`s31` & `fpscr`). 17 of
these are "caller" saved and need to be dealt with by the ARM exception entry handler. Since FPU
registers are not often used in ISRs, there is an optimization ("lazy context save")[^10] that can be enabled which defers the
actual saving of the FPU registers on the stack until a floating point instruction is used in the
exception. By deferring the actual push of the registers, interrupt latency can usually be reduced by
the push and pop of these 17 registers!

> A full discussion of FPU stacking optimizations is outside the scope of this article but better managing how the
> registers are stacked can also be a very helpful tool for reducing stack overflows and memory usage in embedded
> environments ... Preserving FPU state across RTOS context switches requires an additional 132 bytes (33
> registers) of data to be tracked for each thread! For further reading, ARM wrote a great
> application note highlighting the lazy preservation FPU features.[^8]

### Execution Priority & Priority Boosting

If no exception is active, the current "execution priority" of the system can be thought of as being the
"highest configurable priority level" + 1 -- essentially meaning if any exception is pended, the
currently running code will be interrupted and the ISR will run.

There are a few ways in software that the "execution priority" can be manipulated to be above the
default priority of thread mode or the exception that is active. This is known as "priority
boosting". This can be useful to do in software when running code that _cannot_ be interrupted such
as the logic dealing with context switching in a RTOS.

**Priority boosting** is usually controlled via three register fields:

- **PRIMASK** - Typically configured in code using the CMSIS `__disable_irq()` and `__enable_irq()`
  routines or the `cpsid i` and `cpsie i` assembly instructions directly. Setting the PRIMASK to 1 disables all exceptions
  of **configurable priority**. This means, only `NMI`, `Hardfault`, & `Reset` exceptions can still occur.
- **FAULTMASK** - Typically configured in code using the CMSIS `__disable_fault_irq()` and
  `__enable_fault_irq()` routines or the `cpsid f` and `cpsie f` assembly instructions directly. Setting the FAULTMASK
  disables all exceptions except the `NMI` exception. This register is **not** available for ARMv6-M devices.
- **BASEPRI**- Typically configured using the CMSIS `__set_BASEPRI()` routine. The register can be used to
  prevent exceptions up to a certain priority from being activated. It has no effect when
  set to 0 and can be set anywhere from the highest priority level, N, to 1. It's also **not** available for
  ARMv6-M based MCUs.

### Interruptible-continuable instructions

Most ARM instructions run to completion before an interrupt is executed and are atomic. For
example, any aligned 32-bit memory access is an atomic operation. However, to minimize interrupt
latency, some of the longer multi-cycle instructions can be aborted and
re-started after the exception completes. These include divide instructions (`udiv` & `sdiv`) and double
word load/store instructions (`ldrd` & `strd`).

Some instructions are also
"interruptible-continuable" which means they can be interrupted but will resume from where they
left off on exception return. These include the Load and Store Multiple registers instructions
(`ldm` and `stm`). This feature is **not** supported for ARMv6-M and instead the instructions will just
be aborted and restarted.

> NOTE: It's generally a good idea to refrain from using load-multiple or store-multiple instructions to
> memory regions or variables where repeated reads or writes could cause issues or to guard these
> accesses in a critical section by disabling interrupts.

{: #examples}
