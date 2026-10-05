---
id: "intr-how-to-debug-a-hardfault-on-an-arm"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU"
summary: "Faults happen on embedded devices all the time for a variety of reasons -- ranging from something as simple as a NULL pointer dereference to something more unexpected like running a faulty code path only when in a …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug"
license: "CC-BY-SA-4.0"
mode: "V"
---

Faults happen on embedded devices all the time for a variety of reasons -- ranging from
something as simple as a NULL pointer dereference to something more unexpected like
running a faulty code path only when in a zero-g environment on the Tower of Terror in
Disneyland[^14]. It's important for any embedded engineer to understand how to debug and resolve
this class of issue quickly.



In this article, we explain how to debug faults on ARM Cortex-M based devices. In the process, we
learn about fault registers, how to automate fault analysis, and figure out ways to recover from
some faults without rebooting the MCU. We include practical examples, with a step by step walk-through on how to investigate them.



> If you'd rather listen to me present this information and see some demos in action, [watch this webinar recording.](https://go.memfault.com/debugging-arm-cortex-m-mcu-webinar?utm_campaign=Debugging%20Cortex%20M%20Webinar&utm_source=blog&utm_medium=Interrupt&utm_term=Debug)
