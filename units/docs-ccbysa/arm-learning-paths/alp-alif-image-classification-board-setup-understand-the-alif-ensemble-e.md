---
id: "alp-alif-image-classification-board-setup-understand-the-alif-ensemble-e"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Understand the Alif Ensemble E8 hardw"
summary: "The Alif Ensemble E8 DevKit features a dual-core Arm Cortex-M55 processor and three neural processing units (NPUs): two Ethos-U55 and one Ethos-U85."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/board-setup/#understand-the-alif-ensemble-e8-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Alif Ensemble E8 DevKit features a dual-core Arm Cortex-M55 processor and three neural processing units (NPUs): two Ethos-U55 and one Ethos-U85. In this Learning Path, you use the Cortex-M55 High-Performance (HP) core running at 400 MHz to orchestrate inference on the Ethos-U85 NPU.

Before writing any ML code, you need to verify that your toolchain, debug probe, and flashing workflow all function correctly. This section covers DevKit hardware setup, software installation, and a short validation build.

The instructions assume macOS on Apple Silicon. If you use Arm Linux, links are provided for the equivalent Linux packages.
