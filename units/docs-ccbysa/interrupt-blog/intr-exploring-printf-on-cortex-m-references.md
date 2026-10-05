---
id: "intr-exploring-printf-on-cortex-m-references"
type: "concept"
domain: "debug"
title: "Exploring printf on Cortex-M: References"
summary: "Exploring printf on Cortex-M: References"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-20-printf-on-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/printf-on-embedded#references"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [Interrupt: Introduction to ARM Semihosting](https://interrupt.memfault.com/blog/arm-semihosting)
- [Interrupt: From Zero to main(): Bootstrapping libc with Newlib](https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib)
- [libc `setvbuf()` stdlib reference](http://www.cplusplus.com/reference/cstdio/setvbuf/)
- [Newlib `reent.h` header](https://github.com/bminor/newlib/blob/6226bad0eafe762b811c62d1dc096bc0858b0d1a/newlib/libc/include/reent.h)
- [Reentrancy in Newlib](https://www.codeinsideout.com/blog/freertos/reentrant/)
- [MCU on Eclipse: Steps to use FreeRTOS with newlib reentrant Memory Allocation](https://mcuoneclipse.com/2020/11/15/steps-to-use-freertos-with-newlib-reentrant-memory-allocation/)
- [Zephyr Logging Documentation](https://docs.zephyrproject.org/3.4.0/services/logging/index.html#default-frontend)
- [Newlib `_impure_ptr` declaration](https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/reent/impure.c;h=76f67459e48d3efc20698f8fda39620b1359f63f;hb=HEAD#l27)
- [SEGGER ARM Semihosting Wiki](https://wiki.segger.com/Semihosting)
- [ARM Semihosting Documentation](https://developer.arm.com/documentation/dui0375/g/What-is-Semihosting-/What-is-semihosting-)
- [Newlib libc `initialise_monitor_handles()`](https://github.com/bminor/newlib/blob/1a0908203606527b6ac0ed438669b5bcd247a5f9/newlib/libc/sys/arm/syscalls.c#L114-L169)
- [Newlib semihosting `_write` implementation](https://github.com/bminor/newlib/blob/1a0908203606527b6ac0ed438669b5bcd247a5f9/newlib/libc/sys/arm/syscalls.c#L314-L338), and [here](https://github.com/bminor/newlib/blob/69f4c4029183fb26d2fcae00790881620c1978a3/newlib/libc/sys/arm/swi.h#L74-L89)
- [MCU on Eclipse: Tutorial: Using Single Wire Output SWO with ARM Cortex-M and Eclipse](https://mcuoneclipse.com/2016/10/17/tutorial-using-single-wire-output-swo-with-arm-cortex-m-and-eclipse/)
- [SEGGER RTT Wiki](https://wiki.segger.com/RTT)
- [SEGGER RTT download page](https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/#downloading-rtt-target-package)
- [Zephyr SEGGER RTT GitHub repo](https://github.com/zephyrproject-rtos/segger/tree/master/SEGGER)
