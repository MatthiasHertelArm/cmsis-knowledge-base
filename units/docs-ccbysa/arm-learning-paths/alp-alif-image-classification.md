---
id: "alp-alif-image-classification"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85"
summary: "Deploy a MobileNetV2 image classification model to an Alif Ensemble E8 DevKit and run inference on the Ethos-U85 NPU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Deploy a MobileNetV2 image classification model to an Alif Ensemble E8 DevKit and run inference on the Ethos-U85 NPU.

**Who is this for:** This is an advanced topic for embedded developers who want to deploy a neural network model to an Arm Cortex-M55 microcontroller using ExecuTorch and an Ethos-U85 NPU.

**Learning objectives:**

- Compile a MobileNetV2 model for the Ethos-U85 NPU using ExecuTorch's ahead-of-time (AOT) compiler on an Arm-based cloud instance
- Build ExecuTorch static libraries for bare-metal Cortex-M55 targets
- Configure CMSIS project files, memory layout, and linker scripts for an ML workload on the Alif Ensemble E8
- Run real-time image classification inference on the Ethos-U85 NPU and verify results using SEGGER Real-Time Transfer (RTT)

**Prerequisites:**

- Experience with C/C++ and embedded development concepts
- An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with a USB-C cable
- A SEGGER J-Link debug probe (included in the DevKit)
- A development machine running macOS on Apple Silicon with Visual Studio Code installed
- An AWS account or access to an Arm-based cloud instance for native Arm compilation

**Steps:**

1. Set up the Alif Ensemble E8 DevKit
2. Compile the model on an Arm cloud instance
3. Create the image classification firmware project
4. Add the application code
5. Configure memory layout and flash settings
6. Prepare a test image
7. Build, flash, and verify inference

Time: about 120 minutes.
