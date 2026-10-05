---
id: "tbx-csolution-project-format-define-asm"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `define-asm:`"
summary: "Contains a list of symbol #define statements that are passed via the command line to the development tools for Assembler source files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#define-asm"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Contains a list of symbol #define statements that are passed via the command line to the development tools for Assembler  source files.

`define-asm:`                                               | Content
:-----------------------------------------------------------|:------------------------------------
    `- <symbol-name>`                        | #define symbol passed via command line
    `- <symbol-name>: <value>`               | #define symbol with value passed via command line
    `- <symbol-name>: \"<string>\"`          | #define symbol with string value passed via command line

**Example:**

```yml
define-asm:                # Start a list of define statements for Assembler source code
  - AsmValue: 12           # add symbol 'AsmValue' with value 12
```
