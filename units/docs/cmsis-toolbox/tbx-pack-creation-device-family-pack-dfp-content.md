---
id: "tbx-pack-creation-device-family-pack-dfp-content"
type: "concept"
domain: "pack"
title: "Pack Creation: Device Family Pack (DFP) Content"
summary: "The DFP provides foundation support for a device or device family and is used by:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#device-family-pack-dfp-content"
license: "Apache-2.0"
mode: "V"
---

The DFP provides foundation support for a device or device family and is used by:

- Compiler (Arm Compiler, GCC, IAR, and LLVM): startup code, project templates for bare-metal development, and memory information for linker scripts.
- Debuggers: SVD description files for peripheral awareness and debug description for configuration options.
- Programmers: download algorithms and debug description for download options.
- IDE and web portals: parameter information and links to documentation, repository, and support.
- Other technologies such as RUST or Zephyr as the DFP content can be exported.
- HAL drivers and CMSIS-Drivers that offer interfaces to device peripherals.

Therefore, a DFP collects the following information:

| Must have                | Strongly recommended          | Optional          |
|:-----------------------  |:------------------------------|:------------------|
| [Device description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_devices_pg.html) | [`Overview.md` file](https://github.com/Open-CMSIS-Pack/DFP-Pack-HandsOn/blob/main/Docs/Overview.md)                    | Project templates |
| [SVD description files](https://open-cmsis-pack.github.io/svd-spec/main/index.html)                         | Links to documentation                                                                                                  | [Debug description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html) |
| [Device Header file](https://arm-software.github.io/CMSIS_6/latest/Core/device_h_pg.html)                   | [Device features](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature) | HAL drivers       |
| [Startup files (see note)](https://arm-software.github.io/CMSIS_6/latest/Core/startup_c_pg.html)            | [Pack Requirements](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html)        | [CMSIS-Drivers](https://arm-software.github.io/CMSIS_6/latest/Driver/index.html)     |
| [Download algorithms](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/flashAlgorithm.html) |                                                                                                                         |                   |

!!! Note
    Startup files are not required if templates for a configuration generator (such as CubeMX) exports the startup code.

**Hands-on Tutorial:**

- [DFP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/DFP-Pack-HandsOn) explains the structure and creation of a Device Family Pack (DFP).

**Pack Example:**

- [STM32L4xx_DFP](https://github.com/Open-CMSIS-Pack/STM32L4xx_DFP) available on [keil.arm.com/packs/stm32l4xx_dfp-keil](https://www.keil.arm.com/packs/stm32l4xx_dfp-keil).
