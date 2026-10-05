---
id: "intr-device-firmware-update-cookbook"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook"
summary: "Implementing OTA (Over The Air) firmware updates is a rite of passage for firmware engineers. Device firmware update is a key component of most hardware projects. Often, it is also one of the more complicated components."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook"
license: "CC-BY-SA-4.0"
mode: "V"
---

Implementing OTA (Over The Air) firmware updates is a rite of passage for
firmware engineers. Device firmware update is a key component of most hardware
projects. Often, it is also one of the more complicated components.

I have worked on multiple firmware update systems over the year, and every time
I have learned something new. How do I package my images? How do I make sure I
don't brick the device? How do I share information between my bootloader and my
application? Little by little all firmware engineers accumulate answers to
those questions and develop favored design patterns.


In this post, I share the device firmware update architecture I would implement
knowing everything I know now. I also highlight a few design patterns that are
particularly useful. The example comes with a fully functional example of a
multi-stage bootloader with DFU functionality.


I learned some of these lessons in this post the hard way, and I hope I can spare
you and your colleagues a few sleepless nights spent debugging firmware update
problems in the wild!

> If you'd rather listen to me present this information and see some demos in action, watch
> [this webinar recording](https://hubs.la/Q02hgRrk0)
