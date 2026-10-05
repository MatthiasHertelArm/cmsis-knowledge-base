---
id: "intr-tools-we-use-installing-gdb-for-ar-outro"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Outro"
summary: "I learned a lot wading through the different varieties of GDB floating around! I was particularly surprised at how much Python support varied across all these options. That's certainly a spot that's caused me headaches in the past."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#outro"
license: "CC-BY-SA-4.0"
mode: "V"
---

I learned a lot wading through the different varieties of GDB floating around! I
was particularly surprised at how much Python support varied across all these
options. That's certainly a spot that's caused me headaches in the past.

Overall I think the choice of toolchain/GDB depends on these criteria:

- does your SDK/platform already provide a nicely working copy?
- do you have specific needs that are not met by existing options?

The biggest difficulty overall seems to be sourcing a copy with

1. the version of Python your tools are relying on
2. supports Linux/Mac/Windows (depending on what developers on your team are
   using)

Though it might seem like an option of last resort, I was pleasantly surprised
at how straightforward it was to build GDB from source, and `crosstool-NG` gets
a special shoutout for really simplifying building a complete cross toolchain
🙌!

The great thing about these tools being open source: we have lots of options!

_(also could be considered a downfall 😅)_

Thanks so much for reading!
