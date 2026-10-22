---
id: "zep-scheduling-configuration-options"
type: "concept"
domain: "rtos"
title: "Scheduling: Configuration Options"
summary: "Although normally reserved for the idle thread, in certain special applications, a thread might want to make the CPU idle."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

* `CONFIG_TIMESLICING`
* `CONFIG_TIMESLICE_SIZE`
* `CONFIG_TIMESLICE_PRIORITY`


# CPU Idling


Although normally reserved for the idle thread, in certain special
applications, a thread might want to make the CPU idle.
