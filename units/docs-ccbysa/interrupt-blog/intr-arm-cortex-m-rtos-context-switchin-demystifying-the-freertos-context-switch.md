---
id: "intr-arm-cortex-m-rtos-context-switchin-demystifying-the-freertos-context-switch"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Demystifying the FreeRTOS Context Switcher"
summary: "All the code can be found on the Interrupt Github page with more details in the README in the directory linked."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#demystifying-the-freertos-context-switcher"
license: "CC-BY-SA-4.0"
mode: "V"
---

For this setup we will use:

- a nRF52840-DK[^7] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^8] as our GDB Server.
- GCC 8.3.1 / GNU Arm Embedded Toolchain as our compiler[^9]
- GNU make as our build system

All the code can be found on the
[Interrupt Github page](https://github.com/memfault/interrupt/tree/master/example/freertos-example) with more
details in the `README` in the directory linked.

The example application itself is very basic: it creates a "Ping" **FreeRTOS** task
and a "Pong" **FreeRTOS** task. The "Ping" task sends a message to the "Pong" task
once per second and each time the event loop in a task runs, I've added
a breakpoint instruction so we can confirm with the debugger the tasks are switching between each
other.
