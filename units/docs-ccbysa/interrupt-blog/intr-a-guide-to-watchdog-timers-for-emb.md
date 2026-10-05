---
id: "intr-a-guide-to-watchdog-timers-for-emb"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems"
summary: "At some point you've probably had to unplug and plug back in an electronic device to get it to work again!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices"
license: "CC-BY-SA-4.0"
mode: "V"
---

At some point you've probably had to unplug and plug back in an electronic device to get it to work again!
System freezes and hangs are not only frustrating to an end user, but they can also be quite challenging to debug and fix.

For some classes of devices, such as a satellite[^1], a manual reset is not even possible, making a
wedged device a multi-million dollar "brick". As firmware engineers, we must make sure our systems
can always recover from a stuck task, or an infinite loop. This is best accomplished with a watchdog.



In this article we will discuss the last line of defense in embedded systems -- watchdogs. We will walk through a step-by-step example of how to implement a watchdog subsystem, incorporating a "hardware" and "software" watchdog, and examine effective strategies for root causing the underlying problems leading to these hangs.
