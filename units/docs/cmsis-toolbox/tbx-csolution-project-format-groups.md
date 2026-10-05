---
id: "tbx-csolution-project-format-groups"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `groups:`"
summary: "The groups: keyword specifies a list that adds source groups and files to a project or layer:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#groups"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

The `groups:` keyword specifies a list that adds [source groups and files](#source-file-management) to a project or layer:

`groups:`                                                       |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- group:`                                                      | **Required** | Name of the group.
&nbsp;&nbsp;&nbsp; [`for-context:`](#for-context)               |   Optional   | Include group for a list of *build* and *target* types.
&nbsp;&nbsp;&nbsp; [`not-for-context:`](#not-for-context)       |   Optional   | Exclude group for a list of *build* and *target* types.
&nbsp;&nbsp;&nbsp; [`for-compiler:`](#for-compiler)             |   Optional   | Include group for a list of compilers.
&nbsp;&nbsp;&nbsp; [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
&nbsp;&nbsp;&nbsp; [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
&nbsp;&nbsp;&nbsp; [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
&nbsp;&nbsp;&nbsp; [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
&nbsp;&nbsp;&nbsp; [`debug:`](#debug)                           |   Optional   | Generation of debug information.
&nbsp;&nbsp;&nbsp; [`warnings:`](#warnings)                     |   Optional   | Control generation of compiler diagnostics.
&nbsp;&nbsp;&nbsp; [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
&nbsp;&nbsp;&nbsp; [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
&nbsp;&nbsp;&nbsp; [`undefine:`](#undefine)                     |   Optional   | Remove define symbol settings for code generation.
&nbsp;&nbsp;&nbsp; [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
&nbsp;&nbsp;&nbsp; [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
&nbsp;&nbsp;&nbsp; [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
&nbsp;&nbsp;&nbsp; [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
&nbsp;&nbsp;&nbsp; [`groups:`](#groups)                         |   Optional   | Start a nested list of groups.
&nbsp;&nbsp;&nbsp; [`files:`](#files)                           |   Optional   | Start a list of files.

**Example:**

See [`files:`](#files) section.
