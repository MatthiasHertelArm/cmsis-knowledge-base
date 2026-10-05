---
id: "lfs-design-the-design-of-littlefs"
type: "concept"
domain: "project"
title: "DESIGN: The design of littlefs"
summary: "A little fail-safe filesystem designed for microcontrollers."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#the-design-of-littlefs"
license: "BSD-3-Clause"
mode: "V"
---

A little fail-safe filesystem designed for microcontrollers.

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| littlefs |
--|     |---|          |
  '-----'   '----------'
   | | |
```

littlefs was originally built as an experiment to learn about filesystem design
in the context of microcontrollers. The question was: How would you build a
filesystem that is resilient to power-loss and flash wear without using
unbounded memory?

This document covers the high-level design of littlefs, how it is different
than other filesystems, and the design decisions that got us here. For the
low-level details covering every bit on disk, check out [SPEC.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md).
