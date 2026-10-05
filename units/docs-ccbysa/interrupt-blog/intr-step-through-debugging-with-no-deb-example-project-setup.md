---
id: "intr-step-through-debugging-with-no-deb-example-project-setup"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: Example Project Setup"
summary: "In the following sections, we will explore how to set up Debug monitor mode with a very simple bare-metal application running on a nRF52 using the following tooling:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#example-project-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the following sections, we will explore how to set up Debug monitor mode with a very simple bare-metal application running on a nRF52 using the following tooling:

- a nRF52840-DK[^1] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^2] as our GDBServer (V6.80b)
- GCC 9.3.1 / GNU Arm Embedded Toolchain as our compiler[^3]
- GNU Make as our build system
- the simple CLI shell [we built up in a previous post](https://interrupt.memfault.com/blog/firmware-shell).
- PySerial's `miniterm.py`[^miniterm] to connect to the serial console on the nRF52.

In this article, we will extend upon the [example app we built to explore how breakpoints work](https://interrupt.memfault.com/blog/cortex-m-breakpoints).
