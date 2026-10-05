---
id: "alp-zephyr-vsworkbench-1-installation-install-the-required-host-tool"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Set up the Workbench for Zephyr development environment: Install the required host tools"
summary: "In the Workbench for Zephyr panel, select Install Host Tools to automatically install the required dependencies."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation/#install-the-required-host-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the Workbench for Zephyr panel, select **Install Host Tools** to automatically install the required dependencies. 

This process installs Python 3.x, CMake, the Ninja build system, Git, Device Tree Compiler (DTC), and the West meta-tool.

(figure: Workbench for Zephyr extension panel in Visual Studio Code showing the Install Host Tools button highlighted, with a checklist of required tools including Python, CMake, Ninja, Git, and Device Tree Compiler#center)
   
**Note:**
On Windows, you might see permission prompts when Workbench for Zephyr installs or runs tools. Select **Allow** to continue with the setup.

When the installation completes, select **Verify Host Tools** to confirm that each required package is installed and up to date. The panel displays the version and status for Python, CMake, Ninja, Git, and Device Tree Compiler. If any tool is missing or out of date, follow the prompts to resolve the issue before continuing.
