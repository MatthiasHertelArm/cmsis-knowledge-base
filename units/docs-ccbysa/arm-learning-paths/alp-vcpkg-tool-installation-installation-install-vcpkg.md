---
id: "alp-vcpkg-tool-installation-installation-install-vcpkg"
type: "concept"
domain: "project"
title: "Install tools on the command line using vcpkg: Install vcpkg: Install vcpkg"
summary: "vcpkg is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, build systems, and work flows. it is maintained by the Microsoft C++ team and open source contributors."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/vcpkg-tool-installation/installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/vcpkg-tool-installation/installation/#install-vcpkg"
license: "CC-BY-SA-4.0"
mode: "V"
---

[vcpkg](https://vcpkg.io/en/index.html) is a free C/C++ package manager for acquiring and managing libraries. It runs on all platforms, build systems, and work flows. it is maintained by the Microsoft C++ team and open source contributors.

**Notice of Product License Terms:**
Your use of an Arm tool is subject to your acceptance of the End User License Agreement for Arm Software Development Tools, located within the `license_terms` folder of the downloaded archive. By installing and using the Arm tool, you agree to be bound by the terms and conditions of the End User License Agreement.


To install the tool, open your favorite Terminal application and run one of the following commands:


  **Windows (cmd):**
curl -LO https://github.com/microsoft/vcpkg-tool/releases/download/2026-04-08/vcpkg-init.cmd && .\vcpkg-init.cmd
  
  **Windows (PowerShell):**
iex (iwr -useb https://github.com/microsoft/vcpkg-tool/releases/download/2026-04-08/vcpkg-init.ps1)
  
  **Linux/macOS:**
. <(curl https://github.com/microsoft/vcpkg-tool/releases/download/2026-04-08/vcpkg-init.sh -L)
  


When done, your user profile directory should contain a `.vcpkg` folder with all necessary files and scripts.

Continue by initializing `vcpkg`.
