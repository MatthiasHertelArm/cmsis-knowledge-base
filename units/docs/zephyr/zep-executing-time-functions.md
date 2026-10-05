---
id: "zep-executing-time-functions"
type: "concept"
domain: "rtos"
title: "Executing Time Functions"
summary: "The timing functions can be used to obtain execution time of a section of code to aid in analysis and optimization."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/timing_functions/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/timing_functions/index.rst"
license: "Apache-2.0"
mode: "V"
---

The timing functions can be used to obtain execution time of
a section of code to aid in analysis and optimization.

Please note that the timing functions may use a different timer
than the default kernel timer, where the timer being used is
specified by architecture, SoC or board configuration.
