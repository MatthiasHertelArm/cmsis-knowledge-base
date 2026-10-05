---
id: "intr-a-guide-to-using-arm-stack-limit-r-how-does-it-work"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: How does it work?"
summary: "The best part about this new feature is how easy it is to use and how it takes the guesswork out of debugging stack overflows."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#how-does-it-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

The best part about this new feature is how easy it is to use and how it takes
the guesswork out of debugging stack overflows.

We need to set the PSPLIM, and the MSPLIM registers to the boundary of the
stack. If the MSP == MSPLIM register or the PSP == PSPLIM register, a UsageFault
is generated. The UsageFault Status Register [^m33-usfr] contains a sticky bit
in position four to indicate that a stack overflow occurred.

Having hardware protection for the PSP and MSP allows flexibility within an OS.
For example, we can protect the MSP during exceptions and interrupts. We can
also switch out the PSPLIM value on a context switch to safeguard each task's
stack. If you need a refresher on context switching, check a previous post
[here](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching).

If no RTOS is present, we can still monitor the MSP, as this will protect your
whole application.
