---
id: "intr-arm-cortex-m-rtos-context-switchin-cortex-m-operation-modes"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Cortex-M ARM MCU Features / Cortex-M Operation Modes"
summary: "When a Cortex-M based MCU is running from an exception handler such as an Interrupt Service Routine (ISR), it is known as running in Handler Mode. The rest of the time the MCU runs in Thread Mode."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#cortex-m-operation-modes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M ARM MCU Features_

When a Cortex-M based MCU is running from an exception handler such as an _Interrupt Service
Routine_ (**ISR**), it is known as running in **Handler
Mode**. The rest of the time the MCU runs in **Thread Mode**.

The core can operate at either a **privileged** or **unprivileged** level. Certain instructions and
operations are only allowed when the software is executing as privileged.
For example, unprivileged code may not access NVIC registers. In Handler Mode, the core is
_always_ privileged. In Thread Mode, the software can execute at either level.

Switching Thread Mode from the unprivileged to privileged level
can _only_ happen when running from Handler Mode.

These different configurations enable use cases where certain application code, such as the
RTOS kernel, can be better sandboxed from one another. We will cycle back to this terminology
throughout the article.
