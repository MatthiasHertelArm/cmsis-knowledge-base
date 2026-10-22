---
id: "zep-system-timer-drivers-timer-driver-locking"
type: "concept"
domain: "rtos"
title: "System Timer Drivers: Timer Driver Locking"
summary: "The kernel exposes a unified timer lock via sys_clock_lock and sys_clock_unlock. This lock protects both the kernel's internal tick accounting (curr_tick, the timeout queue) and any driver-private state that must be consistent with it (e.g. a hardware cycle counter baseline)."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/system_timer_drivers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/system_timer_drivers.rst"
license: "Apache-2.0"
mode: "V"
---

The kernel exposes a unified timer lock via `sys_clock_lock` and
`sys_clock_unlock`.  This lock protects both the kernel's internal
tick accounting (`curr_tick`, the timeout queue) and any driver-private
state that must be consistent with it (e.g. a hardware cycle counter
baseline).

Timer drivers that maintain internal state should acquire this lock at
the start of their ISR, update their hardware state, then pass the lock
key to `sys_clock_announce_locked` which consumes it.  This
ensures that the driver's cycle counter baseline and the kernel's
`curr_tick` are always updated under the same lock, eliminating race
conditions that can arise on SMP systems (or, less commonly, on UP
systems where higher-priority ISRs need consistent realtime references)
when two separate locks are used.

The driver-provided callbacks `sys_clock_set_timeout` and
`sys_clock_elapsed` are always invoked by the kernel with this
lock already held.

For backward compatibility, `sys_clock_announce` remains
available and acquires the lock internally.  New and migrated drivers
should prefer the `sys_clock_lock` /
`sys_clock_announce_locked` pattern.

Note that a natural implementation of this API results in a "tickless"
kernel, which receives and processes timer interrupts only for
registered events, relying on programmable hardware counters to
provide irregular interrupts.  But a traditional, "ticked" or "dumb"
counter driver can be trivially implemented also:

* The driver can receive interrupts at a regular rate corresponding to
  the OS tick rate, calling `sys_clock_announce` with an argument of one
  each time.

* The driver can ignore calls to `sys_clock_set_timeout`, as every
  tick will be announced regardless of timeout status.

* The driver can return zero for every call to `sys_clock_elapsed`
  as no more than one tick can be detected as having elapsed (because
  otherwise an interrupt would have been received).
