---
id: "intr-a-simple-scheduler-via-an-interrup"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model"
summary: "Using an RTOS is often a tradeoff between the ease of decomposing tasks, with the complexity of the scheduler itself."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler"
license: "CC-BY-SA-4.0"
mode: "V"
---

Using an RTOS is often a tradeoff between the ease of decomposing tasks, with the complexity of the scheduler itself. There exists a middle ground between highly complex systems that may require an RTOS, and simpler ones that can be easily modeled using a super loop.Since ARM is the most popular embedded CPU and almost every ARM processor has a hardware scheduler, it would be interesting to make a compact framework utilizing these features. The most popular approach to RTOS-less event-driven systems is super-loop consuming events produced by interrupts. This article discusses an alternative, more efficient approach in some circumstances. It has less overhead than an RTOS and also benefits event-driven systems.

One of the main benefits of an RTOS is task decomposition to independent concurrent threads with configurable priority. Typically, it enhances the system's maintainability, reduces complexity, and facilitates subsequent development. But this is not free. The RTOS kernel takes up a portion of system resources and introduces new issues because of its complexity. Also, bugs related to concurrency and synchronization are known to be the hardest things to fix. Loop-based solutions are cumbersome and have a bad reputation because they don't respond quickly.

This is why concepts where interrupts are used as the main 'execution engine' are so popular. Interrupts have low overhead, but they allow for preemptive design. In their latest MCU designs, ARM even made handlers that can be written in C. But, writing application logic in interrupt handlers makes it hard to break tasks down, as it might be in the RTOS case. Our goal is to describe an alternative approach that reuses the hardware properties of the interrupt controller to allow both task decomposition and overall framework simplicity.



In this article, we'll weigh the benefits of using the Cortex-M interrupt model as a scheduler and go over a simple implementation of this concept.
