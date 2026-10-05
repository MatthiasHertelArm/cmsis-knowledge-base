---
id: "zep-timers-concepts"
type: "concept"
domain: "rtos"
title: "Timers: Concepts"
summary: "Any number of timers can be defined (limited only by available RAM). Each timer is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/timers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/timers.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of timers can be defined (limited only by available RAM). Each timer
is referenced by its memory address.

A timer has the following key properties:

* A **duration** specifying the time interval before the timer
  expires for the first time.  This is a `k_timeout_t` value that
  may be initialized via different units.

* A **period** specifying the time interval between all timer
  expirations after the first one, also a `k_timeout_t`. It must be
  non-negative.  A period of `K_NO_WAIT` (i.e. zero) or
  `K_FOREVER` means that the timer is a one-shot timer that stops
  after a single expiration. (For example then, if a timer is started
  with a duration of 200 and a period of 75, it will first expire
  after 200 ms and then every 75 ms after that.)

* An **expiry function** that is executed each time the timer expires.
  The function is executed by the system clock interrupt handler.
  If no expiry function is required a `NULL` function can be specified.

* A **stop function** that is executed if the timer is stopped prematurely
  while running. The function is executed by the thread that stops the timer.
  If no stop function is required a `NULL` function can be specified.

* A **status** value that indicates how many times the timer has expired
  since the status value was last read.

A timer must be initialized before it can be used. This specifies its
expiry function and stop function values, sets the timer's status to zero,
and puts the timer into the **stopped** state.

A timer is **started** by specifying a duration and a period.
The timer's status is reset to zero, and then the timer enters
the **running** state and begins counting down towards expiry.


**Note:** The timer's duration is a **minimum** delay relative to the time the timer was started. The timer's period is a **minimum** delay relative to the last time the timer "should" have expired. This means that a periodic timer will not drift relative to the system timer, and that its periodic delay can be shorter or longer than the specified period. To ensure a minimum delay until the timer expires, restart the timer from within the **expiry function** or after the timer expired. The variability of the delays stem from system variables like interrupt handling delays and execution time of preceding timer handlers.

When a running timer expires its status is incremented
and the timer executes its expiry function, if one exists;
If a thread is waiting on the timer, it is unblocked.
If the timer's period is zero the timer enters the stopped state;
otherwise, the timer restarts with a new duration equal to the delta between
the time the timer "should" have expired and its period.

A running timer can be stopped in mid-countdown, if desired.
The timer's status is left unchanged, then the timer enters the stopped state
and executes its stop function, if one exists.
If a thread is waiting on the timer, it is unblocked.
Attempting to stop a non-running timer is permitted,
but has no effect on the timer since it is already stopped.

A running timer can be restarted in mid-countdown, if desired.
The timer's status is reset to zero, then the timer begins counting down
using the new duration and period values specified by the caller.
If a thread is waiting on the timer, it continues waiting.

A timer's status can be read directly at any time to determine how many times
the timer has expired since its status was last read.
Reading a timer's status resets its value to zero.
The amount of time remaining before the timer expires can also be read;
a value of zero indicates that the timer is stopped.

A thread may read a timer's status indirectly by **synchronizing**
with the timer. This blocks the thread until the timer's status is non-zero
(indicating that it has expired at least once) or the timer is stopped;
if the timer status is already non-zero or the timer is already stopped
the thread continues without waiting. The synchronization operation
returns the timer's status and resets it to zero.


**Note:** Only a single user should examine the status of any given timer, since reading the status (directly or indirectly) changes its value. Similarly, only a single thread at a time should synchronize with a given timer. ISRs are not permitted to synchronize with timers, since ISRs are not allowed to block.
