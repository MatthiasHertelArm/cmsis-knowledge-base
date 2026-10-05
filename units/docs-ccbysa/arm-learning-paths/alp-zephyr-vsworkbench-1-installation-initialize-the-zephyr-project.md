---
id: "alp-zephyr-vsworkbench-1-installation-initialize-the-zephyr-project"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Set up the Workbench for Zephyr development environment: Initialize the Zephyr project workspace"
summary: "Zephyr uses a Git-based workspace manager called West to organize its source code, modules, and samples. Use Workbench for Zephyr to initialize your first West workspace."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation/#initialize-the-zephyr-project-workspace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Zephyr uses a Git-based workspace manager called West to organize its source code, modules, and samples. Use Workbench for Zephyr to initialize your first West workspace.

In the Workbench for Zephyr panel, select **Initialize Workspace** to set up your project environment. Configure the workspace settings by selecting **Minimal from template** for the source location and using the default path `https://github.com/zephyrproject-rtos/zephyr`. 

Choose a target-specific template (such as STM32 or NXP) and select your Zephyr version (such as v4.3.0 or later). Specify the directory for your workspace, keeping in mind that initialization takes approximately 10 minutes to complete. 

Select **Import** to create and update the workspace.

(figure: Workbench for Zephyr Initialize Workspace panel in Visual Studio Code showing fields for setting up a West workspace, including template selection from Minimal, STM32, and NXP options, with Zephyr version dropdown listing v3.7.0 and v4.1.0#center)
   
**Note:**
The workspace initialization downloads the Zephyr source code and dependencies. This process can take several minutes depending on your internet connection speed.
