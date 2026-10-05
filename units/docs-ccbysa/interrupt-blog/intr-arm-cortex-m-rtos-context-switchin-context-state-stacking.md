---
id: "intr-arm-cortex-m-rtos-context-switchin-context-state-stacking"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Cortex-M ARM MCU Features / Context State Stacking"
summary: "In our guide about ARM Cortex-M Exception Handling, we touched upon how the hardware itself implements the AAPCS[^1] so that interrupts can be implemented as normal C functions. Here we will expand on what that actually means."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#context-state-stacking"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M ARM MCU Features_

In our
[guide](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#exception-entry--exit)
about ARM Cortex-M Exception Handling, we touched upon how the hardware itself implements the AAPCS[^1]
so that interrupts can be implemented as normal C functions. Here we will expand on what that
actually means.

Per the AAPCS[^1], there is a certain set of registers that a function is responsible for
restoring to their original value before returning to the function which called it:

> A subroutine must preserve the contents of the registers r4-r8, r10, r11 and SP (and r9 in PCS
> variants that designate r9 as v6).

Conversely, this means it is the responsibility of the calling function to preserve the registers not
mentioned, `r0` - `r3`, `r12` and `LR` (`r14`).

The specification also states the "The [C]PSR is a global register" where "the N, Z, C, V and Q
bits (bits 27-31) and the GE[3:0] bits (bits 16-19) are undefined on entry to or return from a
public interface." These bits convey state about recent comparisons, etc. This means it's also the
calling functions responsibility to preserve any state it needs in the register.

The AAPCS also imposes a requirement that "The stack must be double-word aligned." for
"public interfaces" which means when entering a function the stack should always start off 8-byte aligned.

Taking all of these factors into account, in order for execution from an interrupt to be **ABI**
compliant, the ARM architecture needs to align the stack and save the register state that a
calling function is responsible for preserving. To accomplish this, the ARM Cortex-M core will push
that context onto the stack.

> NOTE: The stack data is pushed on is the one which was in use prior to servicing the
> exception. So for example, if the system was in Thread Mode using the `psp` and exception
> takes place, the data will be pushed on the
> `psp`. If the core was already servicing another exception and was preempted by a higher priority exception,
> the data will be pushed on the `msp`.

The reference manual has a great picture of what the stack looks like after this automatic context
state saving takes place:

{: #basic-context-state-frame}


{: #psr-alignment}

> NOTE: On exception entry, the ARM hardware uses bit 9 of the stacked xPSR value to indicate
> whether 4 bytes of padding was added to align the stack on an 8 byte boundary.

#### FP Extension & Context State Stacking

When the **FP Extension** is in use _and_ active, the **AAPCS**[^1] states that `s16` - `s31` must be preserved across
subroutine calls and `s0` - `s15` do not need to be preserved. Additionally, similar to the `PSR`
register, the state of the FPU needs to be preserved so the `FPSCR` needs to be stored as well. This means an additional 17
registers (68 bytes) need to be stacked on exception entry!

Fortunately, the folks at ARM realized this could be a performance or memory problem for some use cases so
there are several really neat ways to optimize this.

As we mentioned [above](#fpu-config-options), one option is to completely disable the FPU. In this
situation no state needs to be preserved.

However, there's also some fine granularity controls about how the context is preserved. These can
be configured via the _Floating Point Context Control Register_ (`FPCCR`) located at address
`0xE000EF34`:



With respect to _Context State Stacking_, the values that are interesting are:

{: #fpca-description}

- `ASPEN` - When set to `1` (default), any execution of a floating point instruction will set the `FPCA` bit in
  the control register we mentioned [above](#control-register).
- `LSPEN` - When set to `1` (default) enables what is known as a **lazy context save**[^5]. Basically what this means is on exception entry, space will be reserved on the stack for the caller saved floating
  point registers (`s0`-`s15` & `FPSCR`) but the data will not actually be pushed by default. If
  and only if a floating point instruction is executed while in the exception, only then will the state be
  pushed. This is pretty sweet because it means as long as an interrupt does not use the FPU, no
  extra interrupt latency penalty is incurred!

When the FPU is "in use" (CONTROL.FPCA=1), an **extended frame** will be saved by the hardware:

{: #extended-context-state-frame}


> NOTE: If the FPU is enabled but no floating point instructions are executed or ASPEN is disabled
> (i.e CONTROL.FPCA=0), only the **basic frame** will be saved. The ARM **lazy context save** application
> note[^5] explores some interesting tricks one can play based on these facts to prevent the
> extended frame from always needing to be allocated even when the FPU is in use.

{: #exc-return-info}

#### Exception Return

Finally, in order for the hardware to figure out what state to restore when exiting an
exception, a special value, known as `EXC_RETURN` needs to be loaded into the link register, `lr`. Typically, this
will just mirror the value in the `lr` on exception entry. However, a different value can also be
manually loaded into the register as well (i.e to change the Thread Mode stack pointer
being used like we discussed [above](#stack-pointers-and-usage)).

On exception entry, the ARM reference manual pseudocode for the value stored in `lr` gives the best description[^6]:

{: #exception-entry-pseudocode}


It describes the current stack frame in use (**Extended** vs **Basic**) as well as what the active
stack pointer was prior to the exception taking place.

When returning from an exception, the possible values and behavior for `EXC_RETURN` are:

| EXC_RETURN Value | Mode to Return To | Stack to use |
| --------------------------- | --------------------------- || --------------------------- |
| 0xFFFFFFF1 | Handler Mode | MSP |
| 0xFFFFFFF9 | Thread Mode | MSP |
| 0xFFFFFFFD | Thread Mode | PSP |
| 0xFFFFFFE1 | Handler Mode (FPU Extended Frame) | MSP |
| 0xFFFFFFE9 | Thread Mode (FPU Extended Frame) | MSP |
| 0xFFFFFFED | Thread Mode (FPU Extended Frame) | PSP |

{: #context-switching}
