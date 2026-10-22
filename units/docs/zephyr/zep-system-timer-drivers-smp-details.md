---
id: "zep-system-timer-drivers-smp-details"
type: "concept"
domain: "rtos"
title: "System Timer Drivers: SMP Details"
summary: "In general, the timer API described above does not change when run in a multiprocessor context. The kernel will internally synchronize all access appropriately, and ensure that all critical sections are small and minimal."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/system_timer_drivers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/system_timer_drivers.rst"
license: "Apache-2.0"
mode: "V"
---

In general, the timer API described above does not change when run in
a multiprocessor context.  The kernel will internally synchronize all
access appropriately, and ensure that all critical sections are small
and minimal.  But some notes are important to detail:

* Zephyr is agnostic about which CPU services timer interrupts.  It is
  not illegal (though probably undesirable in some circumstances) to
  have every timer interrupt handled on a single processor.  Existing
  SMP architectures implement symmetric timer drivers.

* The `sys_clock_announce` call is expected to be globally
  synchronized at the driver level.  The kernel does not do any
  per-CPU tracking, and expects that if two timer interrupts fire near
  simultaneously, that only one will provide the current tick count to
  the timing subsystem.  The other may legally provide a tick count of
  zero if no ticks have elapsed.  It should not "skip" the announce
  call because of timeslicing requirements (see the time slicing notes in
  kernel_timing).

* Some SMP hardware uses a single, global timer device, others use a
  per-CPU counter.  The complexity here (for example: ensuring counter
  synchronization between CPUs) is expected to be managed by the
  driver, not the kernel.

* The next timeout value passed back to the driver via
  `sys_clock_set_timeout` is done identically for every CPU.
  So by default, every CPU will see simultaneous timer interrupts for
  every event, even though by definition only one of them should see a
  non-zero ticks argument to `sys_clock_announce`.  This is probably
  a correct default for timing sensitive applications (because it
  minimizes the chance that an errant ISR or interrupt lock will delay
  a timeout), but may be a performance problem in some cases.  The
  current design expects that any such optimization is the
  responsibility of the timer driver.
