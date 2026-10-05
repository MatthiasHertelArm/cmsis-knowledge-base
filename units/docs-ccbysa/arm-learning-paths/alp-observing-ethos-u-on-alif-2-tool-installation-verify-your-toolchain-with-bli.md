---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-verify-your-toolchain-with-bli"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Verify your toolchain with Blinky"
summary: "Build and flash the built-in Blinky example to verify your toolchain:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#verify-your-toolchain-with-blinky"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build and flash the built-in Blinky example to verify your toolchain:

1. In VS Code, select the **CMSIS** icon in the left sidebar.
2. Select the **gear icon**.
3. Set **Active Target** to **E8-HE**.
4. Set **Active Project** to **blinky**.
5. Select the **Build** (hammer) icon.
6. Open the **Command Palette** and run **Tasks: Run Task**.
7. Select **Program with Security Toolkit (select COM port)**.
8. Choose the DevKit port when prompted.

If the RGB LED blinks, your VS Code setup, CMSIS packs, SETOOLS configuration, and board connection are working.
