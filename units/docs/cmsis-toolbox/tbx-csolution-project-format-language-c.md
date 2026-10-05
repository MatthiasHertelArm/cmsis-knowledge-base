---
id: "tbx-csolution-project-format-language-c"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `language-C:`"
summary: "Set the language standard for C source file compilation."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#language-c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Set the language standard for C source file compilation.

Value                                                 | Select C Language Standard
:-----------------------------------------------------|:------------------------------------
`c90`                                                 | compile C source files as defined in C90 standard (ISO/IEC 9899:1990).
`gnu90`                                               | same as `c90` but with additional GNU extensions.
`c99` (default)                                       | compile C source files as defined in C99 standard (ISO/IEC 9899:1999).
`gnu99`                                               | same as `c99` but with additional GNU extensions.
`c11`                                                 | compile C source files as defined in C11 standard (ISO/IEC 9899:2011).
`gnu11`                                               | same as `c11` but with additional GNU extensions.
`c17`                                                 | compile C source files as defined in C17 standard (ISO/IEC 9899:2017). Experimental compiler feature new in CMSIS-Toolbox 2.6.0.
`c23`                                                 | compile C source files as defined in C23 standard (ISO/IEC 9899:2023). Experimental compiler feature new in CMSIS-Toolbox 2.6.0.
