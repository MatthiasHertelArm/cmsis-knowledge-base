---
id: "tbx-theory-of-operation-generator-integration"
type: "concept"
domain: "project"
title: "Theory of Operation: Generator Integration"
summary: "The diagram below shows how the STM32CubeMX generator is integrated into the CMSIS build process. The data flow is exemplified on STM32CubeMX (Generator ID for this example is CubeMX)."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#generator-integration"
license: "Apache-2.0"
mode: "V"
---

The diagram below shows how the STM32CubeMX generator is integrated into the CMSIS build process. The data flow is exemplified on STM32CubeMX (Generator ID for this example is `CubeMX`). The information about the project is delivered to the generator using the [Generator Information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#generator-information-files) files (`<solution-name>.cbuild-gen-idx.yml` and `<context>.cbuild-gen.yml`). This information provides `CubeMX` with the project context, such as the selected board or device, and CPU mode, such as TrustZone, disabled/enabled.

(figure: Generator Integration)

The utility [`cbridge`](https://github.com/Open-CMSIS-Pack/generator-bridge) gets as parameter the `<solution-name>.cbuild-gen-idx.yml` and calls the generator. For the `CubeMX` generator example, these files are created:

- `*.ioc` CubeMX project file with current project settings
- `*.c/.h` source files, i.e. for interfacing with drivers
- `<project-name>.cgen.yml` (created by `cbridge`) provides the data for project import into the csolution build process.

!!! Note
    The NXP MCUXpresso generator has a direct interface to the csolution project format. The [utility `cbridge`](https://github.com/Open-CMSIS-Pack/generator-bridge) is in this case not required as the  [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md) are the input and the `<project-name>.cgen.yml` is directly generated.

### Generator Start via `component`

A [`<component>`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) element with a `generator` attribute in a `*.PDSC` file is used to start the generator. Typically this component is provided in a Device Family Pack (DFP) or a Board Support Pack (BSP).

**Example component for CubeMX in DFP:**

```xml
  <component generator="CubeMX" Cclass="Device" Cgroup="CubeMX" Cversion="0.9.0">
      <description>Configure device or board with STM32CubeMX</description>
  </component>
```

!!! Note
    No `<generator>` element in the *.PDSC file is required when the [Global Generator Registry File](#global-generator-registry-file) is used. The `generator="id"` attribute of the `<component>` element in the `*.PDSC` file is the reference to the `- id:` list node in the `global.generator.yml` file.

### Global Generator Registry File

For generators with no `<generator>` element in the *.PDSC file, the `global.generator.yml` in the CMSIS-Toolbox `./etc` directory contains is used. The `generator:` node in this YAML file registers the supported generators with the following keys:

`generator:`                                         |            | Content
:----------------------------------------------------|:-----------|:------------------------------------
`- id:`                                              |**Required**| `<generator-id>` referred in the `*.PDSC` file
&nbsp;&nbsp;&nbsp; `download-url:`                   |  Optional  | URL for downloading the generator
&nbsp;&nbsp;&nbsp; `run:`                            |**Required**| Name and location of the utility that starts the generator
&nbsp;&nbsp;&nbsp; `path:`                           |**Required**| Output directory of the generator. Contains the file `*.cgen.yml`.

```yml
generator:
  - id: CubeMX
    download-url: https://www.st.com/en/development-tools/stm32cubemx.html#st-get-software
    run: ../bin/cbridge
    path: $SolutionDir()$/STM32CubeMX/$TargetType$
```

!!! Note
    The only argument to the `run:` command is the path to the [Generator Information Index File](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#generator-information-files). There are no configurable parameters for this utility. The invocation is:
    `cbridge <csolution-name>.cbuild-gen-idx.yml`

### Add Configuration Generator

The following steps add a new generator to the CMSIS-Toolbox:

1. Add a [Generator Start Component](#generator-start-via-component) to a software pack (for device configuration typically the DFP).
2. Add the configuration utility to the [Global Generator Registry File](#global-generator-registry-file) with  a pull request to the [devtools repository](https://github.com/Open-CMSIS-Pack/devtools/blob/main/tools/projmgr/templates/global.generator.yml).
3. The generator tool specified with `run:` is called with the [`*.cbuild-gen-idx.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-CBuild-Format.md#generator-import-file) as command line parameter. This file also specifies the output directory for the generated files.
4. The generator tool should generate a [*.cgen.yml file and other source files](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#file-structure-of-cgenyml) that are included in the project.

An example project where you can explore this process is [CubeMX](https://github.com/Open-CMSIS-Pack/csolution-examples/tree/main/CubeMX). It contains an example for a [*.cgen.yml file](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/main/CubeMX/STM32CubeMX/MyBoard_ROM/CubeMX.cgen.yml).
