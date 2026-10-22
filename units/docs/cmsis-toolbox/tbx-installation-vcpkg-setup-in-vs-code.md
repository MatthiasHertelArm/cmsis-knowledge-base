---
id: "tbx-installation-vcpkg-setup-in-vs-code"
type: "concept"
domain: "project"
title: "Installation: vcpkg Setup in VS Code"
summary: "Once the tools are installed, you may use the CMSIS-Toolbox commands in a Terminal window of VS Code. If the terminal icon shows a yellow triangle with an exclamation mark, you have to start a new terminal."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/installation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/installation/#vcpkg-setup-in-vs-code"
license: "Apache-2.0"
mode: "V"
---

1. Download and install [Microsoft Visual Studio Code](https://code.visualstudio.com/download) for your operating system.
2. Launch Visual Studio Code. Use the menu `View` and open `Extensions` and install the `Keil Studio Pack` extensions.
3. Use the menu `View` and open `Source Control`. Select 'Clone Repository' and enter as url [`https://github.com/Open-CMSIS-Pack/vscode-get-started`](https://github.com/Open-CMSIS-Pack/vscode-get-started).
4. Specify the destination folder to clone to and select 'Open' when asked 'Would you like to open the cloned directory?'
5. Use the `View` menu 'Explorer' and select the file `vcpkg-configuration.json`. This file instructs [Microsoft vcpkg](https://github.com/microsoft/vcpkg-tool#vcpkg-artifacts) to install the prerequisite artifacts required for building the solution and installs therefore:

    - CMSIS-Toolbox 2.6.1
    - cmake 3.28.4
    - ninja 1.12.0
    - arm-none-eabi-gcc 13.3.1-mpacbti (GNU Arm Embedded Toolchain 13.3.1)

!!! Note
    If vcpkg shows an error in the VSCode status bar, the `vcpkg` output provides further information.

Once the tools are installed, you may use the [CMSIS-Toolbox commands](https://open-cmsis-pack.github.io/cmsis-toolbox/installation/build-tools.md) in a **Terminal** window of VS Code. If the terminal icon shows a yellow triangle with an exclamation mark, you have to start a new terminal. This ensures that the environment settings updates triggered by the vcpkg activation are reflected in the terminal.

Alternatively, use `View` and open the `CMSIS` Extension. Then use the `Build` buttons to translate the project, flash your connected board and/or launch a debug connection.
