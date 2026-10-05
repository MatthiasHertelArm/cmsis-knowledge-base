---
id: "tbx-csolution-project-structure-toolchain-agnostic-project"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Toolchain Agnostic Project"
summary: "Generic Translation Control settings enable projects that work across the range of supported compilers (AC6, GCC, IAR, CLANG). The Translation Control settings are mapped to specify compiler controls by the build tools."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#toolchain-agnostic-project"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

Generic [**Translation Control**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#translation-control) settings enable projects that work across the range of supported compilers (AC6, GCC, IAR, CLANG). The [**Translation Control**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#translation-control) settings are mapped to specify compiler controls by the build tools.

#### cdefault.yml

The `cdefault.yml` file contains a common set of compiler-specific settings that select reasonable defaults with [`misc:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#misc) controls for each compiler. The [`cdefault:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#cdefault) node in the `*.csolution.yml` file enables the usage of this file. The directory [`<cmsis-toolbox-installation-dir>/etc`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/installation.md) contains a `cdefault.yml` file that is used when no local copy of the `cdefault.yml` file is provided.

!!! Note
    - For reproducible builds, place a local copy of `cdefault.yml` in the directory containing the `*.csolution.yml` file.
    - Keep the default configuration options in `cdefault.yml` unless the project requires different settings.
    - For IAR, `-e` enables embedded language extensions, including CMSIS attributes such as `__weak`, `__packed`, `__noreturn`, and `__aligned`.

**Example:**

```yml
default:

  misc:
    - for-compiler: AC6
      C-CPP:
        - -Wno-macro-redefined
        - -Wno-pragma-pack
        - -Wno-parentheses-equality
        - -Wno-license-management
      C:
        - -std=gnu11
      ASM:
        - -masm=auto
      Link:
        - --entry=Reset_Handler
        - --info=summarysizes
        - --summary_stderr
        - --diag_suppress=L6314W

    - for-compiler: GCC
      C-CPP:
        - -masm-syntax-unified
        - -fomit-frame-pointer
        - -ffunction-sections
        - -fdata-sections
      C:
        - -std=gnu11
      Link:
        - --specs=nano.specs
        - --specs=nosys.specs
        - -Wl,-print-memory-usage
        - -Wl,--gc-sections
        - -Wl,--no-warn-rwx-segments   # suppress incorrect linker warning

    - for-compiler: CLANG
      C-CPP:
        - -fomit-frame-pointer
        - -ffunction-sections
        - -fdata-sections
      C:
        - -std=gnu11
      Link:
        - -Wl,-print-memory-usage
        - -Wl,--gc-sections

    - for-compiler: IAR
      C-CPP: 
        - -e
        - --dlib_config DLib_Config_Full.h
```

#### Compiler Selection

There are two ways to select a toolchain:

- An explicit [`compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler) selection in the `*.csolution.yml` project file:

```yml
solution:
  cdefault:           # use the cdefault.yml file with toolchain specific controls
  compiler: AC6       # select Arm Compiler
  :
```

- The command line option `--toolchain` of the `cbuild` or `csolution` tool overwrites any `compiler:` definition in the csolution project files.

```shell
cbuild Hello.csolution.yml --toolchain GCC
```

The solution-level [`compiler-alias:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler-alias) node accepts software components and pack conditions defined for compatible compiler toolchains while retaining the selected compiler for the build.

!!! Tip
    - [Toolchain agnostic example projects](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/pack-tools.md#project-examples) do not contain a [`compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler) selection in the [`*.csolution.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#solution) project file.
    - Instead the [`select-compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#select-compiler) node list the compilers that this *csolution project* is tested with. The [VS Code extension Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) adds the [`compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler) node based on the installed compiler in your environment.
