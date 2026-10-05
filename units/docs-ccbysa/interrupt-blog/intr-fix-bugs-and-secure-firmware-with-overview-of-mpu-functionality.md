---
id: "intr-fix-bugs-and-secure-firmware-with-overview-of-mpu-functionality"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU: Overview of MPU functionality"
summary: "At its core, the MPU lets you control the access to regions in \"the system address map\" (see section in reference manual). This includes memory areas like internal flash, SRAM, peripherals, and memory mapped devices (i.e external RAM/flash)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#overview-of-mpu-functionality"
license: "CC-BY-SA-4.0"
mode: "V"
---

At its core, the MPU lets you control the access to regions in "the system address map" (see section in [reference manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf)). This includes memory areas like internal flash, SRAM, peripherals, and memory mapped devices (i.e external RAM/flash).

The MPU also allows for an _application level programmers’ model_ to be implemented in software. When an _ARM Cortex-M_ based device is running code outside of an exception handler, it's referred to as running in _thread_ mode. When in _thread_ mode, code can be running as _Privileged_ or _Unprivileged_ (configured via the special-purpose `CONTROL` register). The MPU will let you change what memory regions can be accessed based on this setting. For example, while in _Unprivileged_ thread mode, all peripheral accesses (like reading from an external flash) could be disabled. It is common to use this model when an MCU is running untrusted code (i.e third party applications). In this manner, the code can be sandboxed such that the third party app can't corrupt or crash the system or steal data. This configuration setting is known as _access permissions_ (`AP`) and can be used to:

- disable all read & write accesses for privileged and/or unprivileged code.
- disable unprivileged writes
- make areas read-only for privileged and/or unprivileged code.

Additionally, the MPU let's you configure if a region of memory can be executed from using the _eXecute Never capability_ (`XN`). In a [previous article](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#section-definitions), we discussed how different regions of memory will hold code (_text_) and data. Sometimes arbitrary data (like a string from a `printf()` statement) can look like valid ARM instructions. A classic security vulnerability would be to find a way to execute this data as code, escalate privileges and harm the system or steal information. We'll explore this concept in more detail below.
