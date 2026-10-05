---
id: "tbx-csolution-project-structure-linker-script-management"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Linker Script Management"
summary: "A Linker Script contains a series of Linker directives that specify the available memory and how it should be used in a project. The Linker directives reflect exactly the available memory resources and memory map for the project context."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#linker-script-management"
license: "Apache-2.0"
mode: "V"
---

A Linker Script contains a series of Linker directives that specify the available memory and how it should be used in a project. The Linker directives reflect exactly the available memory resources and memory map for the project context.

This section describes the Linker Script management of the **`csolution` Project Manager**:

1. The [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) node specifies an explicit Linker Script and/or memory regions header file. This overrules Linker Scripts that are part of software components or specified using the `file:` notation.

2. The [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) `auto:` enables the [automatic Linker Script generation](#automatic-linker-script-generation).

3. If no [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) node is used, a Linker Script file can be provided as part of software components. The extensions `.sct`, `.scf`, `.ld`, and `.icf` are recognized as Linker Script files.

4. If no Linker Script is found, the [automatic Linker Script generation](#automatic-linker-script-generation) is used.

### Linker Script Preprocessing

(figure: Linker Script File Generation)

A standard C preprocessor is used for the Linker Script file when:

- the linker script file extension is `*.src`.
- the [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) node contains a `regions:` header file or a `define:`.

Otherwise, no preprocessor is used, and the Linker Script file is directly passed to the linker.

!!! Note
    - If the [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#linker) specifies a `script:` or `regions:` files, the [automatic Linker Script generation](#automatic-linker-script-generation) is disabled.
    - Some toolchains (for example GNU ld) support splitting a linker script into multiple files using an `INCLUDE` directive. Ensure that these included files are reachable by the linker (recommended is the use of relative paths in the `INCLUDE` directive). For portable projects, prefer a preprocessed linker script (`*.src`) and include a `regions:` header.

### Automatic Linker Script generation

The automatic Linker Script generation uses a Linker Script template and generates a `<regions>.h` file based on information from the software packs using the:

- [`<device>` - `<memory>` element in the DFP](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html#element_board_memory)
- [`<board>` - `<memory>` element in the BSP](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory)

Both files, the Linker Script template and the `<regions>.h` are located in the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-overview.md#rte-directory-structure) path `\RTE\Device\<device>`. The `<regions>.h` file name is extended with:

- `Bname` when the project context uses a [`board:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#board-name-conventions) specification, i.e. `regions_IMXRT1050-EVKB.h`
- `Dname` when the project context only uses a [`device:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#device-name-conventions) specification, i.e. `regions_stm32u585xx.h`.

Both files, the Linker Script template and the `<regions>.h` can be modified by the user as it might be required to adjust the memory regions or give additional attributes (such as `noinit`).

!!! Note
    For more information, refer to [Create Applications: Configure Linker Scripts](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/CreateApplications.md#configure-linker-scripts).

#### Linker Script Templates

The following compiler-specific Linker Script template files are copied to the `\RTE\Device\<device>` directory when no Linker Script exists. The files are located in the directory [`<cmsis-toolbox-installation-dir>/etc`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/installation.md) of the CMSIS-Toolbox.

Linker Script Template       | Linker control file for ...
:----------------------------|:-----------------------------
`ac6_linker_script.sct.src`  | Arm Compiler
`gcc_linker_script.ld.src`   | GCC Compiler
`iar_linker_script.icf.src`  | IAR Compiler
`clang_linker_script.ld.src` | CLANG Compiler (LLVM)

!!! Important
    [CLANG v21 (ATfE)](https://developer.arm.com/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded) uses picolibc initialization support that requires the linker symbols `__bothinit_array_start` and `__bothinit_array_end`. The current `clang_linker_script.ld.src` template defines these symbols around the pre-initialization and initialization arrays. When upgrading an existing project to CLANG v21 (ATfE), update any customized or previously copied CLANG linker script accordingly.
