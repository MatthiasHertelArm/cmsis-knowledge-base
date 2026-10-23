---
id: "tbx-csolution-project-format-toolchain-options"
type: "concept"
domain: "project"
title: "CSolution Project Format: Toolchain Options"
summary: "Toolchain options may be used at various places, such as:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#toolchain-options"
license: "Apache-2.0"
mode: "V"
---

Toolchain options may be used at various places, such as:

- [`solution:`](#solution) level to specify options for a collection of related projects.
- [`project:`](#projects) level to specify options for a project.

### `select-compiler:`

Lists the compilers that this *csolution project* is tested with. This information is used by the [`cbuild setup` command](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-operation.md#details-of-the-setup-mode) to determine possible compiler choices. The actual compiler to be used is selected with the [`compiler:`](#compiler) node.

!!! Note
    - [`select-compiler:`](#select-compiler) is only supported in the [`*.csolution.yml`](#solution) project file.
    - This control is new in CMSIS-Toolbox 2.5.0

`select-compiler:`                                          |            | Content
:-----------------------------------------------------------|:-----------|:-------------------------------------------
`- compiler:`                                               |**Required**| Specifies a supported compiler.

**Example:**

```yml
solution:
  created-for: cmsis-toolbox@2.5  # minimum CMSIS-Toolbox version required for project build
  select-compiler:                # list tested compilers that can be selected
    - compiler: GCC               # GCC is supported
    - compiler: AC6@6.22          # AC6 is supported, version number is a hint on what was tested
```

### `compiler:`

Selects the compiler toolchain used for code generation. It can be applied in `*.csolution.yml` files.
Optionally the compiler can have a version number specification.

Compiler ID                                           | Supported Compiler
:-----------------------------------------------------|:------------------------------------
`AC6`                                                 | Arm Compiler for Embedded version 6
`GCC`                                                 | GCC Compiler
`IAR`                                                 | IAR Compiler
`CLANG`                                               | Arm Toolchain for Embedded (CLANG frontend based on LLVM)
`CLANG_TI`                                            | TI variant of the CLANG Compiler
`XC`                                                  | Microchip variant of the GCC Compiler

!!! Note
    Refer to [Installation: Compiler Toolchains](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/installation.md#compiler-toolchains) for details about the supported compilers.

**Example:**

```yml
compiler: GCC              # Select GCC Compiler
```

```yml
compiler: AC6@6.18.0       # Select Arm Compiler version 6.18.0
```

### `compiler-alias:`

Declares a compiler toolchain that is compatible with the toolchain selected by [`compiler:`](#compiler). This allows the solution to use software components and other pack content whose conditions specify the aliased compiler. The selected compiler still performs the build.

`compiler-alias:`                                      |            | Content
:------------------------------------------------------|:-----------|:------------------------------------
`compiler-alias:`                                      |  Optional  | Compiler ID that is compatible with the selected compiler.

!!! Note
    `compiler-alias:` is supported only at the [`solution:`](#solution) level. The alias uses a compiler ID without a version.

**Example:** Use the XC compiler and accept pack content defined for GCC:

```yml
solution:
  compiler: XC
  compiler-alias: GCC
```

### `linker:`

The `linker:` node specifies an explicit Linker Script and/or memory regions header file.  It can be applied in `*.cproject.yml` and `*.clayer.yml` files.
Refer to [Linker Script Management](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#linker-script-management) for detailed information.

`linker:`                                                   |            | Content
:-----------------------------------------------------------|:-----------|:--------------------------------
`- regions:`                                                |  Optional  | Path and file name of `<regions_file>.h`, used to generate a Linker Script.
   `script:`                                 |  Optional  | Explicit file name of the Linker Script, overrules files provided with [`file:`](#files) or components.
   `auto:`                                   |  Optional  | Request [automatic Linker Script generation](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#automatic-linker-script-generation).
   [`define:`](#define)                      |  Optional  | Define symbol settings for the linker script file preprocessor.
   [`for-compiler:`](#for-compiler)          |  Optional  | Include Linker Script for the specified toolchain.
   [`for-context:`](#for-context)            |  Optional  | Include Linker Script for a list of *build* and *target* type names.
   [`not-for-context:`](#not-for-context)    |  Optional  | Exclude Linker Script for a list of *build* and *target* type names.

!!! Note
    - The `linker:` node must have at least `regions:`, `script:`, `auto:`, or `define:`.
    - If no `script:` file is specified, compiler-specific [Linker Script template files](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#linker-script-templates) are used.
    - A Linker Script file is preprocessed when `regions:` or `define:` is specified, or when the file extension is `*.src`.
    - If both `auto:` and `script:` is specified, a warning is issued, and [automatic Linker Script generation](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#automatic-linker-script-generation) is performed, and the specified `script:` is ignored.
    - The `script:` and `regions:` paths may use [access sequences](#access-sequences) such as `$Dname$` and `$Pname$` to select device/core-specific files.

**Examples:**

```yml
linker:
  - script:   MyLinker.scf.src   # linker script file
    regions:  MyRegions.h        # pre-processed using header file
```

```yml
linker:
  - script:   RTE/Device/$Dname$_$Pname$/linker_gnu.ld.src        # example device/core-specific path
    regions:  RTE/Device/$Dname$_$Pname$/regions_$Dname$_$Pname$.h # (adjust to your RTE/Device layout)
```

```yml
linker:
  - regions:  MyRegions.h        # Default linker script is used and pre-processed using header file
```

```yml
linker:
  - script:   MyLinker.scf.src   # linker script file, not pre-processed
    for-compiler: AC6            # for Arm Compiler 6

  - script:   MyLinker.ld        # linker script file, not pre-processed
    for-compiler: CLANG          # for CLANG LLVM-based compiler
```

```yml
linker:
  - script:   MyLinker.scf.src   # linker script file
    for-compiler: AC6            # for Arm Compiler 6
    regions:  MyRegions.h        # pre-processed using header file

  - script:   MyLinker.ld.src    # linker script file
    for-compiler: CLANG          # for CLANG LLVM-based compiler
    regions:  MyRegions.h        # pre-processed using header file
    define:                      # with define setting
      - Setup: 1                 # define with value
```

### `output:`

Configure the generated output files.

`output:`                              |            | Content
:--------------------------------------|:-----------|:--------------------------------
    `base-name:`        |  Optional  | Specify a common base name for all output files.
    `type:`             |  Optional  | A list of output types for code generation (see list below).

`type:`           | Description
:-----------------|:-------------
`- lib`           | Library or archive. Note: GCC uses the prefix `lib` in the base name for archive files.
`- elf`           | Executable in ELF format. The file extension is toolchain-specific.
`- hex`           | Intel HEX file in HEX-386 format.
`- bin`           | Binary image.
`- map`           | Linker MAP file.

The **default** setting for `output:` is:

```yml
output:
  base-name: $Project$   # used the base name of the `cproject.yml` file.
  type: elf              # Generate executable file.
```

**Example:**

```yml
output:
  type:
  - elf                  # Generate executable file.
  - map                  # Generate Linker MAP file.
```

```yml
output:                  # configure output files.
  base-name: MyProject   # used for all output files, including linker map file.
  type:
  - elf                  # Generate executable file.
  - hex                  # generate a HEX file.
  - bin                  # generate a BIN file.
```

Generate a **library**:

```yml
output:                  # configure output files.
  type: lib              # Generate library file.
```
