---
id: "tbx-csolution-project-format-define"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `define:`"
summary: "Contains a list of symbol #define statements that are passed via the command line to the development tools for C, C++ source files, or the linker script file preprocessor."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#define"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Contains a list of symbol #define statements that are passed via the command line to the development tools for C, C++ source files, or the [linker](#linker) script file preprocessor.

`define:`                                                   | Content
:-----------------------------------------------------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `- <symbol-name>`                        | #define symbol passed via command line
&nbsp;&nbsp;&nbsp; `- <symbol-name>: <value>`               | #define symbol with value passed via command line
&nbsp;&nbsp;&nbsp; `- <symbol-name>: \"<string>\"`          | #define symbol with string value passed via command line

!!! Note
    This control only applies to C and C++ source files (or to the [linker](#linker) script preprocessor).  For assembler source files use the `define-asm:` node.

**Example:**

```yml
define:                    # Start a list of define statements
  - TestValue: 12          # add symbol 'TestValue' with value 12
  - TestMode               # add symbol 'TestMode'
  - MySymbol: 100UL        # add symbol 'MySymbol' with value 100UL
  - TestSymbol: MySymbol+1 # add symbol 'TestSymbol' with value `MySymbol+1`
```
