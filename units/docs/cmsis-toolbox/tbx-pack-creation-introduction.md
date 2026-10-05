---
id: "tbx-pack-creation-introduction"
type: "concept"
domain: "pack"
title: "Pack Creation: Introduction"
summary: "The picture below shows the structure of the different packs and how boards, devices, and examples are exposed to an user in the Arm CMSIS Solution extension for VS Code. Packs are stacked:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#introduction"
license: "Apache-2.0"
mode: "V"
---

The picture below shows the structure of the different packs and how boards, devices, and examples are exposed to an user in the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension for VS Code. Packs are stacked:

- The Device Family Pack (DFP) is the foundation.
- The Board Support Pack (BSP) is based on DFP and are an extension.
- The Generic Software Packs (GSP) should use boards defined in a BSP to publish examples or [Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/ReferenceApplications.md) that run on several boards.

(figure: Project Examples in Packs)

!!! Tip
    - A [**Blinky example**](#board-support-pack-bsp-content) in the BSP simplifies the bring up of an development environment in multiple ways.
    - The VS Code extension [CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) gets examples via a web service. All required packs are automatically installed.
    - It verifies compile, download, and hardware setup. The LED blinks with 1Hz which validates clock settings.
