---
id: "intr-arm-cortex-m-rtos-context-switchin-cortex-m-arm-mcu-features"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Cortex-M ARM MCU Features"
summary: "To understand how RTOS context switching works for ARM Cortex-M MCUs, it's critical to have foundational knowledge about the primitives the architecture provides to make it possible."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#cortex-m-arm-mcu-features"
license: "CC-BY-SA-4.0"
mode: "V"
---

To understand how RTOS context switching works for ARM Cortex-M MCUs, it's critical to have
foundational knowledge about the primitives the architecture provides to make it possible.

In this section we go through these building blocks by distilling down the information spread
across the ARM Cortex-M reference manuals and the _ARM
Architecture Procedure Calling Standard_ (**AAPCS**)[^1] which defines the _Application Binary
Interface_ (**ABI**) a compiler must abide by for ARM.

> NOTE: If you already have a good understanding of these concepts, feel free to
> [switch over](#context-switching) this section (pun intended).
