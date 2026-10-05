---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-what-you-will-build"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: What you will build"
summary: "In this section, you'll build the topo-imx93-npu-deployment Topo Project starting from two non-Topo, non-Compose projects:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#what-you-will-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you'll build the `topo-imx93-npu-deployment` Topo Project starting from two non-Topo, non-Compose projects:

- a Cortex-A web application that prepares images, writes model and tensor data into shared memory, and sends inference commands over `RPMsg`
- a Cortex-M33 ExecuTorch runner firmware project for the FRDM i.MX 93

You'll combine those sources into one repository, then make the repository a normal Compose project. Then, you'll add the Topo metadata and Remoteproc Runtime services.
