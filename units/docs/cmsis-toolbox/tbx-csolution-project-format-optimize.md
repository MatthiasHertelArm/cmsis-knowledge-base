---
id: "tbx-csolution-project-format-optimize"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `optimize:`"
summary: "Generic optimize levels for code generation."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#optimize"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Generic optimize levels for code generation.

Value                                                 | Code Generation
:-----------------------------------------------------|:------------------------------------
`balanced`                                            | Balanced optimization
`size`                                                | Optimize for code size
`speed`                                               | Optimize for execution speed
`debug`                                               | Optimize for debug experience
`none`                                                | No optimization

!!! Note
    When `optimize:` is not specified, the default optimize setting of the compiler is used.

**Example:**

```yml
groups:
  - group:  "Main File Group"
    optimize: none          # optimize this file group for debug illusion
    files:
      - file: file1a.c
      - file: file1b.c
```
