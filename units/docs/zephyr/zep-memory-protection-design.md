---
id: "zep-memory-protection-design"
type: "concept"
domain: "rtos"
title: "Memory Protection Design"
summary: "Zephyr's memory protection design is geared towards microcontrollers with MPU (Memory Protection Unit) hardware."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's memory protection design is geared towards microcontrollers with MPU
(Memory Protection Unit) hardware. We do support some architectures, such as x86,
which have a paged MMU (Memory Management Unit), but in that case the MMU is
used like an MPU with an identity page table.

All of the discussion below will be using MPU terminology; systems with MMUs
can be considered to have an MPU with an unlimited number of programmable
regions.

There are a few different levels on how memory access is configured when
Zephyr memory protection features are enabled, which we will describe here:
