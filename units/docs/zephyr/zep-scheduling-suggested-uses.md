---
id: "zep-scheduling-suggested-uses"
type: "concept"
domain: "rtos"
title: "Scheduling: Suggested Uses"
summary: "Use cooperative threads for device drivers and other performance-critical work."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

Use cooperative threads for device drivers and other performance-critical work.

Use cooperative threads to implement mutual exclusion without the need
for a kernel object, such as a mutex.

Use preemptive threads to give priority to time-sensitive processing
over less time-sensitive processing.
