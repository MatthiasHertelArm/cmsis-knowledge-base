---
id: "zep-scheduling-forcing-a-scheduling-decision"
type: "concept"
domain: "rtos"
title: "Scheduling: Concepts / Forcing a Scheduling Decision"
summary: "A thread can force the scheduler to make an immediate scheduling decision on the current CPU by calling k_reschedule."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

A thread can force the scheduler to make an immediate scheduling decision on the
current CPU by calling `k_reschedule`. When invoked from a thread (with
interrupts unlocked) the scheduler runs immediately; when invoked from an ISR the
decision is deferred until the ISR exits.

Unlike `k_yield`, this routine does not guarantee a switch to a thread of
equal or higher priority -- it simply asks the kernel to re-evaluate which thread
should run next given the current state. Most applications never need this
routine.
