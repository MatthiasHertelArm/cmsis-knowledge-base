---
id: "zep-timers-timer-observers"
type: "concept"
domain: "rtos"
title: "Timers: Timer Observers"
summary: "When CONFIG_TIMER_OBSERVER is enabled, code can register timer observers that are notified of timer lifecycle events across all timers in the system. An observer is a set of optional callbacks invoked when a timer is initialized, started, stopped, or expires."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/timers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/timers.rst"
license: "Apache-2.0"
mode: "V"
---

When `CONFIG_TIMER_OBSERVER` is enabled, code can register
`timer observers` that are notified of timer lifecycle events across all
timers in the system. An observer is a set of optional callbacks invoked when a
timer is initialized, started, stopped, or expires. This allows external modules
-- for example tracing, profiling, or power-management code -- to react to timer
activity without modifying kernel internals or the individual timers.

An observer is defined statically with `K_TIMER_OBSERVER_DEFINE`, which
takes pointers to the `on_init`, `on_start`, `on_stop`, and `on_expiry`
callbacks; any callback that is not needed may be passed as `NULL`. Because the
expiry callback runs in interrupt context, it must be kept short and
non-blocking.
