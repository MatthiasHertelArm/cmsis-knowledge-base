---
id: "intr-step-through-debugging-with-no-deb-applications"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: Applications"
summary: "There's a couple projects online today that make use of the debug monitor functionality. Notably,"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#applications"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a couple projects online today that make use of the debug monitor functionality. Notably,

- SEGGER ships an SDK[^4] that you compile into your project to enable Monitor Mode Debug support
  with SEGGER's tools. There's quite a few articles about how to make use of it on the NRF5x
  series[^5]. On the NRF52, this let's you set breakpoints in application code without triggering
  asserts in the Soft Device (because all that code runs from a higher priority interrupt).
- The Monitor For Remote Inspection Project on GitHub [^6] exposes a DebugMonitor port which
  implements the GDB Remote Serial Protocol[^7]. When compiled into a project, you can connect GDB
  directly to your board via the UART connection!

There's a lot of additional use cases you may want to include an
implementation for in your system as well. Some of my favorites include:

- exposing a debug interface for third party developers
  on an embedded platform.
- debugging of sealed units where there is only a UART or network interface exposed
- debugging power consumption issues where maintaining a SWD/JTAG connection would ruin attempts
  to monitor the quiescent current because the debug interface itself consumes a lot of power.
