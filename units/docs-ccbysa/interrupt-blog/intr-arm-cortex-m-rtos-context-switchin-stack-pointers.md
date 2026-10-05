---
id: "intr-arm-cortex-m-rtos-context-switchin-stack-pointers"
type: "concept"
domain: "debug"
title: "ARM Cortex-M RTOS Context Switching: Cortex-M ARM MCU Features / Stack Pointers"
summary: "The Cortex-M architecture implements two stacks known as the Main Stack (tracked in the msp register) and the Process Stack (tracked in the psp register)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-30-cortex-m-rtos-context-switching.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#stack-pointers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M ARM MCU Features_

The Cortex-M architecture implements two stacks known as the _Main Stack_ (tracked in the `msp` register) and the
_Process Stack_ (tracked in the `psp` register). On reset, the **MSP** is always active and its initial value is derived
from the first word in the vector table. When a stack pointer is "active", its current value will
be returned when the `sp` register is accessed.

In Handler Mode, the `msp` is always the stack which is used. In Thread Mode, the stack
pointer which is used can be controlled in two ways:

- Writes of 1 to the `SPSEL` bit in the `CONTROL` register will switch from using the `msp` to the `psp`
- The value placed in `EXC_RETURN` upon exception return. We will expand on this [below](#exc-return-info).

{: #context-state-stacking}
