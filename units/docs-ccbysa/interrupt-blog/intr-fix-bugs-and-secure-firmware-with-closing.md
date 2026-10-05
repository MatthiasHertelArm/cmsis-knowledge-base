---
id: "intr-fix-bugs-and-secure-firmware-with-closing"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU: Closing"
summary: "We hope this post gave you a useful overview of how the ARMv6-M & ARMv7-M MPU works and can be leveraged to guard against software bugs and exploits."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

We hope this post gave you a useful overview of how the _ARMv6-M_ & _ARMv7-M_ MPU works and can be leveraged to guard against software bugs and exploits. Future topics we'd like to delve into on the matter include the re-designed MPU present in the _ARMv8-M_ architecture and how to use the MPU for application sandboxing (running privileged and unprivileged code).

Do you use the MPU on your products? Have you had a use case where you've leveraged some of the more interesting configuration options (i.e `SRD` region masking or more complex selection of `TEX`, `S`, `C`, `B` values for a _Cortex-M7_ with some caches)? Or do you have any questions about the material in the blog post or wish there were some other details we covered? Let us know in the discussion area below!

> Interested in learning more about debugging HardFaults? [Watch this webinar recording.](https://go.memfault.com/debugging-arm-cortex-m-mcu-webinar?utm_campaign=Debugging%20Cortex%20M%20Webinar&utm_source=blog&utm_medium=Interrupt&utm_term=Debug).
