---
id: "tbx-csolution-project-format-misc"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `misc:`"
summary: "Add miscellaneous literal tool-specific controls that are directly passed to the individual tools depending on the file type."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#misc"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Add miscellaneous literal tool-specific controls that are directly passed to the individual tools depending on the file type.

`misc:`                                    |              | Content
:------------------------------------------|:-------------|:------------------------------------
[`- for-compiler:`](#for-compiler)         |   Optional   | Name of the toolchain that the literal control string applies to.
&nbsp;&nbsp;&nbsp; `C-CPP:`                |   Optional   | Applies to `*.c` and `*.cpp` files (added before `C` and `CPP:`).
&nbsp;&nbsp;&nbsp; `C:`                    |   Optional   | Applies to `*.c` files only.
&nbsp;&nbsp;&nbsp; `CPP:`                  |   Optional   | Applies to `*.cpp` files only.
&nbsp;&nbsp;&nbsp; `ASM:`                  |   Optional   | Applies to assembler source files only.
&nbsp;&nbsp;&nbsp; `Link:`                 |   Optional   | Applies to the linker (added before `Link-C:` or `Link-CPP:`).
&nbsp;&nbsp;&nbsp; `Link-C:`               |   Optional   | Applies to the linker; added when no C++ files are part of the project.
&nbsp;&nbsp;&nbsp; `Link-CPP:`             |   Optional   | Applies to the linker; added when C++ files are part of the project.
&nbsp;&nbsp;&nbsp; `Library:`              |   Optional   | Set libraries to the correct position in the linker command line (for GCC).

**Example:**

```yml
  build-types:
    - type: Debug
      misc:
        - for-compiler: AC6
          C-CPP:
            - -O1
            - -g
        - for-compiler: GCC
          C-CPP:
            - -Og

    - type: Release
      compiler: AC6
      misc:
        - C:
          - -O3

    - type: GCC-LibDebug
      compiler: GCC
      misc:
        - Library:
          - -lm
          - -lc
          - -lgcc
          - -lnosys
```
