---
id: "intr-step-through-debugging-with-no-deb-basic-terminology"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: Basic Terminology"
summary: "ARM Cortex-M's support several \"levels\" of debug:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#basic-terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

ARM Cortex-M's support several "levels" of debug:

- **Halting debug** - This is the typical configuration you use with a debugger like GDB. In this mode, the core is
  halted while debugging. This mode requires access to the **Debug Port** via JTAG or SWD. We've
  walked through an overview of how ARM debug interfaces work in [this article](https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces).
- Tracing via the **[ITM](https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m)**,
  **DWT** & **ETM** - These peripherals let you stream instruction execution and data
  accesses while the system is running. Tools such as Lauterbach's Trace32[^8] and SEGGER's JTrace[^9]
  can decode these streams and present results in a GUI on your desktop.
- **Debug monitor mode** - Enables debug on running systems via the DebugMonitor exception
  handler. This can be helpful in scenarios where halting the core will cause timing
  sensitive subsystems to fail or for use cases where connecting a debugger is not feasible.

> It's worth noting that debug monitor support is not available for the ARMv6-M architecture
> (Cortex-M0). However, it is implemented for all other Cortex-M architectures.
