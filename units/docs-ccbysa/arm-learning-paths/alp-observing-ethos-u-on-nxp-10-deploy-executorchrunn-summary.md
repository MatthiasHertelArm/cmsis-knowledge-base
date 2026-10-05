---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-summary"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Summary"
summary: "You've completed the full bring-up flow for ExecuTorch on the NXP FRDM i.MX 93."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#summary"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've completed the full bring-up flow for ExecuTorch on the NXP FRDM i.MX 93. Along the way, you set up a reproducible build environment, compiled two `.pte` model artifacts targeting the Ethos-U65, built and patched the Cortex-M33 `executor_runner` firmware, and deployed it through Linux RemoteProc to confirm a successful end-to-end inference run. The remoteproc trace buffer confirmed zero bus errors and full NPU operator coverage, establishing a stable foundation for iterating on models and firmware independently.
