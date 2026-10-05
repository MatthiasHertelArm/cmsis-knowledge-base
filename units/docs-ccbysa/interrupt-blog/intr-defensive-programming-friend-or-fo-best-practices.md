---
id: "intr-defensive-programming-friend-or-fo-best-practices"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?: Best Practices"
summary: "Simple and sweet. Don't assert anything on code that is run during a boot-up sequence that isn't guaranteed, because this is how reboot loops can occur when something goes wrong."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming#best-practices"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Don't Assert on Boot Sequences

Simple and sweet. Don't assert anything on code that is run during a boot-up
sequence that isn't guaranteed, because this is how reboot loops can occur when
something goes wrong. The only time I would assert on a boot sequence is when my
device is connected to a debugger, or when things are absolutely required and
there is zero chance of shipping a broken firmware to end-users.

When in doubt, log these errors instead.

### Playing Offense Internally

There is no better time to enable asserts, watchdogs, and other OffP practices
than when a development board is connected to a debugger! With this in place,
developers can instantly and easily get backtraces and system state, as well as
trace through the execution of the undefined behavior to find out what happened
as well as potentially discover what _would_ happen if the bug is not fixed.

### Playing Offense in Production Builds

Before we dig into what aspects of OffP make sense on production builds, we need
to establish that software crashes should be recorded in some way so that a
developer can retrieve them at a later date. This can be some form of logging,
tracing, or core dumps, or any combination of these. If we don't have a way to
record issues, we'll never know what truly causes these issues and how often
they occur.

The parts of OffP that should be kept compiled in and enabled in production
builds are the ones that ensure that undefined behavior is not experienced in
firmware. This includes argument validation, watchdog timeouts to detect
deadlocks, bugs potentially leading to memory corruption, etc. It's better to
return the device to a known state than to limp along.

What we can often consider disabling completely are marginal issues, such as
software stalls, malloc and queue failures (which are handled), and timeouts.
These types of issues aren't guaranteed to recover or go away, but they may be
acceptable depending on the context and how the device is used.

If you choose to reduce the aggressiveness of the checks, consider keeping the
hooks and timeouts and instead log them somewhere, rather than reset the system.
For inspiration, check out
[ARM MBed's Error Handling API](https://os.mbed.com/docs/mbed-os/v6.5/apis/error-handling.html),
which keeps a circular buffer of warnings that the system has experienced in a
region of RAM that is kept between reboots. The idea is that all layers of the
firmware use a single error API and then developers can do what they want with
them. If you have logging infrastructure in place, you can log them out on boot,
or if your system is set up with core dumps, you can capture this memory region
too.

For instance, we can modify our `ASSERT()` macro to instead log through the
logging system instead of triggering a reset when a production build is
compiled.

```c
#if PRODUCTION_BUILD
  #define MY_ASSERT(expr, msg)    \
    do {                          \
      if (!(expr)) {              \
        /* log error to buffer */ \
      }                           \
    } while (0)
#else
  #define MY_ASSERT(expr, msg)    \
    do {                          \
      if (!(expr)) {              \
        /* core dump */           \
      }                           \
    } while (0)
#endif
```
