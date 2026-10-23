---
id: "tbx-csolution-project-format-translation-control"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control"
summary: "The following translation control options may be used at various places such as:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#translation-control"
license: "Apache-2.0"
mode: "V"
---

The following translation control options may be used at various places such as:

- [`solution:`](#solution) level to specify options for a collection of related projects
- [`project:`](#projects) level to specify options for a project
- [`groups:`](#groups) level to specify options for a specific source file group
- [`files:`](#files) level to specify options for a specific source file

!!! Note
    - The keys `define:`, `define-asm:`, `add-path:`, `add-path-asm:`, `del-path:`, and `misc:` are additive.
    - All other keys can only be defined once at the level of `solution:`, `project:`, `setup:`, `layer:`and `build-types:`. or `target-types:`. However, it is possible to overwrite these keys at the level of `group:`, `file:`, or `component:`; for example it is possible to translate a file group with a different optimize level.
