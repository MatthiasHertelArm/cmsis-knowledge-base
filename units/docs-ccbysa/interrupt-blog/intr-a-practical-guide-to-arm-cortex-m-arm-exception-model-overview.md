---
id: "intr-a-practical-guide-to-arm-cortex-m-arm-exception-model-overview"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: ARM Exception Model Overview"
summary: "An exception is defined in the ARM specification as \"a condition that changes the normal flow of control in a program\" [^4]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#arm-exception-model-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

An exception is defined in the ARM specification as "a condition that changes the normal flow of
control in a program" [^4].

You will often see the terms "interrupt" and "exception" used interchangeably. However, in the ARM
documentation, "interrupt" is used to describe a type of "exception". Exceptions are identified by the following pieces of information:

{: #exception-number}

- **Exception Number** - A unique number used to reference a particular exception (starting at **1**). This
  number is also used as the offset within the **Vector Table** where the address of
  the routine for the exception can be found. The routine is usually referred to as the **Exception
  Handler** or **Interrupt Service Routine** (**ISR**) and is the function which runs when
  the exception is triggered. The ARM hardware will automatically look up this function pointer
  in the **Vector Table** when an exception is triggered and start executing the code.
- **Priority Level** / **Priority Number** - Each exception has a priority associated with it. For most
  exceptions this number is configurable. Counter-intuitively, the lower the priority number, the
  higher the precedence the exception has. So for example if an exception of priority level 2 and
  level 1 occur at the same time, the level 1 exception will be run first. When we say an exception
  has the "highest priority", it will have the _lowest_ **Priority Number**. If two exceptions have the _same_ **Priority Number**, the exception with the lowest **Exception Number** will run first.
- **Synchronous** or **Asynchronous** - As the name implies, some exceptions will fire immediately
  after an instruction is executed (i.e `SVCall`). These exceptions are referred to as
  _synchronous_. Exceptions that do not fire immediately after a particular code path is executed are
  referred to as _asynchronous_.

An exception can be in one of several states:

- **Pending** - The MCU has detected the exception and scheduled it but has not yet invoked the handler for it.
- **Active** - The MCU has started to run the exception handler but not yet finished executing
  it. It's possible for the exception to have been "pre-empted" by a higher priority handler and be
  in this state.
- **Pending & Active** - Only possible for asynchronous exceptions, this basically means the exception was detected by the MCU again while processing an earlier detected version of the same exception.
- **Inactive** - The exception is neither pending nor active.

Some exceptions can be selectively Enabled or Disabled.

> NOTE: Even while an exception is disabled, it can still reach the **pending** state. Upon being
> enabled it will then transition to active. It's generally a good idea to clear any pending exceptions for an interrupt before enabling it.

Let's explore the different types of exceptions available on ARM Cortex-M MCUs:

{:.no_toc}

### Built in Exceptions

These are exceptions that are part of _every_ ARM Cortex-M core. The ARM Cortex-M specifications
reserve **Exception Numbers** **1**-**15**, inclusive, for these.

> NOTE: [Recall](#exception-number) that the **Exception Number** maps to an offset within the **Vector Table**. Index 0 of
> the **Vector Table** holds the reset value of the Main stack pointer. The rest of the **Vector
> Table**, starting at Index 1, holds **Exception Handler** pointers.

Six exceptions are always supported and depending on the Cortex-M variant, additional
handlers will be implemented as well. The minimum set is:

- **Reset** - This is the routine executed when a chip comes out of reset. More details can be found within the [Zero to main() series of posts]().
- **Non Maskable Interrupt** (`NMI`) - As the name implies, this interrupt cannot be disabled. If
  errors happen in other exception handlers, a NMI will be triggered. Aside from the `Reset`
  exception, it has the highest priority of all exceptions.
- **HardFault** - The catchall for assorted system failures that can take place such as accesses to
  bad memory, divide-by-zero errors and illegal unaligned accesses. It's the only handler for
  faults on the ARMv6-M architecture but for ARMv7-M & ARMv8-M, finer granularity fault handlers
  can be enabled for specific error classes (i.e `MemManage`, `BusFault`, `UsageFault`). [^3]
- **SVCall** - Exception handler invoked when an _Supervisor Call_ (`svc`) instruction is executed.
- **PendSV** & **SysTick** - System level interrupts triggered by software. They are typically used
  when running a RTOS to manage when the scheduler runs and when context switches take place.

{:.no_toc}

### External Interrupts

ARM cores also support interrupt lines which are "external" to the core itself. These interrupt
lines are usually routed to vendor-specific peripherals on the MCU such as Direct Memory Access (**DMA**)
engines or General Purpose Input/Output Pins (**GPIO**s). All of these interrupts are configured via a peripheral known as the _Nested Vectored Interrupt Controller_ (**NVIC**).

The **Exception Number** for external interrupts starts at **16**. The ARMv7-M reference manual has a good graphic which displays the Exception number mappings:

{: #exception-number-diagram}

