---
id: "intr-the-hidden-cost-of-misalignment"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment"
summary: "Let's suppose you're building an even smarter fishtank. You're adding temperature and salinity sensors, logging timestamped readings to flash."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's suppose you're building an even smarter
[fishtank](https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db).
You're adding temperature and salinity sensors, logging timestamped readings to
flash. The struct _is_ your binary record format -- every field at a fixed byte
offset, so you can read it back on any system that knows the layout.

You use fixed-width types from `stdint.h` and `#pragma pack(1)` to strip out
compiler-inserted padding. This is the advice I had always received and given,
and it's correct -- as far as it goes.

But `pack(1)` costs more than you think. It **destroys the compiler's ability to
generate efficient code for _every_ field access**, including fields that are
perfectly aligned.

On RISC-V, a single 32-bit store to an aligned field in a `pack(1)` struct
compiles to 7 instructions instead of 1!



In this post, we show how to fix using the `packed` and `aligned` attributes,
and how to avoid byte-decomposition even as the struct grows in the future.
