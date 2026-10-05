---
id: "csx-cmsis-toolbox-examples-in-csolutio-tool-requirements"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox Examples in *csolution project format*: Tool Requirements"
summary: "The examples use CMSIS-Toolbox 2.14.0 or higher; the Native CMake integration template requires version 2.15.0 or higher."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/README.md#tool-requirements"
license: "Apache-2.0"
mode: "V"
---

The examples use **CMSIS-Toolbox 2.14.0** or higher; the Native CMake integration template requires version 2.15.0 or higher. Depending on the example, additional tools include CMake, Ninja, Arm Compiler 6, GCC, CLANG, Arm Virtual Hardware Fixed Virtual Platforms (AVH FVP), STM32CubeMX, and West with a Zephyr workspace. Refer to the README of each example or template for its specific requirements.

Refer to [**Installation of the CMSIS-Toolbox**](https://open-cmsis-pack.github.io/cmsis-toolbox/installation) for information on the setup of a development environment with these tools.

When using VS Code with the [Arm Environment Manager](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager) the required tools are installed based on the settings in the file [`vcpkg-configuration.json`](https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/./vcpkg-configuration.json) using the [Arm Tools Artifactory](https://artifacts.tools.arm.com/).

!!! Note
    The Debug build type includes workarounds for known debugger issues. Refer to [CMSIS-Toolbox Troubleshooting](https://open-cmsis-pack.github.io/cmsis-toolbox/Troubleshooting/#stack-unwinding-fails-or-hangs) for details.
