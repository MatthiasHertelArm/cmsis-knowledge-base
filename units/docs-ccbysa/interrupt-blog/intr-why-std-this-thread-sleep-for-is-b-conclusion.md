---
id: "intr-why-std-this-thread-sleep-for-is-b-conclusion"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: Conclusion"
summary: "I cut my teeth on bare metal C code where everything was statically allocated. No malloc(). No floating point math because there was no FPU. Custom linker scripts. Debugging using GPIO pins and an oscilloscope."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

I cut my teeth on bare metal C code where _everything_ was statically allocated.
No `malloc()`. No floating point math because there was no FPU. Custom linker
scripts. Debugging using GPIO pins and an oscilloscope. Using precalculated
value tables to save a few microseconds in an ISR. We ran at 24 MHz. At that
time, C was luxurious because the "old" stuff was running at 1 MHz, usually in
assembly.

Back then common wisdom was that C++ was just not appropriate for
microcontrollers. Of course, that was a long time ago, before "modern C++" and
before MCUs were clocked at hundreds of MHz with L1 caching and multistage
instruction pipelines.

It seems today that using C++ for firmware brings up a lot of strong reactions.
A lot of embedded people hate it. A lot of people love it. For myself, I think
it can be a great tool, but it does have much complexity you need to get right,
_especially_ when using it on an MCU. This seems to be a good example of such.

I sincerely hope `usleep()` is fixed. Until then, don't use
`std::this_thread::sleep_for()` in your IDF v5 projects. It's a waste of time!









{:.no_toc}
