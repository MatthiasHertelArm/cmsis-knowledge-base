---
id: "intr-introduction-to-arm-semihosting-what-is-semihosting"
type: "concept"
domain: "debug"
title: "Introduction to ARM Semihosting: What Is Semihosting"
summary: "According to ARM documentation[^1], semihosting is a mechanism that enables code running on an ARM target to communicate and use the Input/Output facilities on a host computer that is running a debugger."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-02-16-arm-semihosting.md"
doc_source: "https://interrupt.memfault.com/blog/arm-semihosting#what-is-semihosting"
license: "CC-BY-SA-4.0"
mode: "V"
---

According to ARM documentation[^1], **semihosting** is _a mechanism that enables
code running on an ARM target to communicate and use the Input/Output facilities
on a host computer that is running a debugger_.

In other words, an ARM based MCU can run C library functions, such as
`printf()`, `scanf`, or even `fopen`, and have these interact directly with the
host computer attached to the device. By doing so, it can benefit from the
screen, the keyboard, or the disk of the host.
