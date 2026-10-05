---
id: "zep-floating-point-services-unshared-fp-registers-mode"
type: "concept"
domain: "rtos"
title: "Floating Point Services: Concepts / Unshared FP registers mode"
summary: "This mode is used when the application has only a single thread that uses floating point registers."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

This mode is used when the application has only a single thread
that uses floating point registers.

On x86 platforms, the kernel initializes the floating point registers so they can
be used by any thread (initialization in skipped on ARM Cortex-M platforms and
ARCv2 platforms). The floating point registers are left unchanged whenever a
context switch occurs.


**Note:** The behavior is undefined, if two or more threads attempt to use the floating point registers, as the kernel does not attempt to detect (or prevent) multiple threads from using these registers.
