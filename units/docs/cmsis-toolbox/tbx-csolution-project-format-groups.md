---
id: "tbx-csolution-project-format-groups"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `groups:`"
summary: "The groups: keyword specifies a list that adds source groups and files to a project or layer:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#groups"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

The `groups:` keyword specifies a list that adds [source groups and files](#source-file-management) to a project or layer:

`groups:`                                                       |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- group:`                                                      | **Required** | Name of the group.
    [`for-context:`](#for-context)               |   Optional   | Include group for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context)       |   Optional   | Exclude group for a list of *build* and *target* types.
    [`for-compiler:`](#for-compiler)             |   Optional   | Include group for a list of compilers.
    [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
    [`debug:`](#debug)                           |   Optional   | Generation of debug information.
    [`warnings:`](#warnings)                     |   Optional   | Control generation of compiler diagnostics.
    [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     |   Optional   | Remove define symbol settings for code generation.
    [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
    [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
    [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
    [`groups:`](#groups)                         |   Optional   | Start a nested list of groups.
    [`files:`](#files)                           |   Optional   | Start a list of files.

**Example:**

See [`files:`](#files) section.
