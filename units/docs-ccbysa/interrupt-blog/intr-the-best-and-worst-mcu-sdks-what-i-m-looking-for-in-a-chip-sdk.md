---
id: "intr-the-best-and-worst-mcu-sdks-what-i-m-looking-for-in-a-chip-sdk"
type: "concept"
domain: "debug"
title: "The Best and Worst MCU SDKs: What I’m looking for in a chip SDK"
summary: "My ideal chip SDK provides a way to build and flash projects using tools of my choosing. This seems like a low bar, but few meet it. Here are things chip SDKs should not do."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-10-the-best-and-worst-mcu-sdks.md"
doc_source: "https://interrupt.memfault.com/blog/the-best-and-worst-mcu-sdks#what-i-m-looking-for-in-a-chip-sdk"
license: "CC-BY-SA-4.0"
mode: "V"
---

My ideal chip SDK provides a way to build and flash projects using tools of
my choosing. This seems like a low bar, but few meet it. Here are things chip
SDKs should **not** do.

### Don’t choose my laptop OS for me!

I left Windows behind when I worked at Sun Microsystems, and I have not looked
back. Today, my daily driver is a MacBook Air.  Unfortunately, some chip vendors
require that you use their Windows-based tools to set up and build your projects.
Now that most compilers are cross-platform, there is no excuse for it.

### Don’t choose my IDE for me!

I’ve been using `vim` since college, and you can take it from my cold, dead
hands. I love `vim`! I have it configured just so. It’s lightweight, it’s fast,
and modal editing is the way to work (prove me wrong!). So you’ll understand my
dismay at the spate of Eclipse-based IDEs chip vendors want to foist upon me. I
want nothing to do with their boated, Java environments.

Instead of Eclipse-based IDE, I suggest SDKs provide Makefiles. `make` is the
lowest common denominator build system, and is well supported by many tools.
Bonus points for project files for IAR and Keil, since many of you like those
tools.

### Do include some examples

If a picture is worth a thousand words, then a working code example is worth a
million. Give me one example of each of the main use cases for your MCU. Bonus
points if you give me an example for each peripheral.
