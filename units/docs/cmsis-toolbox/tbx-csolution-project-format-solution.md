---
id: "tbx-csolution-project-format-solution"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure / `solution:`"
summary: "The solution: node is the start of a .csolution.yml file that collects related projects as described in the section \"Configure Related Projects\"."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#solution"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project File Structure_

The `solution:` node is the start of a `*.csolution.yml` file that collects related projects as described in the section
["Configure Related Projects"](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#configure-related-projects).

`solution:`                                               |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
    `created-by:`                          |   Optional   | Identifies the tool that created this solution.
    `created-for:`                         |   Optional   | Specifies the tool for building this solution, i.e. **CMSIS-Toolbox@2.5.0**
    `description:`                         |   Optional   | Brief description text of this solution.
    [`select-compiler:`](#select-compiler) |   Optional   | Lists the possible compiler selection that this project is tested with.
    [`cdefault:`](#cdefault)               |   Optional   | When specified, the [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#cdefaultyml) file is used to setup compiler specific controls.
    [`compiler:`](#compiler)               |   Optional   | Overall toolchain selection for this solution.
    [`compiler-alias:`](#compiler-alias)   |   Optional   | Accept components and conditions defined for compatible compiler toolchains.
    [`language-C:`](#language-c)           |   Optional   | Set the language standard for C source file compilation.
    [`language-CPP:`](#language-cpp)       |   Optional   | Set the language standard for C++ source file compilation.
    [`output-dirs:`](#output-dirs)         |   Optional   | Control the output directories for the build output.
    [`generators:`](#generators)           |   Optional   | Control the directory structure for generator output.
    [`packs:`](#packs)                     |   Optional   | Defines local packs and/or scope of packs that are used.
    [`mlops:`](#mlops)                     |   Optional   | Parameters for MLOps systems; generates `*.cbuild-mlops.yml` with ML model and NPU parameters.
    [`target-types:`](#target-types)       | **Required** | List of target-types that define the target system (device or board).
    [`build-types:`](#build-types)         |   Optional   | List of build-types (i.e. Release, Debug, Test).
    [`projects:`](#projects)               |   Optional   | List of projects that belong to the solution. May be omitted for an [image-only solution](#image-only-solution).
    [`executes:`](#executes)               |   Optional   | Additional pre or post build steps using external tools.
    [`misc:`](#misc)                       |   Optional   | Literal tool-specific controls.

**Example:**

```yml
solution:
  created-for: cmsis-toolbox@2.14 # minimum CMSIS-Toolbox version required for project build
  cdefault:                       # use default setup of toolchain-specific controls.
  compiler: GCC                   # overwrite compiler definition in 'cdefaults.yml'

  packs:
    - pack: ST                    # add ST packs in 'cdefaults.yml'

  build-types:                    # additional build types
    - type: Test                  # build-type: Test
      optimize: none
      debug: on
      packs:                      # with explicit pack specification
        - pack: ST::TestSW
          path: ./MyDev/TestSW

  target-types:
    - type: Board                 # target-type: Board
      board: NUCLEO-L552ZE-Q

    - type: Production-HW         # target-type: Production-HW
      device: STM32U5X            # specifies device

  projects:
    - project: ./blinky/Bootloader.cproject.yml
    - project: /security/TFM.cproject.yml
    - project: /application/MQTT_AWS.cproject.yml
```

#### Image-only solution

A solution may configure programming and debugging for images produced by another build system without specifying a `projects:` node. Such an image-only solution requires a `target-set:` that lists the image files and debugger configuration. An optional [`executes:`](#executes) node can invoke the external build system before the image is used.

```yml
solution:
  created-for: cmsis-toolbox@2.15.0

  target-types:
    - type: Hardware
      device: Vendor::Device
      target-set:
        - set:
          images:
            - image: ./build/application.elf
              load: image+symbols
          debugger:
            name: CMSIS-DAP@pyOCD
```

Select the target-set with `cbuild <solution>.csolution.yml --active Hardware`. The generated `*.cbuild-run.yml` describes the external images and debugger configuration even though the solution has no project context.
