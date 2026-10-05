---
id: "tbx-configure-stm32-devices-with-cubem-cubemx-runtime-context-mapping"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: CubeMX Runtime Context Mapping"
summary: "Some devices, for example the STM32H7S series, provide in CubeMX runtime contexts, for example: Boot, Appli, ExtMemLoader."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#cubemx-runtime-context-mapping"
license: "Apache-2.0"
mode: "V"
---

Some devices, for example the STM32H7S series, provide in CubeMX *runtime contexts*, for example: `Boot`, `Appli`, `ExtMemLoader`. To map the *csolution* project context to these CubeMX *runtime contexts* it is required for this type of devices to use `map:` key in the `generator`: option, as shown below.

The STM32H7S series uses the following CubeMX run-time names:

- `Boot` for the boot loader.
- `Appli` for the user application program.
- `ExtMemLoader` for the part that is in external memory.

The `generators:` node is used to map a `*.cproject.yml` or `*.clayer.yml` file to a CubeMX run-time context as shown below.

```yml
generators:
    options:
    - generator: CubeMX
      map: Appli            # map project or layer to CubeMX runtime context
```
