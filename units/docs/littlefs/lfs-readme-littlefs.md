---
id: "lfs-readme-littlefs"
type: "concept"
domain: "project"
title: "README: littlefs"
summary: "A little fail-safe filesystem designed for microcontrollers."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#littlefs"
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

**Power-loss resilience** - littlefs is designed to handle random power
failures. All file operations have strong copy-on-write guarantees and if
power is lost the filesystem will fall back to the last known good state.

**Dynamic wear leveling** - littlefs is designed with flash in mind, and
provides wear leveling over dynamic blocks. Additionally, littlefs can
detect bad blocks and work around them.

**Bounded RAM/ROM** - littlefs is designed to work with a small amount of
memory. RAM usage is strictly bounded, which means RAM consumption does not
change as the filesystem grows. The filesystem contains no unbounded
recursion and dynamic memory is limited to configurable buffers that can be
provided statically.
