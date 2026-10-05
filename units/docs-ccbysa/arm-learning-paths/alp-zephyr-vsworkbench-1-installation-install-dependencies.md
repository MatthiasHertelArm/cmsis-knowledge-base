---
id: "alp-zephyr-vsworkbench-1-installation-install-dependencies"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Set up the Workbench for Zephyr development environment: Install dependencies"
summary: "To get started with Workbench for Zephyr, you need to have Visual Studio Code downloaded, installed, and running on your computer:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/1_installation/#install-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

To get started with Workbench for Zephyr, you need to have Visual Studio Code downloaded, installed, and running on your computer:


### Windows
For Windows, you need version 10 or later (64-bit x64), along with administrator privileges for installing runners and drivers. 

### macOS
On macOS, the Homebrew package manager is required. To install Homebrew, run the following command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Linux
To use Workbench for Zephyr on Linux, install a recent 64-bit distribution such as Ubuntu 20.04 or later, Fedora, Clear Linux OS, or Arch Linux. Other distributions can work, but you might need to manually configure some system packages. After installing your operating system, use the Workbench host tools manager to check that all required tools are installed correctly.


Zephyr Workbench supports STM32 development boards (STM32 Discovery, Nucleo series), Nordic Semiconductor boards (nRF52, nRF53, nRF91 series), NXP development boards (FRDM, LPCXpresso series), Espressif boards (ESP32-based boards), and many other Zephyr-supported platforms like Renesas, Silabs or Infineon. You need a development board to try out the code examples.
