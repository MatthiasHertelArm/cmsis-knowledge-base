---
id: "alp-observing-ethos-u-on-nxp-1-overview-before-you-begin"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Understand ExecuTorch deployment on NXP with Ethos-U: Before you begin"
summary: "This Learning Path assumes your FRDM i.MX 93 board is already set up and you can transfer files between your host machine and the board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/1-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/1-overview/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

This Learning Path assumes your FRDM i.MX 93 board is already set up and you can transfer files between your host machine and the board.

If you still need to set up Linux, serial console access, and file transfer, follow the Learning Path [Linux on an NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/) before continuing.

ExecuTorch is designed to scale from servers to endpoints, and Arm systems often scale within a *single device*.
The FRDM i.MX 93 platform combines:

- An application processor running Linux (Cortex-A) that handles system services and orchestration
- A Cortex-M33 microcontroller core that runs real-time firmware
- An Ethos-U65 NPU that accelerates TinyML inference

This Learning Path focuses on a concrete milestone: successful bring-up of an ExecuTorch `executor_runner` firmware on Cortex-M33 on this NXP platform.

This example keeps the Linux side intentionally simple. Linux loads and starts the Cortex-M33 firmware through RemoteProc, and you stage a compiled ExecuTorch `.pte` model so the firmware can run it.
