---
id: "tbx-csolution-project-format-project-setups"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project Setups"
summary: "The setups: node can be used to create setups specific to a compiler, target type, and/or built type."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#project-setups"
license: "Apache-2.0"
mode: "V"
---

The `setups:` node can be used to create setups specific to a compiler, target type, and/or built type.

### `setups:`

The `setups:` node collects a list of `setup:` notes.  Only one setup will be selected for each context.

The result is a `setup:` that collects various toolchain options, and that is valid for all files and components in the
project. It is, however, possible to change that `setup:` settings on a [`group:`](#groups) or [`file:`](#files) level.

`setups:`                                                       |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- setup:`                                                      | **Required** | Description of the setup
    [`for-context:`](#for-context)               |   Optional   | Include group for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context)       |   Optional   | Exclude group for a list of *build* and *target* types.
    [`for-compiler:`](#for-compiler)             |   Optional   | Include group for a list of compilers.
    [`output:`](#output)                         |   Optional   | Configure the generated output files.
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
    [`linker:`](#linker)                         |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
    [`processor:`](#processor)                   |   Optional   | Processor configuration.

```yml
project:
  setups:
    - setup: Arm Compiler 6 project setup
      for-compiler: AC6
      linker:
        - script: my-project.sct
      define:
        - test: 12

   - setup: GCC project setup
     for-compiler: GCC
     linker:
       - script: my-project.inc
     define:
       - test: 11
```
