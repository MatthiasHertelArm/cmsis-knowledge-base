---
id: "tbx-theory-of-operation-build-process-overview"
type: "concept"
domain: "project"
title: "Theory of Operation: Build Process Overview"
summary: "This section contains details of the build process. For a high-level description, refer to Overall Workflow."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#build-process-overview"
license: "Apache-2.0"
mode: "V"
---

This section contains details of the build process. For a high-level description, refer to [Overall Workflow](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/overview.md#overall-workflow).

!!! Note
    - The tool options `--verbose` and `--debug` enable detailed output about the build process for analysis.
    - Refer to the chapter [Build Tools](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-tools.md) for more information on the command line syntax.

### `cbuild` Build Invocation

The `cbuild` utility controls the overall build process. It has two operating modes:

- **build mode** generates the application and is the default command (no explicit command required).
- **setup mode** generates the setup information for an IDE to populate dialogues, IntelliSense, and project outline views.

#### Details of the build mode

Without a specific `cbuild` command, the application is built. The typical invocation is:

```bash
cbuild <name>.csolution.yml --active <target-type>[@<target-set>] [--packs] [--update-rte] [--frozen-packs]
```

It generates the application program that is described with the `<name>.csolution.yml` project.

- When option `--packs` is used, it downloads missing *software packs* using [`cpackget`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-tools.md#cpackget-invocation).
- It calls [`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-tools.md#csolution-invocation) to process the the `<name>.csolution.yml` project.
    - With option `--update-rte` new configuration files from *software packs* are updated and the [`RTE_Components.h`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#rte_componentsh) file is recreated.
    - With option `--active` a [target with optional set](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#working-with-target-set) selects the projects and build-types that form the application.
    - With option `--frozen-packs` the file `*.cbuild-pack.yml` is used as input to issue an error when a pack version changes.
- The output are [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md) with all relevant project information for the build process.
- The option `--toolchain` can be used to explicitly select a compiler.

!!! Note
    By default, the `cbuild` invocation does not update or change configuration files in the [**RTE Directory**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#rte-directory-structure). Use the option `--update-rte` if this is required.

#### Details of the setup mode

The `cbuild setup` command prepares the data for an IDE environment. This command is called at the start of an IDE or whenever a *csolution project* file is modified. The typical invocation is:

```bash
cbuild setup <name>.csolution.yml --active <target-type>[@<target-set>] [--packs] [--update-rte] [--frozen-packs]
```

The option `--active` selects the [target-set](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#working-with-target-set) that specifies the application configuration. For an application described by a `<name>.csolution.yml` file, these steps are executed:

- Check YML file syntax against schema for all files specified by `<name>.csolution.yml`.
- Check the correctness of all files specified by `<name>.csolution.yml`.
- Evaluate the potential [software layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#configurations) for [Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/ReferenceApplications.md) using `variables:` to refer to layers (if the value is undefined). All projects are considered in this step.
- Evaluate the [selectable compiler toolchains](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#select-compiler) when the *csolution project* does not contain a `compiler:` selection or the `--toolchain` option is not applied. The available toolchains are based on the [compiler registration](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/installation.md#compiler-registration) and the `select-compiler:` node in the file [`<name>.csolution.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#solution) or [`cdefault.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#cdefault).
- Create the files `compile_commands.json` and `compile_macros.h` in the [output directory](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#output-directory-structure) for every context that belongs to the active target-set.

!!! Note
    The file `compile_commands.json` is generated by `CMake` with the target `<context>-database` and contains all source files of the context along with compiler options. The generated `compile_macros.h` records the selected toolchain's built-in macros and is included by the compilation database commands. This makes the macros available to code-analysis tools that consume only `compile_commands.json`, without requiring IDE-specific configuration. These files are used by various code analyzer tools and the [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) system of an IDE. For practical desktop and CI workflows, refer to [Static Code Analysis](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-tools.md#static-code-analysis).

The operation is further controlled by options:

- The option `--packs` downloads missing software packs.
- The option `--active` selects a [target with optional set](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#working-with-target-set) that combines various projects with defined build-types.
- The option [`--update-rte`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#rte-directory-structure) updates the configuration files of the application.
- With the option `--frozen-packs` the file `*.cbuild-pack.yml` is used as input. An error is issued when a pack version changes.
- The option `--toolchain` can be used to explicitly select a compiler.

### `csolution` Project Manager

[`csolution`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md) processes the [*csolution project files* (in YAML format)](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md) and the `*.pdsc` metadata files of *software packs* and performs the following operations:

- In the [**Project Area**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#project-area):
    - Generate [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md) `*.cbuild-idx.yml` and `*.cbuild.yml` with all relevant project information for the build process.
- In the [**RTE Directory**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#rte-directory-structure):
    - Generate for each [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#context) the [RTE_components.h](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#rte_componentsh) file and pre-include files from the software pack (`*.pdsc`)  metadata.
    - [Copy the configuration files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#plm-of-configuration-files) from selected software components and provide [PLM](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#plm-of-configuration-files) information.
- In the [**base directory of the solution**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#project-area):
    - Generate the file `*.cbuild-pack.yml` that records all used *software packs*. With the option `--frozen-packs`, this file is used as input.

The picture below outlines the operation.

(figure: Operation of `csolution` tool)

### `cbuild2cmake` Generate CMakeLists Files

`cbuild2cmake` reads the [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md) `*.cbuild-idx.yml` and `*.cbuild.yml` to get all relevant project information for the build process. It generates the following output files for `CMake` build system:

Output Directory/File                    | Description
:----------------------------------------|:----------------
`./<tmp-dir>/CMakeList.txt`              | Describes the overall application build process with the current [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#context) configuration.
`./<tmp-dir>/<context>`                  | Each context has a separate sub-directory with the following files:
`./<tmp-dir>/<context>/CMakeList.txt`    | Describes the build process for this context.
`./<tmp-dir>/<context>/toolchain.cmake`  | Describes the toolchain used for this context.
`./<tmp-dir>/<context>/groups.cmake`     | Contains all definitions and source files that are related to file [groups](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#groups).
`./<tmp-dir>/<context>/components.cmake` | Contains all definitions and source files that are related to [components](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#components).

### `CMake` Invocation

The CMake build system is invoked with the following commands:

- CMake configuration command defines the build generator, source, and build directory with:

  `cmake -G Ninja -S <tmpdir> -B <tmpdir> -Wnodev`

- CMake build command to build the application program for each [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#context) with:

  `cmake --build <tmpdir> -j <n> --target <context>`

- CMake build command automatically executed by `cbuild setup` to generate `compile_commands.json` for each [context](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/build-overview.md#context):

  `cmake --build <tmpdir> -j <n> --target <context>-database`
