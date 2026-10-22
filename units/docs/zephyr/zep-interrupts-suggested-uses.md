---
id: "zep-interrupts-suggested-uses"
type: "concept"
domain: "rtos"
title: "Interrupts: Suggested Uses"
summary: "Use a regular or direct ISR to perform interrupt processing that requires a very rapid response, and can be done quickly without blocking."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

Use a regular or direct ISR to perform interrupt processing that requires a
very rapid response, and can be done quickly without blocking.


**Note:** Interrupt processing that is time consuming, or involves blocking, should be handed off to a thread. See Offloading ISR Work for a description of various techniques that can be used in an application.
