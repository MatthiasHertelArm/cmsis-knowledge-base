---
id: "alp-alif-dual-npu-vision"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr"
summary: "Build a power-conscious live camera demo that drives Ethos-U55 and Ethos-U85 from one Cortex-M55 MCU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build a power-conscious live camera demo that drives Ethos-U55 and Ethos-U85 from one Cortex-M55 MCU.

**Who is this for:** This is an advanced topic for embedded ML developers who want to run two ExecuTorch models concurrently on separate Ethos-U NPUs under Zephyr.

**Learning objectives:**

- Identify how one microcontroller unit (MCU) can coordinate two neural processing units (NPUs) while avoiding the power and system cost of a second MCU or application processor.
- Configure an Alif Ensemble E8 DevKit for native Zephyr camera, image signal processor (ISP), display, and dual-NPU operation.
- Build, package, and flash an ExecuTorch application that targets Ethos-U55 and Ethos-U85.
- Validate live camera capture, model results, and parallel inference timing.

**Prerequisites:**

- Experience with C or C++, embedded systems, and Zephyr build concepts
- A development machine running macOS on Apple silicon with Homebrew and the Xcode Command Line Tools installed
- An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with an MT9M114 camera connected to J16 and an MW405 display
- Alif SEROM 1.105.65 and SERAM 1.110.0 installed on the board
- Alif Security Toolkit (SETOOLS) 1.10 installed on the development machine

**Steps:**

1. Understand the dual-NPU architecture
2. Prepare the board and workspace
3. Build the dual-NPU application
4. Package and flash the application
5. Validate live parallel inference

Time: about 90 minutes.
