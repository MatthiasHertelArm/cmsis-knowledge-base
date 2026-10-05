---
id: "intr-introduction-to-arm-semihosting"
type: "concept"
domain: "debug"
title: "Introduction to ARM Semihosting"
summary: "Firmware developers are generally accustomed to using logging for execution information. On microcontrollers, this is usually done through a serial interface attached to a terminal on the host."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-02-16-arm-semihosting.md"
doc_source: "https://interrupt.memfault.com/blog/arm-semihosting"
license: "CC-BY-SA-4.0"
mode: "V"
---

Firmware developers are generally accustomed to using logging for execution
information. On microcontrollers, this is usually done through a serial
interface attached to a terminal on the host.

But one might need more advanced features from the host! I was in this position
not long ago 🤨.

When working on camera firmware, and particularly on the image processing
algorithm, I constantly needed to transfer images from the camera to my host
machine to make sure everything was working fine. So I started using
semi-hosting! It has greatly facilitated not only my development but also the
debugging of my embedded software.

**Semihosting** is one of the many interesting features available on ARM Cortex
microcontrollers. It allows an embedded program to take advantage of the
capabilities of an attached computer when the debugger is running.


This post introduces semihosting and shows how to use it and integrate it into
your own embedded projects.
