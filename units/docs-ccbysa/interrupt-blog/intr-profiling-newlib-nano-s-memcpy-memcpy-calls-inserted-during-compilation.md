---
id: "intr-profiling-newlib-nano-s-memcpy-memcpy-calls-inserted-during-compilation"
type: "concept"
domain: "debug"
title: "Profiling newlib-nano's memcpy: `memcpy` calls inserted during compilation"
summary: "One side effect of replacing memcpy in the entire executable is that the C compiler will often insert calls to memcpy when performing certain operations- for example, when initializing a struct. See an example here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-09-07-memcpy-newlib-nano.md"
doc_source: "https://interrupt.memfault.com/blog/memcpy-newlib-nano#memcpy-calls-inserted-during-compilation"
license: "CC-BY-SA-4.0"
mode: "V"
---

One side effect of replacing `memcpy` in the entire executable is that the C
compiler will often insert calls to memcpy when performing certain operations-
for example, when initializing a struct. See an example here:

[https://godbolt.org/z/ar3rPdv85](https://godbolt.org/z/ar3rPdv85)

This can have significant performance implications if you have a hot path that
is using C structs for passing data; you might see `memcpy` end up at the top of
your profiling results.
