---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-configure-vs-code-settings"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Configure VS Code settings"
summary: "VS Code needs to know where the external Alif SETOOLS and SEGGER J-Link tools are installed."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#configure-vs-code-settings"
license: "CC-BY-SA-4.0"
mode: "V"
---

VS Code needs to know where the external Alif SETOOLS and SEGGER J-Link tools are installed. 

To configure the settings on VS Code:

1. Open the Command Palette and run **Preferences: Open User Settings (JSON)**.
2. Add the following settings, updating the paths for your operating system:

  ```json
  {
    "alif.setools.root": "path/to/your/setools-folder",
    "cortex-debug.JLinkGDBServerPath": "/Applications/SEGGER/JLink/JLinkGDBServerCLExe"
  }
  ```
  If your settings file already contains entries, add only these two settings inside the existing braces.
