---
id: "intr-tools-for-firmware-code-size-optim-epilogue"
type: "concept"
domain: "debug"
title: "Tools for Firmware Code Size Optimization: Epilogue"
summary: "Upon reviewing this blog post, a friend suggested I look at Bloaty by Google. You can check it out on Github or just download it from brew."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-06-best-firmware-size-tools.md"
doc_source: "https://interrupt.memfault.com/blog/best-firmware-size-tools#epilogue"
license: "CC-BY-SA-4.0"
mode: "V"
---

Upon reviewing this blog post, a friend suggested I look at Bloaty by Google.
You can check it out on [Github](https://github.com/google/bloaty) or just
download it from brew.

Bloaty is a nifty tool that wraps all the objdump analysis into a nice CLI
client, and can even tell you what sections, symbols, and files grew or shrunk
between two ELFs which would be very useful for a CI system.

What tools and techniques do you use to debug code size? Let us know in the
comments!

Next in the series, we'll talk about [compiler settings you can use to optimize
for code size](https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags).
