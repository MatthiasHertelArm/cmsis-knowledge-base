---
id: "tbx-pack-creation-pack-generation"
type: "concept"
domain: "pack"
title: "Pack Creation: Pack Generation"
summary: "Packs may be generated using scripts. Several scripts are available on github.com/open-cmsis-pack:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#pack-generation"
license: "Apache-2.0"
mode: "V"
---

Packs may be generated using scripts. Several scripts are available on [github.com/open-cmsis-pack](https://github.com/open-cmsis-pack):

- [gen-pack](https://github.com/Open-CMSIS-Pack/gen-pack) is a library for scripts creating software packs.
- [gen-pack-action](https://github.com/Open-CMSIS-Pack/gen-pack-action) is a GitHub workflow action generating documentation and software packs.

!!! Tip
    - Arm uses GitHub actions to create packs. Review this process under the `workflow` directory on the projects available on [github.com/arm-software](https://github.com/arm-software) or [github.com/open-cmsis-pack](https://github.com/open-cmsis-pack).
    - A good simple pack project is the [CMSIS-Driver pack](https://github.com/arm-software/cmsis-driver). Once this pack is published it is available for software developers using pack managers or [web portals](https://www.keil.arm.com/packs/cmsis-driver-arm/overview/).
