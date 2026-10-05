---
id: "zep-kernel-timing-uptime"
type: "concept"
domain: "rtos"
title: "Kernel Timing: Uptime"
summary: "The kernel tracks a system uptime count on behalf of the application. This is available at all times via k_uptime_get, which provides an uptime value in milliseconds since system boot."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/clocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/clocks.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel tracks a system uptime count on behalf of the application.
This is available at all times via `k_uptime_get`, which
provides an uptime value in milliseconds since system boot.  This is
expected to be the utility used by most portable application code.

The internal tracking, however, is as a 64 bit integer count of ticks.
Apps with precise timing requirements (that are willing to do their
own conversions to portable real time units) may access this with
`k_uptime_ticks`.

`k_uptime_delta` can be used to get the time elapsed between a reference
and the current time. The referenced time will be updated to the current uptime,
to easily calculate the next elapsed time.
