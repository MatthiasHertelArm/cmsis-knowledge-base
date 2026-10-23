---
id: "zep-system-timer-drivers-generic-tickless-core"
type: "concept"
domain: "rtos"
title: "System Timer Drivers: Generic Tickless Core"
summary: "The work described above, the cycle-to-tick conversion, the announce baseline, the tick-aligned deadline computation and the counter wrap and range handling, is nearly the same in every tickless driver, and the hand-rolled variations are a recurring source of timer bugs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/system_timer_drivers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/system_timer_drivers.rst"
license: "Apache-2.0"
mode: "V"
---

The work described above, the cycle-to-tick conversion, the announce baseline,
the tick-aligned deadline computation and the counter wrap and range handling,
is nearly the same in every tickless driver, and the hand-rolled variations are
a recurring source of timer bugs.
`drivers/timer/system_timer_generic.h` carries that logic once.

It is an implementation header, not a declaration header: including it
*defines* `sys_clock_set_timeout`, `sys_clock_elapsed` and
`sys_clock_cycle_get_32` / `sys_clock_cycle_get_64`.  Any number
of drivers can be built on it; each includes it once, after providing the macros
and primitives below.  A build compiles a single system timer driver, so those
definitions land once.  The driver then works in cycles only; the core owns the
tick domain.

The core emits both cycle getters, the 64-bit one whatever the counter's width:
the announce baseline is 64-bit, and the linker drops the getter where nothing
calls it.

Whether a driver also selects
`CONFIG_TIMER_HAS_64BIT_CYCLE_COUNTER` stays its own call.  That
option says a 64-bit read is cheap, or at least no dearer than a 32-bit one, so
nothing is gained by preferring the narrower getter.  With
`TIMER_CORE_COUNTER_NONATOMIC` both go through the clock lock and that holds;
with an atomic counter narrower than 64 bits only the 64-bit getter takes the
lock, and the 32-bit one stays a lock-free read.

Two primitives are required: `timer_driver_cycle_get()`, which reads the
hardware cycle counter, and one arming function, `timer_driver_set_compare()`
or `timer_driver_set_reload()` depending on the backend.  The driver's ISR
acknowledges the hardware then calls `timer_core_announce()`, its init
connects the IRQ then calls `timer_core_init()`, and on SMP its
`smp_timer_init()` calls `timer_core_smp_prime()`.


### Backend selection


Exactly one of these states what the hardware is:

`TIMER_CORE_BACKEND_COMPARE_ORDERED`
   Absolute comparator, ordered match: the interrupt fires once the counter has
   reached or passed the programmed value, so a deadline already in the past
   fires at once.  The usable range is half the counter width.

`TIMER_CORE_BACKEND_COMPARE_EXACT`
   Absolute comparator, equality match: a value written after the counter has
   passed it is missed for a whole counter period.  The core writes the
   comparator through a verify loop, so the driver needs no minimum-delay floor
   of its own.

`TIMER_CORE_BACKEND_RELOAD`
   Relative delay: down-counters and compare-match-reset periodics.  Assumed to
   auto-reload, so a ticked kernel free-runs from the value set at init.


### Optional macros


Each is defined only when the default, given below, does not fit:

`TIMER_CORE_CYCLES_PER_SEC`
   Counter rate, in Hz.  Defaults to the kernel system clock rate.  Set it when
   the counter is prescaled or runs at a fixed rate of its own.  The core derives
   `TIMER_CORE_CYC_PER_TICK` from it, which a driver may read for its own
   hardware setup, typically the one-tick period it programs at init, but never
   defines itself.

`TIMER_CORE_CYCLES_PER_SEC_RUNTIME`
   The rate above is a variable, not a build-time constant, because it is read
   from the clock controller or computed at init.  The core then precomputes the
   cycles per tick once instead of relying on the division folding.  The variable
   must hold its final value before `timer_core_init()` is called.

`TIMER_CORE_COUNTER_WIDTH`
   Width, in bits, up to 64, of the count `timer_driver_cycle_get()` returns.
   Defaults to the native register width.  A counter of another width states its
   own, and must: a genuine 64-bit counter on a 32-bit CPU would otherwise inherit
   a 32-bit mask and lose any span past 2^32 cycles.  The core masks every delta to
   this width, so a narrow counter is read raw and the driver never has to widen
   the count in software.

`TIMER_CORE_COUNTER_NONMONOTONIC`
   The counter may momentarily read behind a value already observed, as a global
   timer does under QEMU SMP.  The core treats a backwards read as no elapse
   rather than a huge jump.

`TIMER_CORE_COUNTER_NONATOMIC`
   `timer_driver_cycle_get()` is not a single atomic read but a value
   synthesized from state the ISR also touches.  The core then reads it under
   the clock lock.

`TIMER_CORE_HAVE_CYCLE_GET_32`, `TIMER_CORE_HAVE_CYCLE_GET_64`
   The driver defines that entry point itself and the core does not.  For a
   counter that needs scaling.  `timer_core_cycle_get()`, available after the
   include, gives the full-width count in the counter's own domain to scale
   from.

   The 32-bit one is required of a driver that sets
   `TIMER_CORE_CYCLES_PER_SEC`, a counter running at a rate of its own being
   one the kernel cannot read raw.  The core then emits no 64-bit getter
   either, that being in the domain the driver just declared foreign.  Supply
   one as well to have it.

`TIMER_CORE_ALARM_MAX_CYCLES`
   Largest value the arming primitive can express, nothing more.  Defaults to the
   whole span of `TIMER_CORE_COUNTER_WIDTH`, the alarm and the counter usually
   being one piece of hardware.  Set it where the arming range is decided by
   something else: a compare or reload register narrower than the counter, or a
   separate device.

   It states hardware capacity, so it carries no safety margin.  The core derives
   its own from `TIMER_CORE_COUNTER_WIDTH`: it arms no further ahead of the last
   announce than half the counter's span, a quarter with
   `TIMER_CORE_COUNTER_NONMONOTONIC`, so a late announce still yields a delta the
   masking can resolve.  Whichever of the two binds first wins.

`TIMER_CORE_ALARM_MIN_CYCLES`
   Reload floor, in cycles, `TIMER_CORE_BACKEND_RELOAD` only.  Defaults to 1.

`TIMER_CORE_ALARM_LEAD_CYCLES`
   Cycles a compare must be ahead of the counter for the match to be caught,
   `TIMER_CORE_BACKEND_COMPARE_EXACT` only.  Defaults to 1, a comparator
   written while the counter is still below it firing.  Raise it for hardware
   that has to carry the write into the counter's clock domain first and misses
   a match programmed closer than that.

New tickless drivers should build on this header rather than reimplement the
tick accounting.  The header documents each macro and primitive in full.
