---
id: "tbx-pack-creation-layers"
type: "concept"
domain: "pack"
title: "Pack Creation: Layers"
summary: "Layers with connections are used to by Reference Applications to target hardware. These layers are added when a reference application is configured for a board:, typically in the IDE."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#layers"
license: "Apache-2.0"
mode: "V"
---

[*Layers*](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#software-layers) with [*connections*](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/ReferenceApplications.md#connections) are used to by [*Reference Applications*](#reference-applications) to target hardware. These layers are added when a *reference application* is configured for a `board:`, typically in the IDE.

**Register *Layers* in PDSC File:**

[*Layers*](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#software-layers) are part of a BSP and published using the [`<csolution>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_csolution_pg.html) in the PDSC file.

```xml
  <csolution>
    <clayer type="Board" path="Layers/Default" file="Board.clayer.yml" copy-to="Board/MyBoard" condition="Board-Spec"/>
  </csolution>
```

!!! Note
    Several [STM32 Board Support Packs (BSP)](https://github.com/Open-CMSIS-Pack#stm32-packs-with-generator-support)  contain *layers* that are pre-configured for certain applications. For example, the *layer* in the [ST_NUCLEO-F756ZG_BSP](https://github.com/Open-CMSIS-Pack/ST_NUCLEO-F756ZG_BSP/tree/main/Layers/Default) supports applications that require Ethernet, USB Device, UART, or I2C interfaces.
