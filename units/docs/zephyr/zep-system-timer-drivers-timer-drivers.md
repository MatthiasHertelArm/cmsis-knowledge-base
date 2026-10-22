---
id: "zep-system-timer-drivers-timer-drivers"
type: "concept"
domain: "rtos"
title: "System Timer Drivers: Timer Drivers"
summary: "Kernel timing at the tick level is driven by a timer driver with a comparatively simple API."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/system_timer_drivers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/system_timer_drivers.rst"
license: "Apache-2.0"
mode: "V"
---

Kernel timing at the tick level is driven by a timer driver with a
comparatively simple API.

* The driver is expected to be able to "announce" new ticks to the
  kernel via the `sys_clock_announce` call, which passes an integer
  number of ticks that have elapsed since the last announce call (or
  system boot).  These calls can occur at any time, but the driver is
  expected to attempt to ensure (to the extent practical given
  interrupt latency interactions) that they occur near tick boundaries
  (i.e. not "halfway through" a tick), and most importantly that they
  be correct over time and subject to minimal skew vs. other counters
  and real world time.

* The driver is expected to provide a `sys_clock_set_timeout` call
  to the kernel which indicates how many ticks may elapse before the
  kernel must receive an announce call to trigger registered timeouts.
  It is legal to announce new ticks before that moment (though they
  must be correct) but delay after that will cause events to be
  missed.  Note that the timeout value passed here is in a delta from
  current time, but that does not absolve the driver of the
  requirement to provide ticks at a steady rate over time.  Naive
  implementations of this function are subject to bugs where the
  fractional tick gets "reset" incorrectly and causes clock skew.

* The driver is expected to provide a `sys_clock_elapsed` call which
  provides a current indication of how many ticks have elapsed (as
  compared to a real world clock) since the last call to
  `sys_clock_announce`, which the kernel needs to test newly
  arriving timeouts for expiration.

* The driver may optionally provide a `sys_clock_no_timeout` call.
  The kernel invokes it in place of `sys_clock_set_timeout` when no
  timeout is pending, that is when the timeout queue is empty, and
  `CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE` is enabled.

  No tick announcement is forthcoming and the system does not care about precise
  uptime keeping, so the driver may do something to save resources.  Normal
  operation resumes at the next `sys_clock_set_timeout`; unlike
  `sys_clock_disable`, this is not a teardown.

  The timer *counter* must not be stopped.  `sys_clock_cycle_get_32`
  and `sys_clock_cycle_get_64` must keep counting up as if the call had
  never happened.


**Note:** The CPU keeps running with an empty timeout queue, for instance because the ready queue still holds threads, or because an interrupt fires.  Those threads and ISRs may call `k_cycle_get_32` or the timer interrupt is safe, gating the timer's clock most likely is not. Exactly what is safe is hardware specific.

  The hook is optional.  Without it, `sys_clock_set_timeout` is asked
  for the longest wait it can express, `UINT32_MAX` ticks.  That is
  numerically what `K_TICKS_FOREVER` was here, the long-standing "no deadline"
  signal, so a driver that has not been converted keeps working.

* The driver may optionally provide a `sys_clock_idle_enter` call,
  which the power-management path uses in place of
  `sys_clock_set_timeout` when the CPU is about to enter low-power
  idle.  It receives the number of ticks until the next expected wakeup, or
  `SYS_CLOCK_IDLE_FOREVER` when there is none and the uptime accounting may
  drift.

  A driver that hands off to a low-power wakeup timer, or otherwise
  reconfigures itself for sleep, does so here.  Told `SYS_CLOCK_IDLE_FOREVER`
  it may also stop its time base, which `sys_clock_no_timeout` does not
  allow, because the CPU is on its way out and `sys_clock_idle_exit` is
  guaranteed to run on the way back in.  Only the calling CPU goes idle, so a
  driver whose time base is shared between CPUs must ensure only the last CPU
  going idle stops the clock.

  The hook is optional.  Without it, `sys_clock_set_timeout` is called
  with its deprecated `idle` argument set to `true`, so a driver still
  keying its low-power handling on that argument keeps working.

The last three entry points divide the four states a system can be in:


* -
  - nothing pending
  - something pending
* - **running**
  - `sys_clock_no_timeout()`
  - `sys_clock_set_timeout(ticks)`
* - **idle**
  - `sys_clock_idle_enter(SYS_CLOCK_IDLE_FOREVER)`
  - `sys_clock_idle_enter(ticks)`
Without `CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE` the left column never
arises: the kernel keeps a synthetic deadline armed so the uptime stays exact,
and a driver only ever sees the right one.
