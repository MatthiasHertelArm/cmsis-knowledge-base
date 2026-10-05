---
id: "alp-alif-image-classification-board-setup-install-the-alif-security-tool"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Install the Alif Security Toolkit"
summary: "The Security Toolkit (SETOOLS) programs firmware images onto the DevKit."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#install-the-alif-security-toolkit"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Security Toolkit (SETOOLS) programs firmware images onto the DevKit.

- Download the macOS version of SETOOLS from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/).

- Extract it into `~/alif`. This creates the toolkit directory under a stable location, for example `~/alif/app-release-exec-macos/`. 

- Update the command below to reflect the filename that you download.

```bash
cd ~/Downloads
tar xvf replace_with_your_alif_security_toolkit_download.tar -C ~/alif
```

- Open a terminal in the SETOOLS directory and run:

```bash
cd ~/alif/app-release-exec-macos
./updateSystemPackage -d
```

On macOS, the system blocks this unsigned binary the first time. After that happens, open **System Settings > Privacy & Security**, scroll to the **Security** section, and select **Allow Anyway**. Run the command again.

When prompted for a serial port, enter the DevKit's USB modem port. On macOS, it usually appears as `/dev/cu.usbmodemXXXXXXX`. If SETOOLS detects the Ensemble E8 and asks to set it as the default, answer `y`.
