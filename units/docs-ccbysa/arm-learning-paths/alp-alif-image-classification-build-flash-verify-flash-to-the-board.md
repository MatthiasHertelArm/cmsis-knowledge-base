---
id: "alp-alif-image-classification-build-flash-verify-flash-to-the-board"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: Flash to the board"
summary: "In VS Code, press F1, select Tasks: Run Task, then select Program with Security Toolkit (select COM port). Choose the DevKit's port when prompted."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#flash-to-the-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

In VS Code, press **F1**, select **Tasks: Run Task**, then select **Program with Security Toolkit (select COM port)**. Choose the DevKit's port when prompted.

The flashing process takes about 30 seconds. The Security Toolkit reads the `M55_HP_cfg.json` configuration and writes the binary to the correct MRAM address.
