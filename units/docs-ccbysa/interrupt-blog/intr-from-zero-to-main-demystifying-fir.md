---
id: "intr-from-zero-to-main-demystifying-fir"
type: "concept"
domain: "debug"
title: "From Zero to main(): Demystifying Firmware Linker Scripts"
summary: "This is the second post in our Zero to main() series."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-25-how-to-write-linker-scripts-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is the second post in our [Zero to main() series]().



[Last time](https://interrupt.memfault.com/blog/zero-to-main-1), we talked about
bootstrapping a C environment on an MCU before invoking our `main` function. One
thing we took for granted was the fact that functions and data end up in the
right place in our binary. Today, we're going to dig into how that happens by
learning about memory regions and linker scripts.



You may remember the following things happening auto-magically:

1. We used variables like `&_ebss`, `&_sdata`, ...etc. to know where each of our
   sections was placed in flash and to define where some needed to go in RAM.
2. A pointer to our `ResetHandler` was found at address 0x00000004 for the MCU
   to find.

While these things are true for many projects, they are held together at best by
convention, at worst by generations of copy/paste engineering. You'll find some
MCUs have different memory maps, some startup scripts name those variables
differently, and some programs have more or less segments.

Since they are not standardized, those things need to be specified somewhere in
our project. In the case of projects linked with a Unix-`ld`-like tool, that
somewhere is the linker script.

Once again, we will use our simple "minimal" program, available [on
Github](https://github.com/memfault/zero-to-main/blob/master/minimal).
