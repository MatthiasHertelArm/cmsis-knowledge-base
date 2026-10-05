---
id: "intr-from-zero-to-main-bare-metal-c"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bare metal C"
summary: "Working on embedded software, one quickly develops a quasi-religious respect for the axioms of embedded C programming:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-14-zero-to-main-1.md"
doc_source: "https://interrupt.memfault.com/blog/zero-to-main-1"
license: "CC-BY-SA-4.0"
mode: "V"
---

Working on embedded software, one quickly develops a quasi-religious respect for
the axioms of embedded C programming:

1. The entry point of thy program shall be named "main".
2. Thou shalt initialize thy static variables, else The Machine shall set them
   to zero.
3. Thou shalt implement The Interrupts. HardFault_Handler chief among them, but
   also SysTick_Handler.

Ask an engineer where those rules come from, and they'll wave towards cryptic startup files implemented in assembly. Often times those files are copy-pasted
from project to project. Seldom are they ever read, let alone modified.


Throughout the [Zero to main() series]() of posts,
we demystify what happens between when power is applied
and your main function is called. In the process, we'll learn how to bootstrap a
C environment, implement a bootloader, relocate code, and more!
