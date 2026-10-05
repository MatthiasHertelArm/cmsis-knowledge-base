---
id: "intr-a-simple-scheduler-via-an-interrup-the-hardware-scheduler"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model: The Hardware Scheduler"
summary: "Before we dive into our interrupt scheduler, let's look at how the typical preemptive RTOS scheduler works. First, it keeps a set of threads with some user-defined priority. Second, threads may activate each other, either directly or indirectly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler#the-hardware-scheduler"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we dive into our interrupt scheduler, let's look at how the typical preemptive RTOS scheduler works. First, it keeps a set of threads with some user-defined priority. Second, threads may activate each other, either directly or indirectly. Third, the scheduler is responsible for ensuring that the most prioritized thread will be active and activation of other threads will trigger 'rescheduling' and possibly preemption of the currently active one.

If you look at the programmer's model of interrupt controllers like [NVIC](https://developer.arm.com/documentation/ddi0337/e/Nested-Vectored-Interrupt-Controller?lang=en) or GIC, you will notice that these devices do exactly that. For example, in the NVIC case, the device contains a set of registers describing the state of interrupt vectors, their priorities, and so on. Also, it has a special register called STIR (Software Trigger Interrupt Register). Writing a vector number to that register causes the corresponding interrupt to be activated in the same way as hardware does. Since the user can also change the priority of interrupts, the interrupt controller itself may be treated as a simple scheduler or an implementation of the so-called [actor model](https://en.wikipedia.org/wiki/Actor_model) in a **hardware** peripheral.
