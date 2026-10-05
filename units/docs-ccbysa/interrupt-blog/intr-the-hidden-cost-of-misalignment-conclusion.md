---
id: "intr-the-hidden-cost-of-misalignment-conclusion"
type: "concept"
domain: "debug"
title: "The Hidden Cost of Misalignment: Conclusion"
summary: "#pragma pack(1) is a blunt instrument."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-03-the-hidden-cost-of-misalignment.md"
doc_source: "https://interrupt.memfault.com/blog/the-hidden-cost-of-misalignment#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

`#pragma pack(1)` is a blunt instrument. It tells the compiler "nothing about
this struct's alignment can be trusted." In most embedded codebases, that's far
more pessimistic than reality -- you packed the struct to get a stable binary
layout for serialization, not because you actually access it through misaligned
pointers.

Use `__attribute__((packed, aligned(4)))` to say what you actually mean: no
padding between fields, but the struct itself lives at an aligned address. Your
code gets smaller and faster, and the compiler still correctly byte-decomposes
the fields that genuinely need it.

As your structs evolve, alignment can silently degrade. A new field appended at
the wrong offset, and you're back to 7x the ops with no warning from the
compiler. Lint it like you lint everything else.

Individually, these are small wins -- single-digit percent improvements in code
size and throughput. But embedded mastery is the accumulation of these details.
Getting the small things right so the compiler can do its job is how you build
systems that are fast, small, and correct.









{:.no_toc}
