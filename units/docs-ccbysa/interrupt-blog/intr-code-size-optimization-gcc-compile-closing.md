---
id: "intr-code-size-optimization-gcc-compile-closing"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Closing"
summary: "We hope reading this post has given you new ways to optimize the size of your firmware."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

We hope reading this post has given you new ways to optimize the size of your
firmware.

One overarching lesson is that default compiler settings are inadequate in most
cases. The default settings had our applications clocking in at over 108KiB. A
few compiler flag changes cut it down by more than half!

Future posts in this series will consider coding style, and even some desperate
hacks one can use to slim down code size further.
