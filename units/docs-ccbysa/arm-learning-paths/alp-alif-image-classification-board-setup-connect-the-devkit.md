---
id: "alp-alif-image-classification-board-setup-connect-the-devkit"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Connect the DevKit"
summary: "Leave SW4 in its default position. This routes the on-board USB UART to SEUART, which the Alif Security Toolkit (SETOOLS) uses for programming."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#connect-the-devkit"
license: "CC-BY-SA-4.0"
mode: "V"
---

- Unplug all USB cables from the DevKit before changing any jumpers.

- Verify that the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).

- Connect a USB-C cable from your computer to the **PRG USB** port on the bottom edge of the DevKit.

- Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave **SW4** in its default position. This routes the on-board USB UART to **SEUART**, which the Alif Security Toolkit (SETOOLS) uses for programming.

**Note:**
Close any terminal application that's connected to SEUART, such as PuTTY, minicom, or screen, before you use the Security Toolkit (SETOOLS). The DevKit exposes only one SEUART interface, so SETOOLS can't access the port if another application is already using it.


- Create a project directory:

```bash
mkdir ~/alif
```
