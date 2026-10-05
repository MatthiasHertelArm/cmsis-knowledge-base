---
id: "intr-arm-cortex-m33-instruction-tracing"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger"
summary: "In a previous post, we talked about debugging memory corruption issues by making use of watchpoints."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33"
license: "CC-BY-SA-4.0"
mode: "V"
---

In a previous post, we talked about debugging memory corruption issues by making use of
[watchpoints](https://interrupt.memfault.com/blog/cortex-m-watchpoints). You may recall in that post we had
to _reproduce_ the failure so we could halt the core with a watchpoint installed in order to debug
what happened.

But what if an issue is hard to reproduce or the device isn't at your desk? In these scenarios, the
execution history (instruction trace) can be invaluable for root causing the underlying issue.



In this post we will explore how to perform instruction tracing without a debugger by using the ARM Cortex-M33 Micro Trace Buffer (MTB). We will walk through a few practical examples of how to configure the MTB with Dialog Semiconductor's DA14695 MCU.



> Note: The Micro Trace Buffer (MTB) is an optional feature of the ARM architecture. Many silicon vendors do not include the feature in their MCUs. Kudos to Dialog for doing so!
