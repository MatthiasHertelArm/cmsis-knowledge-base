---
id: "alp-deploy-ml-model-to-npu-with-topo-overview-what-you-ll-deploy"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Understand the architecture of the machine learning application: W"
summary: "Topo is an open-source command-line tool developed by Arm that you can use to deploy projects to an Arm-based Linux target over SSH."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/overview/#what-you-ll-deploy"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Topo](https://github.com/arm/topo) is an open-source command-line tool developed by Arm that you can use to deploy projects to an Arm-based Linux target over SSH. Topo builds container images on the host, transfers them to the target, and starts the services on the target. Topo Projects are the standardized format for deploying projects with Topo.

In this Learning Path, you'll deploy the [topo-imx93-npu-deployment](https://github.com/Arm-Examples/topo-imx93-npu-deployment) Topo Project to an NXP FRDM i.MX 93 board, and understand how this Topo Project was created.

The Topo Project builds and deploys a browser-based MobileNetV2 image classifier. The user interface runs on the Cortex-A (Linux) side of the SoC. The inference runner is packaged as Cortex-M33 firmware and is started by [remoteproc-runtime](https://github.com/arm/remoteproc-runtime). The model is exported to an [ExecuTorch](https://docs.pytorch.org/executorch/stable/index.html) `.pte` [file](https://docs.pytorch.org/executorch/stable/pte-file-format.html) for Ethos-U65 NPU acceleration.
