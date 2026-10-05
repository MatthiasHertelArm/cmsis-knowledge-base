---
id: "tbx-csolution-project-format-link-time-optimize"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `link-time-optimize:`"
summary: "When applied, the link-time optimization is enabled. It enables global optimizations across multiple translation units at the linker stage which typically further improves performance and reduces code size."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#link-time-optimize"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

When applied, the link-time optimization is enabled. It enables global optimizations across multiple translation units at the linker stage which typically further improves performance and reduces code size.

**Example:**

```yml
groups:
  - group:  "Main File Group"
    optimize: speed                  # optimize for execution speed
    link-time-optimize:              # enable link-time optimization for this file group
    files:
      - file: file1a.c
      - file: file1b.c
```

!!! Note
    This feature is not available with the IAR compiler.
