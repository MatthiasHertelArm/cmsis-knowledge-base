---
id: "alp-alif-image-classification-board-setup-verify-your-toolchain-build-an"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Verify your toolchain: build and flas"
summary: "Before moving on to ML code, verify your entire toolchain works end to end with the built-in Blinky example."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#verify-your-toolchain-build-and-flash-blinky"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before moving on to ML code, verify your entire toolchain works end to end with the built-in Blinky example.

- In VS Code, select the **CMSIS** icon in the left sidebar.
- Select the gear icon, then set **Active Target** to **E8-HP** and **Active Project** to **blinky**.
- Select the **Build** (hammer) icon.
- Press **Fn+F1**, select **Tasks: Run Task**, then select **Program with Security Toolkit (select COM port)**.
- Choose the DevKit's port when prompted.

If the DevKit's red LED blinks, your toolchain, SETOOLS, and DevKit connection are all working correctly. You are ready to move on to model compilation.
