---
id: "tbx-csolution-project-format-target-set"
type: "concept"
domain: "project"
title: "CSolution Project Format: Context / `target-set:`"
summary: "The target-set: specifies for a target-type: the projects and images to include along with the configuration settings for a debug adapter. It is possible to specify one or more set configurations per target-type."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#target-set"
license: "Apache-2.0"
mode: "V"
---

_Part of: Context_

The `target-set:` specifies for a `target-type:` the projects and images to include along with the configuration settings for a debug adapter. It is possible to specify one or more `set` configurations per `target-type`.
Refer to the section ["Configure Related Projects"](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#configure-related-projects) that describes how to combine multiple projects into an application.

`target-set:`                                         |              | Content
:-----------------------------------------------------|:-------------|:------------------------------------
`- set:`                                              | **Required** | Start of a configuration, optional with name. The default set is unnamed.
&nbsp;&nbsp;&nbsp; `info:`                            |   Optional   | Brief description of the configuration.
&nbsp;&nbsp;&nbsp; [`images:`](#images)               |   Optional   | List of images that belong to this set.
&nbsp;&nbsp;&nbsp; [`debugger:`](#debugger)           |   Optional   | Debugger configuration for this set.

#### `images:`

The `images:` node under `target-set:` specifies the projects with build-type and optional additional [images](#images) that belong to this configuration of the target set.

`images:`                                             |              | Content
:-----------------------------------------------------|:-------------|:------------------------------------
`- project-context:`                                  |   Optional   | Project output or with optional build-type to use. Format: `<project_name>[.build_type]`
&nbsp;&nbsp;&nbsp; `image:`                           |   Optional   | Additional image file to load.
&nbsp;&nbsp;&nbsp; [`load:`](#load)                   |   Optional   | Load mode of the image file for programmers and debug tools.
&nbsp;&nbsp;&nbsp; `info:`                            |   Optional   | Brief description of the image file.
&nbsp;&nbsp;&nbsp; [`type:`](#type)                   |   Optional   | Specifies an explicit file of the image type.
&nbsp;&nbsp;&nbsp; `load-offset:`                     |   Optional   | Offset applied when loading a image file with `type: bin` (for pyOCD only).
&nbsp;&nbsp;&nbsp; [`device:`](#device)               |   Optional   | For image files a pname can be specified to denote the processor that runs the image.

!!! Note
    - Each list node must contain either `image:` or `project-context:` (but not both).
    - The `type:` specification is only accepted for an `image:` file.
    - The `project-context:` can also refer to a [west](#west) `project-id:` with build type.

#### `load:`

Specifies the load mode for an `image:` file or the output of a `project-context:`. This information is used by programmers and debug tools and overrides the default inferred from the file type.

`load:`                              | Description
:------------------------------------|:-------------
&nbsp;&nbsp;&nbsp; `image+symbols`   | Load both the binary image and the debug symbol information (default for `project-context` and `image` with file type elf).
&nbsp;&nbsp;&nbsp; `symbols`         | Load only the debug symbol information.
&nbsp;&nbsp;&nbsp; `image`           | Load only the binary image (default `image` for other file types).
&nbsp;&nbsp;&nbsp; `none`            | No content is loaded for this image, however it is part of the build process.

For example, set `load: none` on a `project-context:` when its output is embedded in another project image and must not be programmed separately.

**Example:**

On devices with two flash banks that can be swapped (for example some STM32 devices), you may want to program a new firmware version into the inactive bank while keeping the link address at the normal execution base (so symbols match after a bank swap). With pyOCD this can be achieved by loading a `.bin` with a `load-offset:` while loading only symbols from the related `project-context:`.

```yml
target-types:
  - type: Version_1
    device: STM32L476RGTx
    target-set:
      - set:
        images:
          - image: $bin(test_v1)$
            load: image
            load-offset: 0x08080000     # program inactive flash bank (pyOCD only)
          - project-context: test_v1
            load: symbols               # do not re-program; use ELF symbols for debug
        debugger:
          name: ST-Link@pyOCD
```

#### `type:`

With `type:` an explicit file type can be specified which is required for unknown file extensions. The explicit file type overwrites the auto-detection of file types based on the file extension.

`type:`           | Auto-detected Extension | Description
:-----------------|:------------------------|:-------------
`- lib`           | `.lib`, `.a`            | Library or archive.
`- elf`           | `.axf`, `.elf`          | Executable in ELF format.
`- hex`           | `.h386`, `.hex`         | Intel HEX file in HEX-386 format.
`- bin`           | `.bin`                  | Binary image.

**Example:**

```yml
solution:
    :

  target-types:
    - type: MCXN947
      board: FRDM-MCXN947
      device: NXP::MCXN947VDF
      target-set:
        - set:                             # without id, <default> set
          debugger:
            name: ST-Link
          images:
          - project-context: core1.Debug
          - project-context: core0.Release
        - set: production                  # id for this target set
          images:
          - project-context: core1.Release
            device: :core1                 # specify the pname that runs the image
          - project-context: core0.Release
            device: :core0                 # specify the pname that runs the image

    - type: Custom-HW
      device: NXP::MCXN947VDF
      target-set:
        - set:                             # without id, <default> set
          debugger:
            name: ULINKplus
            protocol: swd
          images:
          - project-context: core1.Debug
          - project-context: core0.Release
          - image: Zephyr.elf
            load: image

  build-types:
    - type: Debug
      debug: on
      optimize: debug

    - type: Release
      debug: off
      optimize: balanced

  projects:
    - project: ./cm33_core1/core1.cproject.yml
    - project: ./cm33_core0/core0.cproject.yml
```
