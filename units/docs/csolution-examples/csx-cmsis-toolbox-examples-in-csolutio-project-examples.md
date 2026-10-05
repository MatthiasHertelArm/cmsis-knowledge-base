---
id: "csx-cmsis-toolbox-examples-in-csolutio-project-examples"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox Examples in *csolution project format*: Project Examples"
summary: "Each csolution project example shows different aspects of the CMSIS-Toolbox. For example, the CubeMX csolution project contains two targets that show RAM and ROM execution."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/README.md#project-examples"
license: "Apache-2.0"
mode: "V"
---

Examples in this repository:

*csolution project*                  | Description
:------------------------------------|:----------------------------------
[Hello](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./Hello)                     | A simple project to get started. Requires no hardware as it runs on [AVH-FVP](https://github.com/ARM-software/AVH) simulation models.
[DualCore](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./DualCore)               | Application with multiple processors that runs on the [NXP FRDM-K32L3A6](https://www.keil.arm.com/boards/nxp-frdm-k32l3a6-989d2e5/projects/) board.
[SimpleTrustZone](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./SimpleTrustZone) | Simple TrustZone example that shows secure and non-secure projects, including how to use a prebuilt secure image. Runs on [AVH-FVP](https://github.com/ARM-software/AVH) simulation models.
[CubeMX](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./CubeMX)                   | Project that uses [STM32CubeMX](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/tree/main/docs/CubeMX.md) for device configuration and contains a RAM and ROM target.

Each *csolution project* example shows different aspects of the CMSIS-Toolbox. For example, the [CubeMX](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./CubeMX) *csolution project* contains two targets that show RAM and ROM execution.
