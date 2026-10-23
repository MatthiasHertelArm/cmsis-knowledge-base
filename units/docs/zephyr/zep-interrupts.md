---
id: "zep-interrupts"
type: "concept"
domain: "rtos"
title: "Interrupts"
summary: "An interrupt service routine (ISR) is a function that executes asynchronously in response to a hardware or software interrupt. An ISR normally preempts the execution of the current thread, allowing the response to occur with very low latency."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

An `interrupt service routine` (ISR) is a function that executes
asynchronously in response to a hardware or software interrupt.
An ISR normally preempts the execution of the current thread,
allowing the response to occur with very low latency.
Thread execution resumes only once all ISR work has been completed.
