---
id: "tbx-build-information-files-nodes-for-file-management"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / Nodes for File Management"
summary: "Keyword | Description :----------------|:------------------------------------ groups: | Start of a list that adds source groups and files. components: | Start of a list that adds software components."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#nodes-for-file-management"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

Keyword          | Description
:----------------|:------------------------------------
`groups:`        | Start of a list that adds source groups and files.
`components:`    | Start of a list that adds software components.

#### `linker:`

`linker:`                                         | Content
:-------------------------------------------------|:--------------------------------
`- regions:`                                      | Path and file name of `regions_<device_or_board>.h`, used to generate a Linker Script via pre-processor.
`- script:`                                       | Path and file name of the pre-processed Linker Script template.
[`- define:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define)         | Define symbol settings for the linker script file preprocessor.

#### `groups:`

`groups:`                                                      | Content
:--------------------------------------------------------------|:------------------------------------
`- group:`                                                     | Name of the group.
    [`optimize:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#optimize) | Optimize level for code generation.
    [`debug:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debug)       | Generation of debug information.
    [`warnings:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#warnings) | Control generation of compiler diagnostics.
    [`define:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define)     | Define symbol settings for code generation.
    [`add-path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-path) | Additional include file paths.
    [`misc:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#misc)         | Literal tool-specific controls.
    [`groups:`](#groups)                        | Start a nested list of groups.
    [`files:`](#files-of-a-group)               | List of files that belong to a group

#### `files:` of a group

`files:`                                                       | Content
:--------------------------------------------------------------|:------------------------------------
`- file:`                                                      | Name of the file.
    [`category:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileCategoryEnum) | File category according to Open-CMSIS-Pack specification
    [`optimize:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#optimize) | Optimize level for code generation.
    [`debug:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debug)       | Generation of debug information.
    [`warnings:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#warnings) | Control generation of compiler diagnostics.
    [`define:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define)     | Define symbol settings for code generation.
    [`add-path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-path) | Additional include file paths.
    [`misc:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#misc)         | Literal tool-specific controls.

#### `apis:`

`apis:`                                                        | Content
:--------------------------------------------------------------|:------------------------------------
`- api:`                                                       | Name of the API.
    [`condition:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition) | Reference to the condition ID of the software pack that triggered the inclusion of this API.
    `from-pack:`                                | Pack that defines this API.
    `implemented-by:`                           | Refers to the software component that implements the API.
    [`files:`](#files-of-a-component)           | List of files that belong to this API.

#### `components:`

`components:`                                                  | Content
:--------------------------------------------------------------|:------------------------------------
`- component:`                                                 | Name of the software component.
    [`condition:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition) | Reference to the condition ID of the software pack that triggered the inclusion of this component.
    `from-pack:`                                | Pack that defines this component.
    `selected-by:`                              | The original component name used in `cproject/clayer.YML`.
    [`optimize:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#optimize) | Optimize level for code generation.
    [`debug:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debug)       | Generation of debug information.
    [`warnings:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#warnings) | Control generation of compiler diagnostics.
    [`define:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#define)     | Define symbol settings for code generation.
    [`add-path:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-path) | Additional include file paths.
    [`misc:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#misc)         | Literal tool-specific controls.
    `instances:`                                | Number of component instances configured.
    `maxInstances:`                             | Maximum number component instances that can be configured.
    [`generator:`](#generator)                  | Generator information for components that are configurable via a generator.
    `implements:`                               | Refers to the API that the component is based on.
    [`files:`](#files-of-a-component)           | List of files that belong to this component.

#### `files:` of a component

`files:`                                                       | Content
:--------------------------------------------------------------|:------------------------------------
`- file:`                                                      | Name and path to the file.
    [`category:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileCategoryEnum) | File category according to Open-CMSIS-Pack specification
    [`attr:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileAttributeEnum) | File category according to Open-CMSIS-Pack specification; `api` refers to header files that define the api of a component.
    [`condition:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition) | Reference to the condition ID of the software pack that triggered the inclusion of this file.
    `select:` | Selection text for user code template files and api header files.
    [`version:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_files)     | For files that belong to components the version specified in the PDSC file.
    [`base:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#plm-of-configuration-files)     | Unmodified configuration file (base file from the *software pack*) that is currently in use.
    [`update:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#plm-of-configuration-files)   | New configuration file from an updated *software pack*.
    `status:`                                                   | Action for configuration file update: suggested, recommended, required.

#### `constructed-files:`

A list of files that are generated by the RTE management of the `csolution` tool.

`constructed-files:`                                     | Content
:--------------------------------------------------------|:------------------------------------
`- file:`                                                | Name and path to the file.
    [`category:`](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#FileCategoryEnum) | File category according to Open-CMSIS-Pack specification.
