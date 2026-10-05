---
id: "tbx-csolution-project-structure-minimal-project-setup"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Minimal Project Setup"
summary: "A minimal application requires two files:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#minimal-project-setup"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A minimal application requires two files:

- `Sample.csolution.yml` that defines a [target type](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-types) with [board](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#board) or [device](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#device). It includes a [project](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#projects) and selects a [compiler](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#compiler).

- `Sample.cproject.yml` defines the files and software components that are translated into an image.

!!! Note
    When no [`packs:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#packs) are specified in *csolution project files*, the tools use the latest version of the installed packs.

**Simple Project: `Sample.csolution.yml`**

```yml
solution:
  cdefault:                                   # use default setup for toolchains
  compiler: AC6                               # select the compiler to use

  packs:                                      # explicit pack selection may be omitted
    - pack: NXP::K32L3A60_DFP@16.0.0          # specify DFP
    - pack: NXP::FRDM-K32L3A6_BSP@16.0.0

  target-types:
    - type: FRDM-K32L3A6
      board: FRDM-K32L3A6

  build-types:
    - type: Debug                             # toolchain options for 'debug'
      debug: on
      optimize: debug

    - type: Release                           # toolchain options for 'release'
      debug: off
      optimize: balanced

  projects:
    - project: ./Sample.cproject.yml
```

**Simple Project: `Sample.cproject.yml`**

```yml
project:
  packs:
    - pack: ARM::CMSIS                        # specify additional packs

  groups:
    - group: App
      files:
        - file: ./main.c

  components:
    - component: CMSIS:CORE
    - component: Device:Startup
```
