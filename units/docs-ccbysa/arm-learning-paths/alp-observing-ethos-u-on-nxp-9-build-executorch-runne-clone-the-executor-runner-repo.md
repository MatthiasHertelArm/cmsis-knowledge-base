---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-clone-the-executor-runner-repo"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Clone the executor_runner repository"
summary: "Clone the ready-to-build executor_runner project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#clone-the-executor-runner-repository"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone the ready-to-build executor_runner project:

```bash
git clone https://github.com/fidel-makatia/Executorch_runner_cm33.git
cd Executorch_runner_cm33
```

The repository contains the complete runtime source code, pre-built ExecuTorch libraries, and build configuration for Cortex-M33 with Ethos-U65 NPU support.
