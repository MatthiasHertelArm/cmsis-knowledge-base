---
id: "zep-interrupts-ram-based-isr-execution"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / RAM-based ISR Execution"
summary: "For ultra-low latency, ISRs and vector tables can be relocated to RAM to eliminate flash access delays. That can be achieved by enabling the CONFIG_SRAM_VECTOR_TABLE and CONFIG_SRAM_SW_ISR_TABLE options which will result in vector tables being placed in RAM."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

For ultra-low latency, ISRs and vector tables can be relocated to RAM to
eliminate flash access delays. That can be achieved by enabling the
`CONFIG_SRAM_VECTOR_TABLE` and
`CONFIG_SRAM_SW_ISR_TABLE` options which will result in vector
tables being placed in RAM.
Then, Zephyr Code and Data Relocation can be
used to relocate the ISR code and all the related symbols to RAM as well.
