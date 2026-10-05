---
id: "cc-i-o-retarget-example-project-build-project-in-vs-code"
type: "concept"
domain: "core"
title: "I/O Retarget example project: Build project in VS Code"
summary: "Arm Keil Studio Pack Extensions for VS Code include all required tools and interfaces to build the csolution projects."
status: "draft"
collection: "cmsis-compiler"
source: "ARM-software/CMSIS-Compiler@8cdaa0a:documentation/doxygen/src/rt_example.md"
doc_source: "https://github.com/ARM-software/CMSIS-Compiler/blob/8cdaa0a/documentation/doxygen/src/rt_example.md#build-project-in-vs-code"
license: "Apache-2.0"
mode: "V"
---

[Arm Keil Studio Pack Extensions](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) for VS Code
include all required tools and interfaces to build the `csolution` projects.

> - See [Arm Keil Studio for VS Code Extensions User Guide](https://mdk-packs.github.io/vscode-cmsis-solution-docs/index.html)
>   for more information about using the Keil Studio extensions.

When the project is opened in VS Code with Arm Keil Studio Extensions installed one must first ensure that the build tools are configured.
The `Arm Tools Environment Manager` should handle this automatically and create `vcpkg-configuration.json` with all the necessary tools listed.
Right-click anywhere in the workspace and select "Configure Arm Tools Environment" to modify tools configuration. See
[Arm Tools Environment Manager Overview](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager) for available functionality.

To build a project using Keil Studio extensions open [CMSIS view](https://mdk-packs.github.io/vscode-cmsis-solution-docs/userinterface.html),
open "Manage Solution Settings" view and verify that "Active Target", "Active Projects" and "Build Type" are selected. Since there is only
one option in each category they should all be automatically selected.

You can execute the build by [selecting "Build"](https://mdk-packs.github.io/vscode-cmsis-solution-docs/userinterface.html#3-actions-available-through-the-cmsis-view) from the CMSIS view.
