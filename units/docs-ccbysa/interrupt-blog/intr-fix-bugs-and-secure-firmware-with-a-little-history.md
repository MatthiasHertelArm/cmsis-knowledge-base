---
id: "intr-fix-bugs-and-secure-firmware-with-a-little-history"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU: A Little History"
summary: "The MPU made its debut as an optional feature of the ARMv7-M architecture and appears in many Cortex-M3, Cortex-M4, and Cortex-M7 based processors."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#a-little-history"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MPU made its debut as an optional feature of the [ARMv7-M](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf) architecture and appears in many _Cortex-M3_, _Cortex-M4_, and _Cortex-M7_ based processors. A very similar implementation was also added as a feature to the [ARMv6-M](https://static.docs.arm.com/ddi0419/d/DDI0419D_armv6m_arm.pdf) architecture (a simpler & lower power alternative derived from _ARMv7-M_) which some _Cortex-M0+_ processors implement. Newer architectures (such as [ARMv8-M](https://static.docs.arm.com/ddi0553/a/DDI0553A_e_armv8m_arm.pdf) used on the _Cortex-M33_) implement an improved version of the MPU but for the purposes of this article we will focus on the _ARMv6/7-M_ variant.
