---
id: "czep-zephyr-integration-with-cmsis-tool"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox"
summary: "<img src=\"./images/preview.png\" alt=\"Overview of Zephyr capabilities in Keil Studio\" width=\"330\" height=\"205\" align=\"left\">"
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md"
license: "Apache-2.0"
mode: "V"
---

[<img src="./images/preview.png" alt="Overview of Zephyr capabilities in Keil Studio" width="330" height="205" align="left">](https://armkeil.blob.core.windows.net/developer/Files/videos/KeilStudio/CMSIS-Zephyr.mp4 "Overview of Zephyr capabilities in Keil Studio")

This repository contains two basic Zephyr examples configured in the [`zephyr.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./zephyr.csolution.yml) file for multiple development boards. It uses the GCC toolchain, [Keil Studio](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack), and Zephyr's `west` build system to generate the application image.

The [Arm CMSIS Debugger](https://marketplace.visualstudio.com/items?itemName=Arm.vscode-cmsis-debugger) provides kernel-aware debugging and views for device peripherals, including the interrupt system. It is used to download and run the application on target hardware.

pyOCD supports runtime behavior analysis in CI workflows using RTT and SystemView.

Overall, Zephyr development is simplified by managing different build configurations, using an intuitive project tree, supporting multi-core configurations, and providing smart editor features such as code completion.
