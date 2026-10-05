---
id: "alp-zephyr-vsworkbench-1-installation-import-and-configure-the-zephy"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Set up the Workbench for Zephyr development environment: Import and configure the Zephyr toolchain"
summary: "To build and debug Zephyr applications for Arm Cortex-M boards, you need to import and configure the Zephyr toolchain using Workbench for Zephyr."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation/#import-and-configure-the-zephyr-toolchain"
license: "CC-BY-SA-4.0"
mode: "V"
---

To build and debug Zephyr applications for Arm Cortex-M boards, you need to import and configure the Zephyr toolchain using Workbench for Zephyr.

In the Workbench for Zephyr panel, select **Import Toolchain**. This opens a guided setup panel.

In the **Import Toolchain** panel, configure the following options to set up your Zephyr toolchain for Arm development:

- **Toolchain Family**: select *Zephyr SDK* to use the official Zephyr toolchain.
- **SDK Type**: select *Minimal* to install only the essential components needed for development.
- **Version**: select the Zephyr SDK release you want to use, such as v0.17.0 or v0.17.3.
- **Target Architectures**: select *arm* to target Arm-based boards.

These settings ensure your environment is optimized for Arm Cortex-M development. After configuring these options, continue with the import process to download and install the selected SDK.

Next, specify the directory where you want to install the SDK. Select **Import** to start the download and installation process. When the import completes, the panel displays a confirmation that the toolchain is ready.

If you see errors during import, check your internet connection and confirm you have at least 2 GB of free disk space. For more troubleshooting tips, review the extension's documentation or check the Visual Studio Code output panel.


(figure: Workbench for Zephyr Import Toolchain panel in Visual Studio Code showing dropdown menus for selecting toolchain family, SDK type, version, and target architectures including Zephyr SDK, Minimal, and arm options#center)
