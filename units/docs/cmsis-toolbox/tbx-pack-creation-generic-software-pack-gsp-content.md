---
id: "tbx-pack-creation-generic-software-pack-gsp-content"
type: "concept"
domain: "pack"
title: "Pack Creation: Generic Software Pack (GSP) Content"
summary: "A GSP may provide additional middleware software such as RTOS, communication stacks, or crypto libraries."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#generic-software-pack-gsp-content"
license: "Apache-2.0"
mode: "V"
---

A GSP may provide additional middleware software such as RTOS, communication stacks, or crypto libraries.

**Hands-on Tutorial:**

- [GSP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/GSP-Pack-HandsOn) explains the steps to create a software pack.

**Pack Example:**

- [MDK-Middleware](https://github.com/ARM-software/MDK-Middleware) available on [www.keil.arm.com/packs/mdk-middleware-keil](https://www.keil.arm.com/packs/mdk-middleware-keil/overview/).

### Hints for Pack Creation

Several [tools and scripts](https://github.com/Open-CMSIS-Pack#ready-to-use-tools) help to automate the pack creation and are used in these hands-on tutorials.

- Use [C startup files](https://arm-software.github.io/CMSIS_6/latest/Core/cmsis_core_files.html) that allows the use of a DFP with any toolchain.
- For elements, use a brief description text of less than 128 characters to explain the purpose. When possible, link to documentation with detailed information.
  - Example: A component `Device:HAL:ENET` should not have description `ENET HAL Driver`, use `Ethernet HAL driver` instead.
- Consider adding [project templates](https://github.com/Open-CMSIS-Pack/STM32U5xx_DFP/tree/main/Templates) to help get started with more complex projects.
    This is useful when devices are configured using generators or provide multiple linker scripts (e.g., RAM/ROM execution).
- To distribute [toolchain agnostic examples](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#toolchain-agnostic-project) as part of packs:
  - Consider to use [`select-compiler`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#select-compiler) to make projects toolchain independent.
  - To avoid that examples need updates with every pack release, specify the [minimum pack version required](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/main/DualCore/HelloWorld.csolution.yml#L9).
  - Use [CI workflows](https://github.com/Open-CMSIS-Pack/STM32H743I-EVAL_BSP/tree/main/.github/workflows) to validate that projects compile correctly.
- Add an [overview.md file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_package_description.html) that describes the software pack's overall usage. These files are displayed on [www.keil.arm.com/packs](https://www.keil.arm.com/packs) and indexed by Web search engines.
