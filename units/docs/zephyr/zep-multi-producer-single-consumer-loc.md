---
id: "zep-multi-producer-single-consumer-loc"
type: "concept"
domain: "rtos"
title: "Multi Producer Single Consumer Lock Free Queue"
summary: "A Multi Producer Single Consumer Lock Free Queue (MPSC) is an lockfree intrusive queue based on atomic pointer swaps as described by Dmitry Vyukov at 1024cores."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/mpsc_lockfree.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/mpsc_lockfree.rst"
license: "Apache-2.0"
mode: "V"
---

A `Multi Producer Single Consumer Lock Free Queue (MPSC)` is an lockfree
intrusive queue based on atomic pointer swaps as described by Dmitry Vyukov
at [1024cores](https://www.1024cores.net/home/lock-free-algorithms/queues/intrusive-mpsc-node-based-queue).
