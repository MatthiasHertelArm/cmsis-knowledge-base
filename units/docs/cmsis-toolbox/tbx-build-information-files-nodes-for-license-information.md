---
id: "tbx-build-information-files-nodes-for-license-information"
type: "concept"
domain: "project"
title: "Build Information Files: File Format / Nodes for License Information"
summary: "The .cbuild.<build-type>+<target-type>.yml files contain license information about each software component that is included in software packs."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#nodes-for-license-information"
license: "Apache-2.0"
mode: "V"
---

_Part of: File Format_

The `*.cbuild.<build-type>+<target-type>.yml` files contain license information about each software component that is included in software packs.

#### `licenses:`

Each different license that is used in a project context has a separate section.

`licenses:`                                              | Content
:--------------------------------------------------------|:------------------------------------
`- license:`                                             | License identifier or short description.
&nbsp;&nbsp;&nbsp; `license-agreement:`                  | File category according to Open-CMSIS-Pack specification
&nbsp;&nbsp;&nbsp; [`packs:`](#packs)                    | List of software [packs](#packs) used to generate this project context.
&nbsp;&nbsp;&nbsp; [`components:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#components)   | List of software [components](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#components) used to generate this project context.

**Example:**

```yml
  licenses:
    - license: <proprietary> END USER LICENSE AGREEMENT FOR ARM SOFTWARE DEVELOPMENT TOOLS
      license-agreement: ${CMSIS_PACK_ROOT}/Keil/MDK-Middleware/8.0.0/license_terms/license_agreement.txt
      packs:
        - pack: Keil::MDK-Middleware@8.0.0
      components:
        - component: Keil::USB&MDK:CORE@8.0.0
        - component: Keil::USB&MDK:Device:HID@8.0.0
        - component: Keil::USB&MDK:Device@8.0.0
    - license: Apache-2.0
      packs:
        - pack: ARM::CMSIS-Compiler@2.1.0
        - pack: ARM::CMSIS-Driver_STM32@1.0.0
        - pack: ARM::CMSIS-RTX@5.9.0
        :
      components:
        - component: CMSIS Driver:GPIO(API)
        - component: CMSIS Driver:I2C(API)
        - component: CMSIS Driver:SPI(API)
        :
        - component: ARM::CMSIS-Compiler:CORE@1.1.0
        - component: ARM::CMSIS-Compiler:STDERR:Custom@1.1.0
        - component: ARM::CMSIS-Compiler:STDIN:Custom@1.1.0
        :
```
