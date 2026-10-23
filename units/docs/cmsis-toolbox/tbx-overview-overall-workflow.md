---
id: "tbx-overview-overall-workflow"
type: "concept"
domain: "project"
title: "Overview: Overall Workflow"
summary: "The CMSIS-Toolbox includes the following tools for the creation of embedded applications:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/overview/#overall-workflow"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Toolbox includes the following tools for the creation of embedded applications:

Tool                     | Description
:------------------------|:-----------------------
[cpackget](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#cpackget-invocation)  | Pack Manager: install and manage software packs in the host development environment.
[cbuild](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#cbuild-invocation)      | Build Invocation: orchestrate the build steps utilizing CMSIS tools and a CMake compilation process.
[csolution](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#csolution-invocation)| Project Manager: create build information for embedded applications that consist of one or more related projects.

These tools use *software packs* for device/board support and access to reusable software components. The operation is controlled via [*csolution project files* in YAML format](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/YML-Input-Format.md). The overall application is defined in the `*.csolution.yml` file and contains one or more projects that can utilize pre-configured software layers. The build engine CMake/Ninja calls the C/C++ compiler toolchain that generates the Build Output.

The [**cbuild**](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#cbuild-invocation) command orchestrates the overall build steps. This command calls individual tools to generate the application as outlined in the following diagram.

(figure: cbuild workflow)

The build steps are:

1. [**cpackget**](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#cpackget-invocation) downloads *Software Packs* that are required for `*.csolution.yml` when using the option `--pack`.
2. [**csolution**](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#csolution-invocation) processes the *csolution project* and the *Software Packs* to generate the overall *Build Information*. Refer to [CSolution Project Structure](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#overview-of-operation) for details.
3. **cbuild2cmake** converts this *Build Information* into CMake format.
4. **CMake/Ninja** call the C/C++ compiler toolchain to translate the source files into the application image.

Further information:

- [Theory of Operation: Build Process Overview](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-operation.md#build-process-overview) for details about the build process.
- [Installation: Compiler Toolchains](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/installation.md#compiler-toolchains) for a list of supported compilers.
  
!!! Notes
    - This documentation uses the filename extension `*.yml`, but the extension `*.yaml` is also supported.
    - The term *CMSIS solution* refers to an application project that is specified with *csolution project files* (`*.csolution.yml`, `*.cproject.yml`, and `*.clayer.yml`).
    - *Software packs* describe software components in Open-CMSIS-Pack format that can contain middleware, drivers, board support, or device support. *Software packs* also provide documentation, examples, and reusable software layers.
    - The CMSIS-Toolbox build system does not use the CMake compiler and linker flags specified by environment variables [CFLAGS, LDFLAGS](https://cmake.org/cmake/help/latest/envvar/CFLAGS.html).
