---
id: "alp-deploy-ml-model-to-npu-with-topo-deploy-what-you-ve-accomplished"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Clone and deploy the application with Topo: What you've accomplish"
summary: "You've prepared an FRDM i.MX 93 board for shared-memory NPU inference, deployed the topo-imx93-npu-deployment Topo Project with Topo, and started Cortex-M33 firmware through remoteproc-runtime."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy/#what-you-ve-accomplished"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've prepared an FRDM i.MX 93 board for shared-memory NPU inference, deployed the `topo-imx93-npu-deployment` Topo Project with Topo, and started Cortex-M33 firmware through `remoteproc-runtime`. You used a browser-based application to stage the ExecuTorch `.pte` program and input tensor for MobileNetV2 classification with Ethos-U65 acceleration.

You can now use the deployed application as a reference for your own heterogeneous Arm applications, or adapt the model, firmware runner, web interface, or Topo metadata for another target.
