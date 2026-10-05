---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-connect-to-the-alif-ensemble-e"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Connect to the Alif Ensemble E8 DevKit"
summary: "To connect to the Alif Ensemble E8 DevKit:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#connect-to-the-alif-ensemble-e8-devkit"
license: "CC-BY-SA-4.0"
mode: "V"
---

To connect to the Alif Ensemble E8 DevKit:

1. Unplug all USB cables from the DevKit before changing any jumpers.

2. Verify that the jumpers are in their factory default positions, as shown in the Alif Ensemble E8 DevKit (DK-E8) User Guide on [alifsemi.com](https://alifsemi.com/support/kits/ensemble-e8devkit/).

3. Connect a USB-C cable from your computer to the PRG USB port on the bottom edge of the DevKit.

(figure: Close-up of the Alif Ensemble E8 DevKit showing a USB-C cable connected to the PRG USB port; the separate MCU USB port is visible below#center)

4. Confirm that a green LED illuminates near the E1 device and the UART switch (SW4).

Leave SW4 in its default position. This routes the on-board USB UART to SEUART, which the Alif Security Toolkit (SETOOLS) uses for programming.
