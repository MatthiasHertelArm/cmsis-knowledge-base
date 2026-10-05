---
id: "zep-kernel-timing-timeouts"
type: "concept"
domain: "rtos"
title: "Kernel Timing: Timeouts"
summary: "The Zephyr kernel provides many APIs with a \"timeout\" parameter. Conceptually, this indicates the time at which an event will occur. For example:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/clocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/clocks.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr kernel provides many APIs with a "timeout" parameter.
Conceptually, this indicates the time at which an event will occur.
For example:

* Kernel blocking operations like `k_sem_take` or
  `k_queue_get` may provide a timeout after which the
  routine will return with an error code if no data is available.

* Kernel `k_timer` objects must specify delays for
  their duration and period.

* The kernel `k_work_delayable` API provides a timeout parameter
  indicating when a work queue item will be added to the system queue.

All these values are specified using a `k_timeout_t` value.  This is
an opaque struct type that must be initialized using one of a family
of kernel timeout macros.  The most common, `K_MSEC`, defines
a time in milliseconds after the current time.

What is meant by "current time" for relative timeouts depends on the context:

* When scheduling a relative timeout from within a timeout callback (e.g. from
  within the expiry function passed to `k_timer_init` or the work handler
  passed to `k_work_init_delayable`), "current time" is the exact time at
  which the currently firing timeout was originally scheduled even if the "real
  time" will already have advanced. This is to ensure that timers scheduled from
  within another timer's callback will always be calculated with a precise offset
  to the firing timer. It is thereby possible to fire at regular intervals without
  introducing systematic clock drift over time.

* When scheduling a timeout from application context, "current time" means the
  value returned by `k_uptime_ticks` at the time at which the kernel
  receives the timeout value.

Other options for timeout initialization follow the unit conventions
described above: `K_NSEC()`, `K_USEC`, `K_TICKS` and
`K_CYC()` specify timeout values that will expire after specified
numbers of nanoseconds, microseconds, ticks and cycles, respectively.

Precision of `k_timeout_t` values is configurable, with the default
being 32 bits.  Large uptime counts in non-tick units will experience
complicated rollover semantics, so it is expected that
timing-sensitive applications with long uptimes will be configured to
use a 64 bit timeout type.

Finally, it is possible to specify timeouts as absolute times since
system boot.  A timeout initialized with `K_TIMEOUT_ABS_MS`
indicates a timeout that will expire after the system uptime reaches
the specified value.  There are likewise nanosecond, microsecond,
cycles and ticks variants of this API.
