---
id: "intr-defensive-programming-friend-or-fo-offensive-programming"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?: Offensive Programming"
summary: "Offensive programming, although seemingly opposite in word choice, actually expands upon defensive programming and takes it one step further. Instead of just accepting that malloc() can fail, software with offensive programming in mind might assert that malloc() never fails."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming#offensive-programming"
license: "CC-BY-SA-4.0"
mode: "V"
---

Offensive programming, although seemingly opposite in word choice, actually
expands upon defensive programming and takes it one step further. Instead of
just accepting that `malloc()` can fail, software with offensive programming in
mind might assert that `malloc()` _never_ fails. If a `malloc()` call does fail,
the software fatally assert, print enough information for the developer to root
cause the issue or capture a core dump, and then reset it back to a known
working state.

In embedded systems, where the entire stack from hardware to software is often
built and controlled by a single organization, any bug is the responsibility of
the engineers in that organization to root cause and fix. Offensive programming
can be a useful approach to surface bugs that might otherwise take weeks to
reproduce or never be found.

Offensive programming can take many forms inside of software, but the most
common way is to use
[assertions](https://interrupt.memfault.com/blog/asserts-in-embedded-systems) liberally
and creatively against developer errors and system state behavior.

Let's run through a few hypothetical situations and how you could use offensive
programming. If your embedded system is experiencing:

- **Performance issues** - such as the GUI freezing or slow response times to
  button presses, you can use
  [watchdogs](https://interrupt.memfault.com/blog/firmware-watchdog-best-practices) or
  timers and assertions to crash the system when the system stalls so that a
  developer can figure out what exactly was consuming CPU time.
- **Memory issues** - such as high stack usage, no free heap memory, or
  excessive fragmentation, trigger a crash of the system when these states are
  detected and capture the relevant parts for analysis by a developer to figure
  out where the system went sideways. It's rarely the final call to `malloc()`
  or the highest function in the stack that pushes the system over the edge, but
  everything that led up to it.
- **Locking issues** - set a low-ish timeout (5 seconds) on RTOS functions, such
  a `mutex_lock` and `queue_put`. Setting a low timeout will cause the system to
  crash if the operation did not succeed in the allotted time, again allowing a
  developer to further inspect what was the root issue. You can also choose to
  spin indefinitely and have the watchdog [clean
  up](https://interrupt.memfault.com/blog/firmware-watchdog-best-practices).

This is just scratching the surface of offensive programming techniques, but I
hope you now have an idea of what this article is all about!

### Benefits of Offensive Programming

You might be asking why you should instrument your code and firmware with a
bunch of asserts, timers, watchdogs, and coordinated faults, and that's a
reasonable question. Software crashes on an embedded system don't just take down
a thread, but often the entire system as well.

There are two sides to this double-edged sword.

On one hand, when the device experiences unforeseen issues, you can leave the
system running in an undefined and unpredictable state. Maybe the heap is out of
memory, or the system failed to put a critical event in a queue and we've
dropped data, or maybe a thread has deadlocked and there is no automated
recovery mechanism. Some devices don't even have power buttons and need to be
manually unplugged or the batteries pulled out!

On the other hand, devices in an unintended state are essentially broken devices
and should be reset. If the device was out of heap, it likely isn't going to
recover and there exists a leak. If a thread has deadlocked, it also isn't going
to recover. Not to mention, running in an undefined state leaves firmware open
to security holes and is exactly what we want to avoid.

On top of preventing your firmware from running in an unpredictable state,
triggering asserts and faults at the exact moment of the bug helps developers
track down these issues! If your devices are connected to a debugger while an
assert or fault is hit, or you have core dump instrumentation, you can reap the
following benefits:

- **Quicker bug fixes** - If the system is halted or a core dump is captured
  when an assert is hit, the developer can get access to backtraces, registers,
  function arguments, and system state such as the heap, lists, and queues. With
  all this information, developers can root cause issues more quickly.
- **Faster development** - Writing a new piece of code that integrates into
  multiple modules can be tricky if there are bugs or assumptions in the modules
  you are integrating with. By having assertions and OffP practices in the
  surrounding layers, if a developer does anything misaligned with the API
  specs, the system will immediately alert the developer. It's better than
  tracking down what `-3` or `unknown_error` means and how it bubbled up through
  the system.
- **Awareness of prevalence** - Developers don't notice bugs unless they are
  obvious or dropped in their inbox as a bug report. By forcing the software to
  reset, awareness of these unknown bugs is increased and developers can more
  easily understand how often they are occurring.
- **Returning system to sane state** - If your comms thread is deadlocked, no
  data will be sent from your device to the outside world, making your device a
  brick until a user manually resets it. By resetting the device, you are more
  likely to put the device back into a functioning state. Most embedded devices
  have very quick reboot times, so it isn't a huge deal.
