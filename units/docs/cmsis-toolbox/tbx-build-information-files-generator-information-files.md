---
id: "tbx-build-information-files-generator-information-files"
type: "concept"
domain: "project"
title: "Build Information Files: Generator Information Files"
summary: "The csolution run command generates the following build information files in the intdir: of the related context. These files are the input to a generator and provide information about the csolution project to the generator."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#generator-information-files"
license: "Apache-2.0"
mode: "V"
---

The `csolution run` command generates the following build information files in the [`intdir:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#output-dirs) of the related `context`. These files are the input to a generator and provide information about the *csolution project* to the generator.  The files are generated in the [`tmp` directory](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#output-directory-structure) of the project and contain absolute paths.

File                    | Description
:-----------------------|:----------------------
`*.cbuild-gen-idx.yml`  | Index file of all `*.cbuild-gen.yml` build descriptions; contains also overall information for the application.
`*.cbuild-gen.yml`      | Build description of a single [`*.cproject.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#project-file-structure) input file. The format is identical with the [`*.cbuild.yml`](#cbuildyml) file.

### File Structure of `*.cbuild-gen-idx.yml`

`build-gen-idx:`                                   | Content
:--------------------------------------------------|:------------------------------------
    `generated-by:`                 | Reference to csolution tool along with version information used to generate this application.
    `generators:`                   | List of generators that are called with the `run` command.

`generators:`                                      | Content
:--------------------------------------------------|:------------------------------------
`- id:`                                            | `generator identifier` specified with the option `--generator` in the [`csolution run`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-tools.md#csolution-invocation) command.
    `output:`                       | Specifies the directory for generated files.
    `board:`                        | [Board name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#board) used for the generator.
    `device:`                       | [Device name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#device) used for the generator.
    `project-type:`                 | Describes the project type "single-core", "multi-core", "trustzone".
    `cbuild-gens:`                  | List of `*.cbuild-gen.yml` files with options that are generated for the generator run.

`cbuild-gens:`                                     | Content
:--------------------------------------------------|:------------------------------------
`- cbuild-gen:`                                    | Build information file with name `<context>.cbuild-gen.yml`; structure identical with [*.cbuild.yml](#cbuildyml).
    `project:`                      | Project name (used as a name for `*.cgen.yml` when `name:` is not specified).
    `configuration:`                | Specifies `.build-type+target-type` of this context.
    `name:`                         | Explicit name for the `*.cgen.yml` [generator import file](#generator-import-file) specified by [`generator options`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#generators-options).
    `map:`                          | Mapping to a generator-specific run-time context name specified by [`generator options`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#generators-options).

**Example:**

```yml
build-gen-idx:
  generated-by: csolution version 2.3.0
  generators:
    - id: CubeMX
      output: C:/w/csolution-examples/CubeMX/STM32CubeMX/MyBoard  # output directory
      device: STM32U585AIIx
      board: B-U585I-IOT02A
      project-type: single-core
      cbuild-gens:
        - cbuild-gen: C:/w/csolution-examples/CubeMX/tmp/CubeMX/MyBoard/Debug/CubeMX.Debug+MyBoard.cbuild-gen.yml
          project: CubeMX     # user selected name of the project
          configuration: .Debug+MyBoard
          name: BoardLayer    # create BoardLayer.cgen.yml in output directory (new in CMSIS-Toolbox 2.4.0)
          map: Boot           # map to STM32CubeMX run-time context (new in CMSIS-Toolbox 2.4.0)
```
