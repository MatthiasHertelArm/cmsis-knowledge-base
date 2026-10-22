---
id: "tbx-csolution-project-format-add-path-asm"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `add-path-asm:`"
summary: "Add include paths to the command line of the development tools for assembly source files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#add-path-asm"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Add include paths to the command line of the development tools for assembly source files.

`add-path-asm:`                                            | Content
:----------------------------------------------------------|:------------------------------------
    `- <path-name>`                         | Named path to be added

!!! Note
    This control only applies to assembler source files.  For C and C++ source files use the `add-path:` node.

**Example:**

```yml
project:
  add-path-asm:
    - .\MyAsmIncludes                    # add path to assembler include files secure project's output directory
```
