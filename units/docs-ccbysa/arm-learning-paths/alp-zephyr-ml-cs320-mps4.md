---
id: "alp-zephyr-ml-cs320-mps4"
type: "concept"
domain: "edge-ai"
title: "Deploy a Zephyr-based machine learning application on Arm Corstone-320 MPS4 with ExecuTorch"
summary: "Deploy a quantized PyTorch model with ExecuTorch in a Zephyr application on Corstone-320 MPS4 and verify inference."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Deploy a quantized PyTorch model with ExecuTorch in a Zephyr application on Corstone-320 MPS4 and verify inference.

**Who is this for:** This is an introductory topic for embedded software developers who want to deploy a Zephyr-based ML Application on the Arm Corstone-320 MPS4 Platform with ExecuTorch.

**Learning objectives:**

- Set up a Zephyr and ExecuTorch development environment for Corstone-320 MPS4.
- Quantize and export a PyTorch model for Ethos-U85 neural processing unit (NPU) delegation.
- Configure and build the Zephyr `hello-executorch` application for Corstone-320 MPS4.
- Run the application on the MPS4 board and verify machine learning (ML) inference through UART output.

**Prerequisites:**

- Basic familiarity with embedded C programming
- Basic familiarity with machine learning concepts
- A Zephyr workspace and board target using Zephyr version V4.3.0 that you prepared by completing the [Port Zephyr RTOS and run applications on the Arm Corstone-320 MPS4 platform](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/) Learning Path
- A Corstone-320 MPS4 FPGA development board
- A Linux development environment, such as Ubuntu 22.04 or later

**Steps:**

1. Set up the Zephyr and ExecuTorch development environment
2. Build and run a machine learning application on the Corstone-320 MPS4 platform

Time: about 45 minutes.
