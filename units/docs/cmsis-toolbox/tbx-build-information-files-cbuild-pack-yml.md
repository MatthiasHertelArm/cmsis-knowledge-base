---
id: "tbx-build-information-files-cbuild-pack-yml"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / `*.cbuild-pack.yml`"
summary: "The <solution-name>.cbuild-pack.yml file contains the pack information for the csolution project. It is structured as outlined below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#cbuild-pack-yml"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The `<solution-name>.cbuild-pack.yml` file contains the [pack information](#lock-pack-versions) for the *csolution project*. It is structured as outlined below.

`cbuild-pack:`                                                     | Content
:------------------------------------------------------------------|:------------------------------------
    `resolved-packs:`                               | List of packs used to create the project contexts.

`resolved-packs:`                                                  | Content
:------------------------------------------------------------------|:------------------------------------
`- resolved-pack:`                                                 | [pack name](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#pack-name-conventions) used.
    `selected-by-pack:`                             | List of [components](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#component-name-conventions) included from the pack.

**Example:**

```yml
cbuild-pack:
  resolved-packs:
    - resolved-pack: ARM::CMSIS@5.9.0
      selected-by:
        - ARM::CMSIS
    - resolved-pack: ARM::V2M_MPS3_SSE_300_BSP@1.2.0
      selected-by:
        - ARM::V2M_MPS3_SSE_300_BSP@1.2.0
    - resolved-pack: Keil::ARM_Compiler@1.7.2
      selected-by:
        - Keil::ARM_Compiler
```
