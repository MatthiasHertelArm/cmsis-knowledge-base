---
id: "tbx-csolution-project-format-files"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `files:`"
summary: "files: | | Content :---------------------------------------------------------------|:-------------|:------------------------------------ - file: | Required | Name of the file. for-context: | Optional | Include file for a list of build and target types."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

Add source files to a project.

`files:`                                                        |              | Content
:---------------------------------------------------------------|:-------------|:------------------------------------
`- file:`                                                       | **Required** | Name of the file.
    [`for-context:`](#for-context)               |   Optional   | Include file for a list of *build* and *target* types.
    [`not-for-context:`](#not-for-context)       |   Optional   | Exclude file for a list of *build* and *target* types.
    [`for-compiler:`](#for-compiler)             |   Optional   | Include file for a list of compilers.
    [`category:`](#filename-extensions)          |   Optional   | Explicit file category to overwrite [filename extension](#filename-extensions) assignment.
    [`language-C:`](#language-c)                 |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)             |   Optional   | Set the language standard for C++ source file compilation.
    [`optimize:`](#optimize)                     |   Optional   | Optimize level for code generation.
    [`link-time-optimize:`](#link-time-optimize) |   Optional   | Enable optimization at linker level.
    [`link:`](#link)                             |   Optional   | Link attribute for library archive files (GCC and LLVM only).
    [`debug:`](#debug)                           |   Optional   | Generation of debug information.
    [`warnings:`](#warnings)                     |   Optional   | Control generation of compiler diagnostics.
    [`define:`](#define)                         |   Optional   | Define symbol settings for C/C++ code generation.
    [`define-asm:`](#define-asm)                 |   Optional   | Define symbol settings for Assembler code generation.
    [`undefine:`](#undefine)                     |   Optional   | Remove define symbol settings for code generation.
    [`add-path:`](#add-path)                     |   Optional   | Additional include file paths for C/C++ source files.
    [`add-path-asm:`](#add-path-asm)             |   Optional   | Additional include file paths for assembly source files.
    [`del-path:`](#del-path)                     |   Optional   | Remove specific include file paths.
    [`misc:`](#misc)                             |   Optional   | Literal tool-specific controls.

!!! Note
    - It is also possible to specify a [Linker Script](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#linker-script-management). Files with the extension `.sct`, `.scf`, `.ld`, and `.icf` are recognized as Linker Script files.
    - *Symbol definition* files (sometimes called “symdefs”) that provide ROM function addresses to the linker are typically **object files**. If such a file has no filename extension (for example `rom_symbol_mbedtls`), set [`category:`](#filename-extensions) to `object`.

**Example:**

Add source files to a project or a software layer. Used in `*.cproject.yml` and `*.clayer.yml` files.

```yml
groups:
  - group:  "Main File Group"
    not-for-context:                     # includes this group not for the following:
      - .Release+Virtual                 # build-type 'Release' and target-type 'Virtual'
      - .Test-DSP+Virtual                # build-type 'Test-DSP' and target-type 'Virtual'
      - +Board                           # target-type 'Board'
    files:
      - file: file1a.c
      - file: file1b.c
        define:
          - a: 1
        undefine:
          - b
        optimize: size

  - group: "Other File Group"
    files:
      - file: file2a.c
        for-context: +Virtual               # include this file only for target-type 'Virtual'
        define:
          - test: 2
      - file: file2a.c
        not-for-context: +Virtual           # include this file not for target-type 'Virtual'
      - file: file2b.c

  - group: "Nested Group"
    groups:
      - group: Subgroup1
        files:
          - file: file-sub1-1.c
          - file: file-sub1-2.c
      - group: Subgroup2
        files:
          - file: file-sub2-1.c
          - file: file-sub2-2.c
```

It is also possible to include a file group for a specific compiler using [`for-compiler:`](#for-compiler) or a specific
target-type and/or build-type using [`for-context:`](#for-context) or [`not-for-context:`](#not-for-context).

```yml
groups:
  - group:  "Main File Group"
    for-compiler: AC6                    # includes this group only for Arm Compiler 6
    files:
      - file: file1a.c
      - file: file2a.c

  - group:  "Main File Group"
    for-compiler: GCC                    # includes this group only for GCC Compiler
    files:
      - file: file1b.c
      - file: file2b.c
```

Using `category:` allows to specify pre-include files that are project-wide or related only to the `group:`.

- A global pre-include file is added to the compiler command line for all modules of the whole project (globally).

```yml
 - group:  "Main File Group"
   files:
     - file: SystemDefinitions.h
       category: preIncludeGlobal
```

- A local pre-include file is added to the compiler command line for all modules of a group (locally).

```yml
 - group:  "Group 2"
   files:
     - file: MyDefinitions.h
       category: preIncludeLocal
```

Some toolchains use *symbol definition* files (sometimes called “symdefs”) to provide ROM function addresses to the linker. These files are typically passed to the linker as **object files**. If such a file has no filename extension (for example `rom_symbol_mbedtls_20200709`), set [`category:`](#filename-extensions) to `object` so it is passed to the linker correctly:

```yml
  - group: symdefs
    files:
      - file: rom_symbol_mbedtls_20200709
        category: object
```
