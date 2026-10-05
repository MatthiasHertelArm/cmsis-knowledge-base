---
id: "intr-a-guide-to-watchdog-timers-for-emb-the-hardware-watchdog"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: The Hardware Watchdog"
summary: "Most chip vendors include an isolated RTL block known as a \"Watchdog Timer\" in a MCU. This peripheral is comprised of a counter which decrements automatically by the hardware each clock cycle."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#the-hardware-watchdog"
license: "CC-BY-SA-4.0"
mode: "V"
---

Most chip vendors include an isolated RTL block known as a "Watchdog Timer" in a MCU. This peripheral is comprised of a counter which decrements automatically by the hardware each clock cycle. When the count reaches zero, the hardware will automatically reset the device.

The peripheral is typically disabled by default and it's the programmers responsibility to configure and enable it in software. Once enabled, the system software needs to reset the counter periodically to prevent the device from rebooting. This operation is usually referred to as "feeding", "kicking", or "patting" the dog. The rationale here is if software is unable to reset the watchdog counter, the system is not running as expected and needs to be reset to get back to a sane state.

> NOTE: It also worth mentioning that for some systems where catching system hangs is mission
> critical, there are even dedicated ICs which can be used[^3]. For these chips, the watchdog is
> usually "fed" by toggling a GPIO line from the MCU being monitored.
