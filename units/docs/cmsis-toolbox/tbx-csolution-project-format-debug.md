---
id: "tbx-csolution-project-format-debug"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `debug:`"
summary: "Control the generation of debug information."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#debug"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Control the generation of debug information.

Value                                                 | Code Generation
:-----------------------------------------------------|:------------------------------------
`on`                                                  | Generate debug information (default)
`off`                                                 | Generate no debug information

**Example:**

```yml
 build-types:
    - type: Release
      optimize: size        # optimize for size
      debug: off            # generate no debug information for the release build
```
