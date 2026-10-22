---
id: "tbx-csolution-project-format-west-build"
type: "concept"
domain: "project"
title: "CSolution Project Format: West Build"
summary: "Enable the West build system integration and add Zephyr application images to the csolution project."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#west-build"
license: "Apache-2.0"
mode: "V"
---

Enable the [West build system integration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#west-build-system-integration) and add [Zephyr](https://www.zephyrproject.org/) application images to the *csolution project*.

### `west:`

Use the command `west build` to generate images from application source code specified in the `west:` node.  When the `west:` node is applied (even with an empty `app-path` source directory list), the [environment variables for the west build system](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-operation.md#west-integration) are created based on the [`compiler:`](#compiler) selection.

`west:`                                                   |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
    `app-path:`                            | **Required** | Path to the application source directory.
    `project-id:`                          |   Optional   | Project identifier (default: last sub-dir name of `app-path`).
    `board:`                               |   Optional   | Board name used for west build invocation (default: [variable `$west-board$`](#variable-west-board)).
    [`device:`](#device)                   |   Optional   | Specify the processor core for execution of the generated image (used in `*.cbuild-run.yml`).
    [`west-defs:`](#west-defs)             |   Optional   | Defines in `CMake` format. The `west-defs:` from build and target-type are added.
    `west-opt:`                            |   Optional   | Options for the `west` tool (default: empty).

### `west-defs:`

Defines for the `west build` commands are specified in CMake format. The `west-defs:` that are defined under the active target and build type are concatenated as follows:

`<west-defs> := <west:west-defs> + <target-type:west-defs> + <build-type:west-defs>`

The information provided with the `west:` and `west-def:` nodes are used to generate the command line for the `west` tool:

```bash
>west <west-opt> build --board <board> --build-dir $SolutionDir()$/out/<project-id>/$TargetType$
            --pristine {auto | always} <app-path> -- <west-defs>
```

!!! Note
    - The generated image files in the build directory (zephyr/zephyr.elf, zephyr/zephyr.hex) are added to the [`output:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md#output) node in `*.cbuild-run.yml`.
    - The CMSIS build system configures the [environment variables for west](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-operation.md#west-integration).
    - The `--sysbuild` option is not supported as the *csolution project* manages multiple applications and images.
    - The cbuild orchestration instructs `west` calls with `--pristine auto` option. The cbuild option `--rebuild` cleans temporary files before proceeding with a new build.

**Example:**

[Arm-Examples/CMSIS-Zephyr](https://github.com/Arm-Examples/CMSIS-Zephyr) explains the setup of a Zephyr project.
