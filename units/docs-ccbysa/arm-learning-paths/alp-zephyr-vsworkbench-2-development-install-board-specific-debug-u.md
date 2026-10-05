---
id: "alp-zephyr-vsworkbench-2-development-install-board-specific-debug-u"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Build a Zephyr application with Workbench for Zephyr: Install board-specific debug utilities"
summary: "To enable debugging on your target hardware, you might need to install additional tools based on the board vendor."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/2_development.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/2_development/#install-board-specific-debug-utilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

To enable debugging on your target hardware, you might need to install additional tools based on the board vendor.

For the NXP FRDM-MCXN947, download and install the LinkServer debug utility:
- LinkServer for Microcontrollers: [NXP LinkServer Download Page](https://www.nxp.com/design/design-center/software/development-software/mcuxpresso-software-and-tools-/linkserver-for-microcontrollers:LINKERSERVER)

Once installed, Workbench for Zephyr attempts to detect it automatically during a debug session.
If you're using a different board, see your vendor's documentation to install the appropriate debug utility.

**Note:** If Workbench for Zephyr doesn't automatically detect the installed debug runner, you can manually configure it.
Open the **Debug Manager** from the Zephyr sidebar, and enter the full path to the runner executable.
