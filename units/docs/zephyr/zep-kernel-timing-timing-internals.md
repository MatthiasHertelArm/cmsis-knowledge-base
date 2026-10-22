---
id: "zep-kernel-timing-timing-internals"
type: "concept"
domain: "rtos"
title: "Kernel Timing: Timing Internals"
summary: "All Zephyr k_timeout_t events specified using the API above are managed in a single, global queue of events."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/timing/clocks.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/timing/clocks.rst"
license: "Apache-2.0"
mode: "V"
---

### Timeout Queue


All Zephyr `k_timeout_t` events specified using the API above are
managed in a single, global queue of events.  The action to take on an
event is specified as a callback function pointer provided by the
subsystem requesting the event, along with a `_timeout`
tracking struct that is expected to be embedded within subsystem-defined
data structures (for example: a `wait_q` struct, or a
`k_tid_t` thread struct).

Note that all variant units passed via a `k_timeout_t` are
converted to ticks once on insertion into the queue.  There are no
multiple-conversion steps internal to the kernel, so precision is
guaranteed at the tick level no matter how many events exist or how long
a timeout might be.

The data structure that holds the queue is selected at build time
through the `CONFIG_TIMEOUT_BACKEND` choice.  Only the
front end is shared between backends (the announce path, the SMP
re-entry handling, and the relative versus absolute timeout rules); each
backend supplies the queue itself, so an integrator can match the data
structure to the workload without touching the common code.

The default, `CONFIG_TIMEOUT_BACKEND_DLIST`, stores
events in a doubly linked list sorted by expiry, each holding a delta
count in ticks from its predecessor.  Insertion is O(N) in the number of
pending timeouts: inexpensive for the handful a typical system has
pending, but it scales poorly when many are outstanding.  The four
alternative backends, all currently experimental, trade extra memory or
behaviour for faster insertion at scale:

* `CONFIG_TIMEOUT_BACKEND_MINHEAP` keeps the events in a
  binary min-heap keyed on absolute expiry, making insertion and removal
  O(log N).  It requires 64-bit ticks
  (`CONFIG_TIMEOUT_64BIT`) and a fixed-capacity heap
  (`CONFIG_TIMEOUT_HEAP_MAX_ENTRIES`, whose overflow is
  fatal), and it does not preserve the firing order of timeouts that
  expire on the same tick.

* `CONFIG_TIMEOUT_BACKEND_WHEEL` is a hierarchical timer
  wheel with O(1) insertion and removal for the near future and a sorted
  overflow list beyond.  It has the largest per-event and static
  footprint, does not preserve same-tick firing order, and wakes a
  tickless-idle CPU periodically because its next-timeout estimate is
  bounded by the wheel period (a power cost the other backends avoid).

* `CONFIG_TIMEOUT_BACKEND_BUCKET` is a single-level
  bucketed delta list, a simpler relative of the wheel.  It gives O(1)
  insertion within a tunable near-future window
  (`CONFIG_TIMEOUT_BUCKET_LISTS`) and falls back to a
  sorted overflow list beyond it.  It also requires 64-bit ticks, but
  unlike the wheel it preserves same-tick firing order and adds no
  idle-wakeup cost.

* `CONFIG_TIMEOUT_BACKEND_SKIPLIST` is a Pugh skip list
  keyed on absolute expiry.  Expected insertion and removal are O(log N)
  with no capacity limit, and same-tick firing order is FIFO.  It
  requires 64-bit ticks.  Each event stores
  `CONFIG_TIMEOUT_SKIPLIST_MAX_LEVEL` forward pointers,
  so per-event RAM is higher than the delta list or min-heap.

The non-default backends target systems that hold many concurrent
timeouts, especially ones clustered in the near future.  For most
applications the delta list remains the appropriate default.


### Timer Drivers


Kernel timing at the tick level is driven by a timer driver.  That interface
and the locking it runs under are described in system_timer_drivers.


### Time Slicing


An auxiliary job of the timing subsystem is to provide tick counters
to the scheduler that allow implementation of time slicing of threads.
A thread time-slice cannot be a timeout value, as it does not reflect
a global expiration but instead a per-CPU value that needs to be
tracked independently on each CPU in an SMP context.

Because there may be no other hardware available to drive timeslicing,
Zephyr multiplexes the existing timer driver.  This means that the
value passed to `sys_clock_set_timeout` may be clamped to a
smaller value than the current next timeout when a time sliced thread
is currently scheduled.


### Subsystems that keep millisecond APIs


In general, code like this will port just like applications code will.
Millisecond values from the user may be treated any way the subsystem
likes, and then converted into kernel timeouts using
`K_MSEC()` at the point where they are presented to the
kernel.

Obviously this comes at the cost of not being able to use new
features, like the higher precision timeout constructors or absolute
timeouts.  But for many subsystems with simple needs, this may be
acceptable.

One complexity is `K_FOREVER`.  Subsystems that might have
been able to accept this value to their millisecond API in the past no
longer can, because it is no longer an integral type.  Such code
will need to use a different, integer-valued token to represent
"forever".  `K_NO_WAIT` has the same typesafety concern too,
of course, but as it is (and has always been) simply a numerical zero,
it has a natural porting path.


### Subsystems using `k_timeout_t`


Ideally, code that takes a "timeout" parameter specifying a time to
wait should be using the kernel native abstraction where possible.
But `k_timeout_t` is opaque, and needs to be converted before
it can be inspected by an application.

Some conversions are simple.  Code that needs to test for
`K_FOREVER` can simply use the `K_TIMEOUT_EQ()`
macro to test the opaque struct for equality and take special action.

The more complicated case is when the subsystem needs to take a
timeout and loop, waiting for it to finish while doing some processing
that may require multiple blocking operations on underlying kernel
code.  For example, consider this design:

```c

void my_wait_for_event(struct my_subsys *obj, int32_t timeout_in_ms)
{
    while (true) {
        uint32_t start = k_uptime_get_32();

        if (is_event_complete(obj)) {
            return;
        }

        /* Wait for notification of state change */
        k_sem_take(obj->sem, timeout_in_ms);

        /* Subtract elapsed time */
        timeout_in_ms -= (k_uptime_get_32() - start);
    }
}
```
This code requires that the timeout value be inspected, which is no
longer possible.  For situations like this, the new API provides the
internal `sys_timepoint_calc` and `sys_timepoint_timeout` routines
that converts an arbitrary timeout to and from a timepoint value based on
an uptime tick at which it will expire.  So such a loop might look like:


```c

void my_wait_for_event(struct my_subsys *obj, k_timeout_t timeout)
{
    /* Compute the end time from the timeout */
    k_timepoint_t end = sys_timepoint_calc(timeout);

    do {
        if (is_event_complete(obj)) {
            return;
        }

        /* Update timeout with remaining time */
        timeout = sys_timepoint_timeout(end);

        /* Wait for notification of state change */
        k_sem_take(obj->sem, timeout);
    } while (!K_TIMEOUT_EQ(timeout, K_NO_WAIT));
}
```
Note that `sys_timepoint_calc` accepts special values `K_FOREVER`
and `K_NO_WAIT`, and works identically for absolute timeouts as well
as conventional ones. Conversely, `sys_timepoint_timeout` may return
`K_FOREVER` or `K_NO_WAIT` if those were used to create
the timepoint, the later also being returned if the timepoint is now in the
past. For simple cases, `sys_timepoint_expired` can be used as well.

But some care is still required for subsystems that use those.  Note that
delta timeouts need to be interpreted relative to a "current time",
and obviously that time is the time of the call to
`sys_timepoint_calc`.  But the user expects that the time is
the time they passed the timeout to you.  Care must be taken to call
this function just once, as synchronously as possible to the timeout
creation in user code.  It should not be used on a "stored" timeout
value, and should never be called iteratively in a loop.



#### API Reference
