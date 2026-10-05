---
id: "intr-a-practical-guide-to-arm-cortex-m-registers-used-to-configure-cortex-m-exc"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Registers used to configure Cortex-M Exceptions"
summary: "Exceptions are configured on Cortex-M devices using a small set of registers within the System Control Space (SCS). An in-depth list of all the registers involved in exception handling can be found in the ARMv7-M reference manual [^11]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#registers-used-to-configure-cortex-m-exceptions"
license: "CC-BY-SA-4.0"
mode: "V"
---

Exceptions are configured on Cortex-M devices using a small set of registers within the **System
Control Space** (**SCS**). An in-depth list of all the registers involved in exception handling can
be found in the ARMv7-M reference manual [^11]. A great way to build out an understanding of how
the exception subsystem works is to walk through the registers used to configure it. In the
sections below we will explore the highlights.

> If you already have a good feel for Cortex-M exception configuration, I'd recommend skipping to the
> [advanced topics section](#advanced-topics) which covers a few of the more subtle details about Cortex-M exceptions
> worth noting or to test your knowledge with a more [complex configuration example](#complex-config-example)!

{:.no_toc}

{: #icsr-register}

### Interrupt Control and State Register (ICSR) - 0xE000ED04

`ICSR` bit assignments:


This register lets one control the NMI, PendSV, and SysTick exceptions and view a
summary of the current interrupt state of the system.

The most useful status fields are:

- **VECTACTIVE** - The Exception Number of the currently running interrupt or 0 if none are active. This number is also stored in the `IPSR` field of the Program Status Register (`xPSR`).
- **RETTOBASE** - A value of _0_ means another interrupt is active aside from the currently executing
  one. This basically reveals whether or not pre-emption took place. This field is not implemented in ARMv6-M devices.
- **VECTPENDING** - The Exception Number of the highest outstanding pending interrupt or 0 if there is None.

{:.no_toc}

### Application Interrupt and Reset Control Register (AIRCR) - 0xE000ED0C

`AIRCR` bit assignments:


The highlights with respect to exceptions are:

- **SYSRESETREQ** - Writing 1 will trigger a system reset resulting in the System Reset Handler getting invoked.
- **PRIGROUP** - This field lets you split exception priorities into two parts known as the _group
  priority_ and _subpriority_. The setting here indicates how many bits make up the _subpriority_. The _group priority_ is used to control which interrupts can preempt one another. The subpriority controls the order in which exceptions in the same group will be processed. This field is _not_ implemented in ARMv6-M based devices. This can be helpful if you only want certain groups of interrupts to be able to preempt one another.

> NOTE: In order to issue a write to this register, the `VECTKEY` field must be set to `0x05FA`.

{:.no_toc}

### System Handler Priority Register (SHPR1-SHPR3) - 0xE000ED18 - 0xE000ED20

This bank of registers allows for the priority of system faults with configurable priority to be
updated. Note that the register bank index starts at **1** instead of **0**. This is because the
first exception numbers (corresponding to `Reset`, `NMI`, and `Hardfault`, respectively) do _not_ have a
configurable priority so writing to anything in **SHPR0** has no effect.

Each priority configuration occupies 8 bits of a register bank. That means the configuration for
Exception Number 11, `SVCall`, would be in bits 24-32 of `SHPR2`. The default priority value for
all System Exceptions is 0, the highest configurable priority level. For most applications, it's not typical to need and change these values.

{:.no_toc}

### System Handler Control and State Register (SHCSR) - 0xE000ED24

This register lets you view the status of or enable various built in exception handlers:



> NOTE: For ARMv6-M devices the only value which is implemented is `SVCALLPENDED`

{:.no_toc}

### Interrupt Controller Type Register (ICTR) - 0xE000E004

This register allows you to determine the total number of external interrupt lines supported by an implementation. For ARMv6-M devices (Cortex-M0, Cortex-M0+), this register is not implemented because the number is always 32. For other Cortex-M MCUs, up to 496 lines may be supported! The layout of the register looks like this:



The exact number of interrupts supported is easily computed as `32 * (INTLINESNUM + 1)`

{:.no_toc}

### NVIC Registers

The NVIC has sets of registers for configuring the "external" interrupt lines. The address ranges
are allocated to support the maximum number of external interrupts which can be implemented, 496,
but usually a smaller set of the registers will be implemented.

Four of the register types have a single bit allocated per external interrupt. Each type is in a
contiguous bank of 32-bit registers. So if we want to configure **external interrupt 65**, the
configuration will be bit 1 of the 3rd 32-bit register in the
bank. [Recall](#exception-number-diagram) **external
interrupts** start at offset 16 in the vector table so the **Exception Number** (index in the vector
table) for this interrupt will be 16 + 65 = 81.

> NOTE 1: Utilizing an **external interrupt** is usually a little bit more involved than it first
> appear to be. In addition to configuring the NVIC registers for the interrupt, you usually need to
> configure the MCU specific peripheral to generate the interrupt as well.[^12]

> NOTE 2: While less common in real-world applications, it's also possible to re-purpose any NVIC
> interrupt and trigger it via software. We'll walk through an example of this in the code examples later in the article.

{:.no_toc}

#### Interrupt Set-Enable (NVIC_ISER) and Clear-Enable (NVIC_ICER) Registers

- `NVIC_ISER0`-`NVIC_ISER15`: `0xE000E100`-`0xE000E13C`
- `NVIC_ICER0`-`NVIC_ICER15`: `0xE000E180`-`0xE000E1BC`

Writing a 1 to the correct bit offset of the register pair will enable or disable the interrupt and a read will return 1 if the interrupt is enabled.

{:.no_toc}

{: #nvic-ispr}

#### Interrupt Set-Pending (NVIC_ISPR) and Clear-Pending (NVIC_ICPR) Registers

- `NVIC_ISPR0`-`NVIC_ISPR15`: `0xE000E200`-`0xE000E23C`
- `NVIC_ICPR0`-`NVIC_ICPR15`: `0xE000E280`-`0xE000E2BC`

Writing a 1 to the correct bit offset of the register pair will set or clear the pending state of the interrupt and a read will return 1 if the interrupt is already pending.

{:.no_toc}

{: #iabr-register}

#### Interrupt Active Bit Registers (NVIC_IABR)

- `NVIC_IABR0`-`NVIC_IABR15`: `0xE000E300`-`0xE000E33C`

A read only bank of registers which return whether or not the interrupt is active. One thing to note is this register is **not** implemented in the ARMv6-M architecture (Cortex-M0 & Cortex-M0+).

{:.no_toc}

{: #nvic-ipr}

#### Interrupt Priority Registers (NVIC_IPR)

- `NVIC_IPR0`-`NVIC_IPR123`: `0xE000E400`-`0xE000E5EC`

The final NVIC configuration register is used to configure the priority of the interrupt. 8 bits
are used to configure the priority of each interrupt. The number of supported priority levels is
implementation defined and is in the range of 4-256. When less than 256 priority levels are
implemented, the lower bits in the field read-as-zero. So, somewhat confusingly, if only 2 bits are implemented, the valid
values from highest priority to lowest priority would be **0b000.0000** (**0x0**), **0b0100.0000**
(**0x40**), **0b1000.0000** (**0x80**) and **0b1100.0000** (**0xC0**).

{:.no_toc}

### Software Triggered Interrupt Register (STIR) - 0xE000EF00

This register can be used to set an NVIC interrupt to pending. It's equivalent to setting the
appropriate bit in the `NVIC_ISPR` to 1. The value that needs to be written to the register is the
**External Interrupt Number** (**Exception Number - 16**). This register is **not** implemented for the
ARMv6-M architecture

{: #advanced-topics}
