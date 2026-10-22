---
id: "zep-atomic-services-concepts"
type: "concept"
domain: "rtos"
title: "Atomic Services: Concepts"
summary: "Any number of atomic variables can be defined (limited only by available RAM)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/atomic.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/atomic.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of atomic variables can be defined (limited only by available RAM).

Using the kernel's atomic APIs to manipulate an atomic variable
guarantees that the desired operation occurs correctly,
even if higher priority contexts also manipulate the same variable.

The kernel also supports the atomic manipulation of a single bit
in an array of atomic variables.
