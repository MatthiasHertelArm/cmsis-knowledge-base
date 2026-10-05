---
id: "tbx-csolution-project-format-project"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure / `project:`"
summary: "The project: node is the start of a .cproject.yml file and can contain the following:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#project"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project File Structure_

The `project:` node is the start of a `*.cproject.yml` file and can contain the following:

`project:`                                                      |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `description:`                               |   Optional   | Brief description text of this project.
&nbsp;&nbsp;&nbsp; [`output:`](#output)                         |   Optional   | Configure the generated output files.
&nbsp;&nbsp;&nbsp; [`generators:`](#generators)                 |   Optional   | Control the directory structure for generator output.
&nbsp;&nbsp;&nbsp; [`rte:`](#rte)                               |   Optional   | Control the directory structure for [RTE (run-time environment)](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#rte-directory-structure) files.
&nbsp;&nbsp;&nbsp; [`packs:`](#packs)                           |   Optional   | Defines packs that are required for this project.
&nbsp;&nbsp;&nbsp; [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
&nbsp;&nbsp;&nbsp; [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
&nbsp;&nbsp;&nbsp; [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
&nbsp;&nbsp;&nbsp; [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
&nbsp;&nbsp;&nbsp; [`linker:`](#linker)                         |   Optional   | Instructions for the linker.
&nbsp;&nbsp;&nbsp; [`debug:`](#debug)                           |   Optional   | Generation of debug information.
&nbsp;&nbsp;&nbsp; [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
&nbsp;&nbsp;&nbsp; [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
&nbsp;&nbsp;&nbsp; [`undefine:`](#undefine)                     |   Optional   | Remove preprocessor (#define) symbols.
&nbsp;&nbsp;&nbsp; [`add-path:`](#add-path)                     |   Optional   | Additional include file paths.
&nbsp;&nbsp;&nbsp; [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
&nbsp;&nbsp;&nbsp; [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.
&nbsp;&nbsp;&nbsp; [`device:`](#device)                         |   Optional   | Specify processor core.
&nbsp;&nbsp;&nbsp; [`processor:`](#processor)                   |   Optional   | Processor specific settings.
&nbsp;&nbsp;&nbsp; [`setups:`](#setups)                         |   Optional   | Configurations specific to a compiler, target-type, and/or built-type.
&nbsp;&nbsp;&nbsp; [`groups:`](#groups)                         | **Required** | List of source file groups along with source files.
&nbsp;&nbsp;&nbsp; [`components:`](#components)                 |   Optional   | List of software components used.
&nbsp;&nbsp;&nbsp; [`layers:`](#layers)                         |   Optional   | List of software layers that belong to the project.
&nbsp;&nbsp;&nbsp; [`connections:`](#connections)               |   Optional   | List of consumed and provided resources.
&nbsp;&nbsp;&nbsp; [`executes:`](#executes)                     |   Optional   | Additional pre or post build steps using external tools.

**Example:**

```yml
project:
  misc:
    - compiler: AC6                          # specify misc controls for Arm Compiler 6
      C: [-fshort-enums, -fshort-wchar]      # set options for C files
  add-path:
    - $OutDir(Secure)$                       # add the path to the secure project's output directory
  components:
    - component: Startup                     # Add startup component
    - component: CMSIS CORE
    - component: Keil RTX5 Library_NS
  groups:
    - group: Non-secure Code                 # Create group
      files:
        - file: main_ns.c                    # Add files to group
        - file: $Source(Secure)$interface.h
        - file: $Output(Secure)$_CMSE_Lib.o
```
