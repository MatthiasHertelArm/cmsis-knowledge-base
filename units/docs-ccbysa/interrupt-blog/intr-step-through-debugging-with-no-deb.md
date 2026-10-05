---
id: "intr-step-through-debugging-with-no-deb"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M"
summary: "Debugging an MCU requires attaching a debugger via JTAG and halting the core. Or does it?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor"
license: "CC-BY-SA-4.0"
mode: "V"
---

Debugging an MCU requires attaching a debugger via JTAG and halting the core. Or does it?

There are many situations where this debug strategy is not feasible such as on

- production units where JTAG has been disabled.
- systems where halting the core causes the subsystem you are trying to debug to
  fault. (i.e Asserts from the NRF52 SoftDevice after halting at a breakpoint[^6])
- remote systems where only a UART or network interface is exposed.

Fortunately, ARM Cortex-M's have us covered!



This week we explore how to debug running systems with ARM Cortex-M's DebugMonitor
exception handler. We cover how to configure the MCU to operate in this mode and walk through an
example of installing breakpoints and single-stepping on a running device!



> In my opinion, DebugMonitor handling is an underutilized feature that can be applied creatively
> for a variety of debug use cases. I hope by the end of this article I can convince you of this as well!
