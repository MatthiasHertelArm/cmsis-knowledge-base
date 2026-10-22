---
id: "zep-mutexes"
type: "concept"
domain: "rtos"
title: "Mutexes"
summary: "A mutex is a kernel object that implements a traditional reentrant mutex. A mutex allows multiple threads to safely share an associated hardware or software resource by ensuring mutually exclusive access to the resource."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/mutexes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/mutexes.rst"
license: "Apache-2.0"
mode: "V"
---

A `mutex` is a kernel object that implements a traditional
reentrant mutex. A mutex allows multiple threads to safely share
an associated hardware or software resource by ensuring mutually exclusive
access to the resource.
