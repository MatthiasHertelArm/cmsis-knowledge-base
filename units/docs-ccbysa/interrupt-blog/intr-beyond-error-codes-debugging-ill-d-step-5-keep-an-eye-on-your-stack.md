---
id: "intr-beyond-error-codes-debugging-ill-d-step-5-keep-an-eye-on-your-stack"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 5 - Keep an Eye on Your Stack"
summary: "I've created a general rule for myself: Whenever there's a hideous, hard-to-repeat, totally illogical, nonsensical issue happening in my firmware, I take a breath and ask myself: Is there any possibility I'm overflowing my stack?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-5-keep-an-eye-on-your-stack"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

I've created a general rule for myself: Whenever there's a hideous,
hard-to-repeat, totally illogical, nonsensical issue happening in my firmware, I
take a breath and ask myself: Is there any possibility I'm overflowing my stack?
Several times, the answer to that question has been a resounding "yes". Catching
and debugging stack overflows is a topic that deserves an entire article;
however, there are a couple of easy things to try that might help answer this
question.

Do you know where your stack(s) live? This sounds like a silly question,
however, there are _many_ different potential configurations for where a stack
lives in memory _especially_ if you're using an RTOS. This involves looking into
your
[startup code](https://embeddedartistry.com/blog/2019/04/08/a-general-overview-of-what-happens-before-main/)
to see where the initial stack pointer gets set and where that address comes
from (hardcoded, linker symbol, etc.). In an RTOS that performs context
switching, there will generally be a different stack for each thread/task in
your system, _any_ of which can overflow.

The easiest way to start probing for a potential stack overflow is to make your
stack(s) bigger and see if that resolves the problem. More precise methods for
catching overflows involve using "canary values" near the end of your stack or
utilizing the MPU to generate a fault if the stack overflows into a forbidden
region.
[This article](https://embeddedartistry.com/blog/2020/05/18/implementing-stack-smashing-protection-for-microcontrollers-and-embedded-artistrys-libc/)
on Embedded Artistry details the "canary method" while
[this article](https://www.iar.com/knowledge/learn/programming/rtos-detecting-stack-overflows-part-2)
discusses utilizing the MPU, among other methods. Another thing to note is that
if utilizing an RTOS, you may already have access to some optional stack
overflow protection checks (usually at the cost of performance). For instance,
FreeRTOS
[offers stack protection](https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/09-Memory-management/02-Stack-usage-and-stack-overflow-checking)
features.

Knowing where your stack "starts" and "ends" can be helpful when debugging. If
you can pause on a breakpoint near the point of failure, you can read the stack
pointer to get a glance at how close to an overflow condition you are.

Similarly to the stack, another troublesome piece of memory management could be
our culprit.
