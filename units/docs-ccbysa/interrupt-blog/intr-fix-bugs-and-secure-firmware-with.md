---
id: "intr-fix-bugs-and-secure-firmware-with"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU"
summary: "On a computer when an application dereferences a NULL pointer or tries to access kernel memory we can catch it pretty easily thanks to the features provided by the MMU on the chip."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu"
license: "CC-BY-SA-4.0"
mode: "V"
---

On a computer when an application dereferences a NULL pointer or tries to access kernel memory we can catch it pretty easily thanks to the features provided by the [MMU](https://en.wikipedia.org/wiki/Memory_management_unit#Benefits) on the chip.

For embedded development on MCUs, we aren't always so lucky. A bad memory access from a task responsible for reading an accelerometer could corrupt a buffer being used elsewhere in the system to update a display! Fortunately, not all hope is lost ...



Many ARM MCUs implement an optional unit, known as the **Memory Protection Unit
(MPU)**, which lets you control how regions of memory are accessed.
In this article, we will deep dive into the unit and walk through a few practical examples of how it can be used to prevent bad memory accesses and security exploits on _Cortex-M_ devices.



> If you'd rather listen to me present this information and see some demos in action, [watch this webinar recording.](https://go.memfault.com/debugging-arm-cortex-m-mcu-webinar?utm_campaign=Debugging%20Cortex%20M%20Webinar&utm_source=blog&utm_medium=Interrupt&utm_term=Debug)
