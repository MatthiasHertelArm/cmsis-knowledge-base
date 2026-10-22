---
id: "zep-timers-suggested-uses"
type: "concept"
domain: "rtos"
title: "Timers: Suggested Uses"
summary: "Use a timer to initiate an asynchronous operation after a specified amount of time."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/timers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/timers.rst"
license: "Apache-2.0"
mode: "V"
---

Use a timer to initiate an asynchronous operation after a specified
amount of time.

Use a timer to determine whether or not a specified amount of time has
elapsed.  In particular, timers should be used when higher precision
and/or unit control is required than that afforded by the simpler
`k_sleep` and `k_usleep` calls.

Use a timer to perform other work while carrying out operations
involving time limits.


**Note:** If a thread needs to measure the time required to perform an operation it can read the system clock or the hardware clock directly, rather than using a timer.
