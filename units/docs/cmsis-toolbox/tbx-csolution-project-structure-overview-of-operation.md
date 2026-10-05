---
id: "tbx-csolution-project-structure-overview-of-operation"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Overview of Operation"
summary: "The generated build information is the interface between the common project information and development tools."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#overview-of-operation"
license: "Apache-2.0"
mode: "V"
---

The generated build information is the interface between the common project information and development tools. It allows build systems, smart editor features, static code analysis and test tools, programming tools, debuggers, trace tools, and CI/DevOps workflows to use the same resolved application and target configuration.

The diagram below outlines the operation of the `csolution` command `convert` that processes the *csolution project* with one or more [`context`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#context) configurations for an application.

!!! Tip
    - [Project Examples](#project-examples) show different project types and provide templates for user projects.
    - [Build Process Overview](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#build-process-overview) explains the complete end-to-end build process.

(figure: Operation Overview of csolution)

Input Files              | Description
:------------------------|:---------------------------------
[Generic Software Packs](https://www.keil.arm.com/packs/?q=&pack-search=&contents=software_only) | Provide re-usable software components that are typically configurable  towards a user application.
[DFP Software Pack](https://www.keil.arm.com/devices)   | Device-related information (including memory sizes) for the tool configuration.
[BSP Software Pack](https://www.keil.arm.com/boards)    | Board specific configuration (i.e. additional memory resources).
[cdefault.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#cdefault)            | When enabled with [`cdefault:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#solution), setup of toolchain specific controls and pre-defined toolchains.
[*.csolution.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#solution)         | Complete scope of the application with sub-projects. Defines [target](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-types) and [build](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#build-types) types.
[*.cproject.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#project)           | Content of an independent build step (linker or library archiver run).
[*.clayer.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#layer)               | Set of source files along with pre-configured components for reuse in different applications.

Input/Output Files       | Description
:------------------------|:---------------------------------
[*.cbuild-pack.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-packyml)  | Exact list of the packs that are used by the application; enables [reproducible builds](#reproducible-builds) as it locks the pack versions.

Output Files             | Description
:------------------------|:---------------------------------
[*.cbuild-idx.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-idxyml)  | Index file of all `*.cbuild.yml` build descriptions; contains also overall information for the application.
[*.cbuild.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-idxyml)      | Build description of a single [`*.cproject.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#project-file-structure) input file for each context.
[*.cbuild-run.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#run-and-debug-management)      | Configuration file of a *csolution project* to run and debug an application on a target.
[*.cbuild-mlops.yml](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#cbuild-mlopsyml)     | Information file for [MLOps integration](#mlops-integration) that is enabled with [`mlops:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#mlops) in the `*.csolution.yml` file.
[Run-Time Environment (RTE)](#rte-directory-structure) | Contains the user-configured files of a project along with the `RTE_Components.h` inventory file.
[Linker Script Files](#automatic-linker-script-generation) | Header file that describes the memory resources.

To generate the build information of an application project, the `csolution` command `convert` executes the following steps:

1. Read Input Files (*csolution project* and *Software Packs*)

2. Process each project context (defined by a [target-set](#working-with-target-set) or the option: `--context`):
    - Apply [`pack:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#pack), [`device:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#device), [`board:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#board), and [`compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler) to filter the content of software packs.
    - From [`groups:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#groups) add the list of user source files.
    - From [`components:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#components) add the list of component source files.

3. Generate *Output Files*:
    - Update [configuration files](#plm-of-configuration-files) in RTE directory (disable with option: `--no-update-rte`).
    - Print results of software component dependency validation.

### Source Code of Software Packs

Software packs and the related [components:](#software-components) allow you to share and reuse code. The content of a software pack is, therefore, *read-only* (with the exception of [configuration files](#configuration-settings) that are copied to the [RTE directory](#rte-directory-structure)) as these source code files should not be modified by a user.

The **benefit** is a clean project directory that only contains the user code and [configuration files](#configuration-settings) for [components:](#software-components). This keeps a [repository](#repository-contents) small and makes it easy to upgrade to a [new pack version](#plm-of-configuration-files).

!!! Note
    - During the development of a software pack, you may [install a repository](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-tools.md#install-a-repository), which contains the source of the software pack.
    - You may copy the content of a software pack to your project workspace and provide a [path to the pack](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#pack).
