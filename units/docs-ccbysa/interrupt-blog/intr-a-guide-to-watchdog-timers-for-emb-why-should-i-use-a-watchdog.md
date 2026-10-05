---
id: "intr-a-guide-to-watchdog-timers-for-emb-why-should-i-use-a-watchdog"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Why should I use a Watchdog?"
summary: "There are numerous ways an embedded device can hang. Some of the most common I've run into over the years include:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#why-should-i-use-a-watchdog"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are numerous ways an embedded device can hang. Some of the most common I've run into over the
years include:

- Memory gets corrupted and code winds up in an infinite loop
- A hardware component (such as a HRM, Accelerometer, or NOR Flash Chip) is wedged and not
  responding to requests.
- One or more tasks become deadlocked because mutexes were grabbed in the wrong order or weren't released.
- A higher priority RTOS task (e.g. a UI task) is using so many CPU cycles that lower priority tasks (like a WiFi task) never get to run preventing sensor data from being published to your cloud service.

Whether you are still in the development phase of a project or have millions of devices in the field,
the embedded system _should_ have a watchdog subsystem in place. It is the best way to
identify system hangs and collect enough information to be able to root cause the underlying issue and deliver a fix.
