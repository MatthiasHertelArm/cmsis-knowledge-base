---
id: "zep-kernel-timing-time-units"
type: "concept"
domain: "rtos"
title: "Kernel Timing: Time Units"
summary: "Kernel time is tracked in several units which are used for different purposes."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/clocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/clocks.rst"
license: "Apache-2.0"
mode: "V"
---

Kernel time is tracked in several units which are used for different
purposes.

Real time values, typically specified in milliseconds or microseconds,
are the default presentation of time to application code.  They have
the advantages of being universally portable and pervasively
understood, though they may not match the precision of the underlying
hardware perfectly.

The kernel presents a "cycle" count via the `k_cycle_get_32`
and `k_cycle_get_64` APIs.  The intent is that this counter
represents the fastest cycle counter that the operating system is able
to present to the user (for example, a CPU cycle counter) and that the
read operation is very fast.  The expectation is that very sensitive
application code might use this in a polling manner to achieve maximal
precision.  The frequency of this counter is available from
`sys_clock_hw_cycles_per_sec`. On most platforms this is a runtime
constant that evaluates to `CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`
and is fixed for the lifetime of the system. On platforms where the system
timer frequency is not fixed, `sys_clock_hw_cycles_per_sec` returns a
runtime value and application code must not assume a single immutable
frequency.


### Runtime System Timer Frequency


Some platforms need the system timer frequency to be available at runtime,
either because the timer driver discovers the clock rate from hardware or
because the timer clock rate can change after boot.

Platforms that can change the active system timer frequency at runtime must
enable `CONFIG_SYSTEM_CLOCK_HW_CYCLES_PER_SEC_RUNTIME_UPDATE` and:

* Call `z_sys_clock_hw_cycles_per_sec_update` after applying the clock change.
* If the system timer driver caches derived constants (e.g. cycles-per-tick) or
  needs to reprogram hardware when the clock changes, provide a timer-driver
  override of `z_sys_clock_hw_cycles_per_sec_update`.

The default implementation of `z_sys_clock_hw_cycles_per_sec_update` only updates
the stored frequency value.


**Note:** the system timer frequency as a single **global** value. It is not compatible with per-CPU frequency scaling configurations where different CPUs could observe different system timer frequencies. When enabled, `sys_clock_hw_cycles_per_sec` and time unit conversions follow the current runtime value.

For asynchronous timekeeping, the kernel defines a "ticks" concept.  A
"tick" is the internal count in which the kernel does all its internal
uptime and timeout bookkeeping.  Interrupts are expected to be
delivered on tick boundaries to the extent practical, and no
fractional ticks are tracked.  The choice of tick rate is configurable
via `CONFIG_SYS_CLOCK_TICKS_PER_SEC`.  Defaults on most
hardware platforms (ones that support setting arbitrary interrupt
timeouts) are expected to be in the range of 10 kHz, with software
emulation platforms and legacy drivers using a more traditional 100 Hz
value.


### Conversion


Zephyr provides an extensively enumerated conversion library with
rounding control for all time units.  Any unit of "ms" (milliseconds),
"us" (microseconds), "tick", or "cyc" can be converted to any other.
Control of rounding is provided, and each conversion is available in
"floor" (round down to nearest output unit), "ceil" (round up) and
"near" (round to nearest).  Finally the output precision can be
specified as either 32 or 64 bits.

For example: `k_ms_to_ticks_ceil32` will convert a
millisecond input value to the next higher number of ticks, returning
a result truncated to 32 bits of precision; and
`k_cyc_to_us_floor64` will convert a measured cycle count
to an elapsed number of microseconds in a full 64 bits of precision.
See the reference documentation for the full enumeration of conversion
routines.

On most platforms, where the various counter rates are integral
multiples of each other and where the output fits within a single
word, these conversions expand to a 2-4 operation sequence, requiring
full precision only where actually required and requested.
