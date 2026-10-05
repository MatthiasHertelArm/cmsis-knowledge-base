---
id: "alp-observing-ethos-u-on-nxp"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration"
summary: "Learn how to bring up ExecuTorch executor_runner firmware on the NXP FRDM i.MX 93 Cortex-M33 using Linux RemoteProc, compile .pte models for Ethos-U65, and run inference with NPU acceleration."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Learn how to bring up ExecuTorch executor_runner firmware on the NXP FRDM i.MX 93 Cortex-M33 using Linux RemoteProc, compile .pte models for Ethos-U65, and run inference with NPU acceleration.

**Who is this for:** This is an introductory topic for developers and data scientists new to TinyML who want to observe ExecuTorch performance on a physical device.

**Learning objectives:**

- Bring up a custom ExecuTorch `executor_runner` firmware on the FRDM i.MX 93 Cortex-M33 using Linux RemoteProc
- Compile an ExecuTorch `.pte` model for Ethos-U65 and run inference with NPU acceleration
- Understand how heterogeneous Arm systems split responsibilities across application cores, microcontrollers, and NPUs

**Prerequisites:**

- An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) development board
- A USB Mini-B to USB Type-A cable, or a USB Mini-B to USB Type-C cable
- Completion of [Use Linux on an NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) (Linux setup, login access, and file transfer)
- Basic knowledge of Machine Learning concepts
- A host computer to compile ExecuTorch libraries

**Steps:**

1. Understand ExecuTorch deployment on NXP with Ethos-U
2. Boot the NXP FRDM i.MX 93 board
3. Set up the ExecuTorch build environment
4. Build and install ExecuTorch
5. Build ExecuTorch models for Ethos-U65
6. Build Cortex-M33 firmware for ExecuTorch
7. Deploy and test on FRDM-IMX93

Time: about 120 minutes.
