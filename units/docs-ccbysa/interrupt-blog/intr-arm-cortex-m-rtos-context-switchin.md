---
id: "intr-arm-cortex-m-rtos-context-switchin"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching"
summary: "Many embedded systems reach a level of complexity where having a basic set of scheduling primitives and ability to run different tasks can be helpful. The operation of switching from one task to another is known as a context switch."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many embedded systems reach a level of complexity where having a basic set of scheduling primitives
and ability to run different tasks can be helpful. The operation of switching from one task to
another is known as a **context switch**. A _Real Time Operating System_ (**RTOS**) will typically
provide this functionality. Having a foundational knowledge of how the core of an **RTOS** works
can be a valuable skill set for an embedded engineer to have.



In this article we will explore how **context switching** works on ARM Cortex-M MCUs. We will
discuss how the hardware was designed to support this operation, features that impact the context
switching implementation such as the Floating Point Unit (FPU), and common pitfalls seen when
porting an RTOS to a platform. We will also walk through a practical example of analyzing the
**FreeRTOS** context switcher, `xPortPendSVHandler`, utilizing `gdb` to strengthen our understanding.


> If you'd rather listen to me present this information and see some demos in action, [watch this webinar recording.](https://go.memfault.com/debugging-arm-cortex-m-mcu-webinar?utm_campaign=Debugging%20Cortex%20M%20Webinar&utm_source=blog&utm_medium=Interrupt&utm_term=Debug)
