---
id: "zep-floating-point-services-concepts"
type: "concept"
domain: "rtos"
title: "Floating Point Services: Concepts"
summary: "The kernel can be configured to provide only the floating point services required by an application. Three modes of operation are supported, which are described below."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/float.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/float.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel can be configured to provide only the floating point services
required by an application. Three modes of operation are supported,
which are described below. In addition, the kernel's support for the SSE
registers can be included or omitted, as desired.

A thread's participation in floating point context preservation can also be
managed at run time. `k_float_enable` enables preservation for a thread
and accepts options -- such as `K_FP_REGS` and `K_SSE_REGS` --
that select which register sets are preserved, while `k_float_disable`
turns preservation off again. On targets that do not implement floating point
context management these routines return `-ENOTSUP`, and they return
`-EINVAL` if the request is otherwise invalid and cannot be performed.
