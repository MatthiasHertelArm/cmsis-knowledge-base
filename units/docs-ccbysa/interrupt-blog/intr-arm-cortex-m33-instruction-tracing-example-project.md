---
id: "intr-arm-cortex-m33-instruction-tracing-example-project"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Example Project"
summary: "Now that we have put together code to configure and decode MTB info, let's try it out! In the following sections, we will make use of the following setup to examine the MTB:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#example-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have put together code to configure and decode MTB info, let's try it out! In the following sections, we will make use of the following setup to examine the MTB:

- a DA14695 Development Kit – USB[^1] (ARM Cortex-M33) as our development board
- SEGGER JLinkGDBServer[^2] as our gdbserver (V6.84a)
- GCC 9.3.1 / GNU Arm Embedded Toolchain as our compiler[^3]
- GNU Make as our build system
