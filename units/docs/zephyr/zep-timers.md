---
id: "zep-timers"
type: "concept"
domain: "rtos"
title: "Timers"
summary: "A timer is a kernel object that measures the passage of time using the kernel's system clock."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/timers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/timers.rst"
license: "Apache-2.0"
mode: "V"
---

A `timer` is a kernel object that measures the passage of time
using the kernel's system clock. When a timer's specified time limit
is reached it can perform an application-defined action,
or it can simply record the expiration and wait for the application
to read its status.
