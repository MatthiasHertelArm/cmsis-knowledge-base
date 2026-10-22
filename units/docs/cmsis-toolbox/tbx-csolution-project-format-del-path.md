---
id: "tbx-csolution-project-format-del-path"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `del-path:`"
summary: "Remove include paths (that are defined at the cproject level) from the command line of the development tools."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#del-path"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Remove include paths (that are defined at the cproject level) from the command line of the development tools.

`del-paths:`                                               | Content
:----------------------------------------------------------|:------------------------------------
    `- <path-name>`                         | Named path to be removed; `*` for all

**Example:**

```yml
  target-types:
    - type: CM3
      device: ARMCM3
      del-paths:
        - /path/solution/to-be-removed
```
