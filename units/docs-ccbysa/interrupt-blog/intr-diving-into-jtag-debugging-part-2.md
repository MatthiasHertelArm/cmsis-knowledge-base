---
id: "intr-diving-into-jtag-debugging-part-2"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2)"
summary: "As noted in my previous article Diving into JTAG protocol. Part 1 — Overview, JTAG was initially developed for testing integrated circuits and printed circuit boards."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2"
license: "CC-BY-SA-4.0"
mode: "V"
---

As noted in my previous article [Diving into JTAG protocol. Part 1 — Overview](https://interrupt.memfault.com/blog/diving-into-jtag-part1), JTAG was initially developed for testing integrated circuits and printed circuit boards. However, its potential for debugging was realized over time, and now JTAG has become the standard protocol for microcontroller debugging. Many Firmware and Embedded engineers first encountered it in this particular context.



In this second part of a JTAG deep-dive series, we take an in-depth look at interacting with a microcontroller's memory and engaging with the processor core and debug registers. While the use of JTAG in testing is fairly standardized when it comes to debugging, each processor architecture has its unique nuances. With that in mind, this article will focus on debugging using JTAG on the ARM Cortex-M architecture, specifically with the STM32F407VG microcontroller.



For successful debugging, it’s not enough to simply know the basics of JTAG. It’s also essential to understand the workings of the ARM Debug Access Port, a key component that allows access to the controller’s internal registers and memory. I’ve detailed this module in the article [A Deep Dive into the ARM Debug Access Port](https://piolabs.com/blog/engineering/diving-into-arm-debug-access-port.html). With that groundwork laid, let’s dive into the world of debugging through JTAG.
