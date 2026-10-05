---
id: "intr-from-zero-to-main-bare-metal-c-closing"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bare metal C: Closing"
summary: "All the code used in this blog post is available on Github."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-14-zero-to-main-1.md"
doc_source: "https://interrupt.memfault.com/blog/zero-to-main-1#closing"
license: "CC-BY-SA-4.0"
mode: "V"
---

All the code used in this blog post is available on
[Github](https://github.com/memfault/zero-to-main/tree/master/minimal).



More complex programs often require a more complicated `Reset_Handler`. For
example:
1. Relocatable code must be copied over
2. If our program relies on libc, we must initialize it
  _EDIT: Post written!_ - [From Zero to main(): Bootstrapping libc with Newlib](https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib)
3. More complex memory layouts can add a few copy / zero loops

We'll cover all of them in future posts. But before that,
we'll talk about how the magical memory region variables come about,
how our `Reset_Handler`'s address ends up at `0x00000004`, and how to write a
linker script in our next post!

_EDIT: Post written!_ - [From Zero to main(): Demystifying Firmware Linker Scripts](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware)
