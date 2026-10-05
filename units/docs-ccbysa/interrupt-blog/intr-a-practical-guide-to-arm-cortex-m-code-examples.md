---
id: "intr-a-practical-guide-to-arm-cortex-m-code-examples"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Code Examples"
summary: "For this setup we will use a nRF52840-DK[^6] running the blinky demo application from the v15.2 SDK[^7] with a modified main.c that can be found here."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#code-examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

For this setup we will use a nRF52840-DK[^6] running the blinky demo application from the v15.2
SDK[^7] with a modified main.c that can be found
[here](https://github.com/memfault/interrupt/tree/master/example/arm-cortex-m-exceptions/main.c). However,
you should be able to run similar code snippets on pretty much any Cortex-M MCU.

We'll use SEGGER's JLinkGDBServer[^9] as our debugger to step through these examples.

{:.no_toc}
