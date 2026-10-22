---
id: "zep-atomic-services"
type: "concept"
domain: "rtos"
title: "Atomic Services"
summary: "An atomic variable is one that can be read and modified by threads and ISRs in an uninterruptible manner. It is a 32-bit variable on 32-bit machines and a 64-bit variable on 64-bit machines."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/atomic.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/atomic.rst"
license: "Apache-2.0"
mode: "V"
---

An `atomic variable` is one that can be read and modified
by threads and ISRs in an uninterruptible manner. It is a 32-bit variable on
32-bit machines and a 64-bit variable on 64-bit machines.
