---
id: "ocp-sensor-sdk-example-usage"
type: "concept"
domain: "project"
title: "Sensor-SDK-Example: Usage"
summary: "This pack has not public release yet. Download or fork this repository and install it as a private pack with:"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Sensor-SDK-Example@3cee161:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example/blob/3cee161/README.md#usage"
license: "Apache-2.0"
mode: "V"
---

This pack has not public release yet. Download or fork this repository and install it as a [private pack](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools#install-a-private-software-pack) with:

```bash
cpackget add <path>/NXP.ISSDK.pdsc
```

Select a board that provides a board layer in the BSP with [ARDUINO connections](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications#connections). Currently several [ST board BSP](https://github.com/Open-CMSIS-Pack#stm32-packs-with-generator-support) provide such layers, for example the [STM32F469I-DISCO](https://www.keil.arm.com/packs/stm32f469i-disco_bsp-keil/overview/). Add this BSP pack using `cpackget`.

You may now use the [Keil Studio for VS Code](https://www.keil.arm.com/) or the [VS Code CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension and open the **Create New Solution** dialog to select this board and a sensor example.

(figure: CreateNewSolution)

The IDE will evaluate the compatible software layers and shows the **Configure Solution** view. Depending on the sensor example several options may be available.  Click **OK** to choose a selection.

(figure: Add Software Layer)

This completes the setup of the example that now contains the settings for the layers. As the solution contains a collection of similar examples, you may now choose one using the **Manage Solution**.

(figure: Select Context Set)
