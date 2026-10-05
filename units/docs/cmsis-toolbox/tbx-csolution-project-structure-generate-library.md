---
id: "tbx-csolution-project-structure-generate-library"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Generate Library"
summary: "A library is a collection of pre-build source code that is stored in a single archive file. A library is typically used by many applications and is compiled for a series of devices that share the same processor."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#generate-library"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A library is a collection of pre-build source code that is stored in a single archive file. A library is typically used by many applications and is compiled for a series of devices that share the same processor. It uses fixed compiler options and does not expose source code. It keeps projects smaller and reduces build time by avoiding repeated compilation of the same sources.

A library may use APIs from other software components. In this case, you typically want to use the component header files, but exclude the component source files from the generated library archive. The `build-scope:` attribute of a [`component:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#components) to controls whether component source files are compiled as part of the current build (default: `include` for image builds, `exclude` for library builds).

**Example:**

The `Library.csolution.yml` file selects the toolchain (`compiler: AC6`), the target processor and a the build options.
The related `Library.cproject.yml` file sets the output to a library archive (`output: type: lib`), declares the required packs/components, and lists the source files that are compiled into the library.

`Library.csolution.yml` file:

```yml
solution:
  cdefault:                              # Default compiler configuration
  packs:
    - pack: ARM::Cortex_DFP              # Generic Device Pack

  compiler: AC6

  target-types:
    - type: Cortex-M4                    # Create for Cortex-M4 processor with FPU
      device: ARMCM4

  build-types:
    - type: Library
      optimize: size
      debug: off

  projects:
    - project: Library.cproject.yml
```

`Library.cproject.yml` file:

```yml
project:
  output:
    type: lib    # generate library

# List packs and components that the library depends on
  packs:
    - pack: ARM::CMSIS
    - pack: ARM::CMSIS-RTX

  components:
    - component: CMSIS:CORE
    - component: CMSIS:RTOS2:Keil RTX5&Source
      build-scope: include              # include RTX source code in library

# List source files that are included in the library
  groups:
    - group: Library
      files:
        - file: myfile1.c
        - file: myfile2.c
```

!!! Tip
    The [CMSIS-RTX](https://github.com/ARM-software/CMSIS-RTX) project includes a [Library directory](https://github.com/ARM-software/CMSIS-RTX/blob/main/Library) with the setup for multiple library variants. The software pack uses conditions in the [pack description file (`*.pdsc`)](https://github.com/ARM-software/CMSIS-RTX/blob/main/ARM.CMSIS-RTX.pdsc) to select the correct library variant for Arm Cortex processors and compiler variants.
