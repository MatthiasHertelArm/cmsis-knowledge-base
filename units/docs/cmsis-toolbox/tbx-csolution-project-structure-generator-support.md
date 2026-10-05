---
id: "tbx-csolution-project-structure-generator-support"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Generator Support"
summary: "The steps for creating a .csolution.yml application with a Generator are:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#generator-support"
license: "Apache-2.0"
mode: "V"
---

*Generators*, such as STM32CubeMX or MCUXpresso Config Tools, simplify the configuration for devices and boards. The CMSIS-Toolbox implements a [generic interface for generators](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#generator-integration). *Generators* may be used to:

- Configure device and/or board settings, such as clock configuration or pinout.
- Add and configure software drivers, for example, for UART, SPI, or I/O ports.
- Configure parameters of an algorithm, such as DSP filter design or motor control parameters.

The steps for creating a `*.csolution.yml` application with a *Generator* are:

1. Create the `*.csolution.yml` container that refers to the projects and selects `device:` or `board:`  (by using `target-types:`)
2. Create `*.cproject.yml` files that are referred to by the `*.csolution.yml` container.
3. Add `components:` to the `*.cproject.yml` file.
4. For components that have a `<generator-id>`, run the related generator.

The *Generator* can add files, components, and settings to a project using the [*Generator* import file (`*.cgen.yml`)](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#generator-import-file). The format of this file is similar to a [software layer](#software-layers).

### Use a Generator

An example that uses STM32CubeMX is provided in [github.com/Open-CMSIS-Pack/csolution-examples](https://github.com/Open-CMSIS-Pack/csolution-examples). The `./CubeMX` example is used below.

To list the *Generator* configuration of a `*.csolution.yml` use:

```bash
csolution CubeMX.csolution.yml list generators --active MyBoard@Debug --verbose
CubeMX (Global Registered Generator)                 # Name of the Generator
  base-dir: STM32CubeMX/MyBoard                      # Generator output directory for context listed below
    cgen-file: STM32CubeMX/MyBoard/CubeMX.cgen.yml
      context: CubeMX.Debug+MyBoard
```

To run the generator (in this case CubeMX) use:

```bash
csolution CubeMX.csolution.yml run --generator CubeMX --active MyBoard@Debug
```

### Configure Generator Output

The *Generator* output directory and the name of the [*Generator* import file (`*.cgen.yml`)](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#generator-import-file) can be configured using the node [`generators:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#generators) as shown below.

```yml
  generators:
    options:
    - generator: CubeMX
      path: ../STM32CubeMX
      name: MyConfig
```

A Generator output configuration is useful for:

- Using a [board layer](#software-layers) that is shareable across multiple projects.
- Using different configurations across a `*.csolution.yml` project.

### Detailed Usage Instructions

These chapters explain how to manage device and board configuration in more detail:

- [Configure STM32 Devices with CubeMX](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/CubeMX.md)
- [Configure NXP Devices with MCUXpresso Config Tools](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/MCUXpressoConfig.md)
