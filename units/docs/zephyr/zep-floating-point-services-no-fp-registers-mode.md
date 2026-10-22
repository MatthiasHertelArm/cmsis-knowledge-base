---
id: "zep-floating-point-services-no-fp-registers-mode"
type: "concept"
domain: "rtos"
title: "Floating Point Services: Concepts / No FP registers mode"
summary: "This mode is used when the application has no threads that use floating point registers. It is the kernel's default floating point services mode."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Concepts_

This mode is used when the application has no threads that use floating point
registers. It is the kernel's default floating point services mode.

If a thread uses any floating point register,
the kernel generates a fatal error condition and aborts the thread.
