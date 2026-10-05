---
id: "intr-tools-for-firmware-code-size-optim"
type: "concept"
domain: "debug"
title: "Tools for Firmware Code Size Optimization"
summary: "Every firmware engineer has run out of code space at some point or another. Whether they are trying to cram in another feature, or to make enough space for A/B firmware updates more code space is always better."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-06-best-firmware-size-tools.md"
doc_source: "https://interrupt.memfault.com/blog/best-firmware-size-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

Every firmware engineer has run out of code space at some point or another.
Whether they are trying to cram in another feature, or to make enough space for
[A/B firmware
updates](https://sbabic.github.io/swupdate/overview.html#double-copy-with-fall-back)
more code space is always better.



In this [series of posts](), we'll explore ways to save code space and ways not to
do it. We will cover compiler options, coding style, logging, as well as
desperate hacks when all you need is another 24 bytes.

But first, let's talk about measuring code size.
