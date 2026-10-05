---
id: "intr-a-practical-guide-to-arm-cortex-m"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling"
summary: "Nearly all embedded systems at one point or another rely on the ability to handle asynchronous events."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic"
license: "CC-BY-SA-4.0"
mode: "V"
---

Nearly all embedded systems at one point or another rely on the ability to handle asynchronous
events. For example, it could be reading external sensor data from an accelerometer in order to
count steps or handling periodic timer events to trigger a context switch for an RTOS.



In this article we will dive into the details of how the ARM Cortex-M _exception model_ supports
the handling of asynchronous events. We
will walk through different exception types supported, terminology (i.e. NVIC, ISR, Priority), the
configuration registers used & common settings, advanced topics to be aware of regarding exceptions
and a few examples written in C.



Note: For the most part, the exception handling mechanism in all Cortex-M processors (ARMv6-M,
ARMv7-M & ARMv8-M architectures) is the same. I will point out differences that do arise in the relevant sections below.

> If you'd rather listen to me present this information and see some demos in action, [watch this webinar recording.](https://go.memfault.com/debugging-arm-cortex-m-mcu-webinar?utm_campaign=Debugging%20Cortex%20M%20Webinar&utm_source=blog&utm_medium=Interrupt&utm_term=Debug)
