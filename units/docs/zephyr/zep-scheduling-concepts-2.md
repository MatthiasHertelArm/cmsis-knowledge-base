---
id: "zep-scheduling-concepts-2"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts"
summary: "Making the CPU idle causes the kernel to pause all operations until an event, normally an interrupt, wakes up the CPU. In a regular system, the idle thread is responsible for this."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

Making the CPU idle causes the kernel to pause all operations until an event,
normally an interrupt, wakes up the CPU. In a regular system, the idle thread
is responsible for this. However, in some constrained systems, it is possible
that another thread takes this duty.
