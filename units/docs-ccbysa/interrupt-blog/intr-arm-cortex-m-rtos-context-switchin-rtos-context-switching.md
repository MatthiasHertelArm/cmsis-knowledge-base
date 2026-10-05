---
id: "intr-arm-cortex-m-rtos-context-switchin-rtos-context-switching"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: RTOS Context Switching"
summary: "An RTOS at its cores offers several basic primitives:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#rtos-context-switching"
license: "CC-BY-SA-4.0"
mode: "V"
---

An RTOS at its cores offers several basic primitives:

- A **scheduler** capable of **context switching** between different **tasks**. **Tasks** can usually be prioritized and
  at a bare minimum a **scheduler** is usually capable of alternating between **tasks** when new events arrive (i.e a new
  accelerometer sample is available) or when the **task** **yields** its slot.
- Very basic Operating System primitives (such as mutexes/semaphores and a way to pass messages
  between tasks)
- Configuration operations for sandboxing different code from one another by leveraging the
  privilege and access control features the hardware offers.

Schedulers usually come in two main varieties:

- Preemptive - A context switch while a task is "running" if something more important comes up.
- Cooperative - A context switch will never occur while another task is "running". A task must
  explicitly yield for another task to run. Tasks must "co-operate" for everyone to get a chance to run.

When an RTOS scheduler decides a different task should be run than what is currently running, it
will trigger a **context switch**. When switching from one task to another, the "state" of the current
task needs to be preserved in some way. This includes information such as the execution state of the task
(i.e blocked on a mutex, sleeping, etc) and the values of the active hardware registers.

As we alluded to in our
[ARM Cortex-M Exception](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#built-in-exceptions)
article, the `SVCall`, `PendSV`, and `SysTick` interrupts integrated into every Cortex-M device
were explicitly designed to make task management simple. Consequently, the context switching logic
winds up looking extremely similar regardless of the RTOS in use. So if you understand how one
works, you will be able to pretty easily learn how any other one works!

In the sections that follow we will walk through step-by-step how the context switcher within
**FreeRTOS**[^3] works for Cortex-M devices. **FreeRTOS** is a very popular (and open source!) RTOS
found in numerous commercial products. It has a great track record and has been around since
~2003 by Real Time Engineers Ltd. In 2017 the company was acquired by Amazon, who now manages the project.
