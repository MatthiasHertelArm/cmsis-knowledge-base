---
id: "lfs-littlefs-spec-littlefs-technical-specification"
type: "concept"
domain: "project"
title: "littlefs SPEC: littlefs technical specification"
summary: "This is the technical specification of the little filesystem with on-disk version lfs2.1. This document covers the technical details of how the littlefs is stored on disk for introspection and tooling."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:SPEC.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md#littlefs-technical-specification"
license: "BSD-3-Clause"
mode: "V"
---

This is the technical specification of the little filesystem with on-disk
version lfs2.1. This document covers the technical details of how the littlefs
is stored on disk for introspection and tooling. This document assumes you are
familiar with the design of the littlefs, for more info on how littlefs works
check out [DESIGN.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md).

```
   | | |     .---._____
  .-----.   |          |
--|o    |---| littlefs |
--|     |---|          |
  '-----'   '----------'
   | | |
```
