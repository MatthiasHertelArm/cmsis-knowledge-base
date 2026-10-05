---
id: "alp-observing-ethos-u-on-alif"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85"
summary: "Run MNIST digit classification on an Alif Ensemble E8 DevKit with ExecuTorch and Ethos-U85 NPU acceleration, from setup through firmware deployment."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run MNIST digit classification on an Alif Ensemble E8 DevKit with ExecuTorch and Ethos-U85 NPU acceleration, from setup through firmware deployment.

**Who is this for:** This is an introductory topic for embedded developers and ML engineers who want to run TinyML inference on physical hardware with Arm Ethos-U85 NPU acceleration.

**Learning objectives:**

- Set up the Alif Ensemble E8 DevKit for ML applications.
- (Optional) Train, compile and export an MNIST PyTorch model to ExecuTorch .pte format using a Docker container.
- Configure CMSIS project files, memory layout, and linker scripts for an ML workload on the Alif Ensemble E8.
- Build and flash firmware to the Alif Ensemble E8 DevKit.
- Run MNIST digit classification on the Ethos-U85 NPU, and monitor inference results through SEGGER Real-Time Transfer (RTT).

**Prerequisites:**

- Experience with C or C++ and embedded development concepts
- Alif [Ensemble E8 Series Development Kit](https://alifsemi.com/ensemble-e8-series/) (contact [Alif Sales](https://alifsemi.com/support/sales-support/))
- USB Type-C cable for programming
- A SEGGER J-Link debug probe, included in the DevKit
- A development machine running Windows, Linux, or macOS with Visual Studio Code installed

**Steps:**

1. Learn about MNIST and the Alif Ensemble E8 DevKit
2. Set up the Alif Ensemble E8 DevKit
3. (Optional) Set up a Docker development environment
4. (Optional) Export PyTorch model to ExecuTorch format
5. Prepare the ExecuTorch model and static libraries for the Alif E8 CMSIS project
6. Create the Alif E8 CMSIS project
7. Process and copy a sample image into the Alif E8 CMSIS project
8. Flash and run the project on the Alif Ensemble E8 DevKit

Time: about 45 minutes.
