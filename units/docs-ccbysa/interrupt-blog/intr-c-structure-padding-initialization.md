---
id: "intr-c-structure-padding-initialization"
type: "concept"
domain: "debug"
title: "C Structure Padding Initialization"
summary: "This article takes a look at a few different aspects of C structure initialization. In particular, we'll look at when it matters, the current state of things in Clang and GCC, recommendations, and the ✨ future ✨."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-01-c-struct-padding-initialization.md"
doc_source: "https://interrupt.memfault.com/blog/c-struct-padding-initialization"
license: "CC-BY-SA-4.0"
mode: "V"
---

This article takes a look at a few different aspects of C structure
initialization. In particular, we'll look at when it matters, the current state
of things in Clang and GCC, recommendations, and the ✨ future ✨.



Time to dive into this very niche, but occasionally hazardous corner of the C
language!
