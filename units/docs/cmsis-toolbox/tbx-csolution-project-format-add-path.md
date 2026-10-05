---
id: "tbx-csolution-project-format-add-path"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `add-path:`"
summary: "Add include paths to the command line of the development tools for C and C++ source files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#add-path"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Add include paths to the command line of the development tools for C and C++ source files.

`add-path:`                                                | Content
:----------------------------------------------------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `- <path-name>`                         | Named path to be added

!!! Note
    This control only applies to C and C++ source files.  For assembler source files, use the `add-path-asm:` node.

**Example:**

```yml
project:
  misc:
    - for-compiler: AC6
      C: [-fshort-enums, -fshort-wchar]
    - for-compiler: GCC
      C: [-fshort-enums, -fshort-wchar]

  add-path:
    - $OutDir(Secure)$                   # add path to secure the project's output directory
```
