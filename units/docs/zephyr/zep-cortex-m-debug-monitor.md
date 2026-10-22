---
id: "zep-cortex-m-debug-monitor"
type: "concept"
domain: "debug"
title: "Cortex-M Debug Monitor"
summary: "Monitor mode debugging is a Cortex-M feature, that provides a non-halting approach to debugging. With this it's possible to continue the execution of high-priority interrupts, even when waiting on a breakpoint."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/debugmon.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/debugmon.rst"
license: "Apache-2.0"
mode: "V"
---

Monitor mode debugging is a Cortex-M feature, that provides a non-halting approach to
debugging. With this it's possible to continue the execution of high-priority interrupts,
even when waiting on a breakpoint.
This strategy makes it possible to debug time-sensitive software, that would
otherwise crash when the core halts (e.g. applications that need to keep
communication links alive).

Zephyr provides support for enabling and configuring the Debug Monitor exception.
It also contains a ready implementation of the interrupt, which can be used with
SEGGER J-Link debuggers.
