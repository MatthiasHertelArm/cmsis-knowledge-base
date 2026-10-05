---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-deployment-overview"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Deployment overview"
summary: "This section is where the heterogeneous system comes together. Linux on the application cores manages the lifecycle of Cortex-M33 through RemoteProc, and your Cortex-M33 firmware brings up ExecuTorch and the Ethos-U65 delegate."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#deployment-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

This section is where the heterogeneous system comes together.
Linux on the application cores manages the lifecycle of Cortex-M33 through RemoteProc, and your Cortex-M33 firmware brings up ExecuTorch and the Ethos-U65 delegate.

Your success criteria is simple and observable: the remoteproc trace buffer shows a completed inference run with no bus errors.
