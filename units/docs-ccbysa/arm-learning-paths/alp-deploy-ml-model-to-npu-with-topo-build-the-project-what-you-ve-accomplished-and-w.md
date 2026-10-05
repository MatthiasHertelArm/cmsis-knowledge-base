---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-what-you-ve-accomplished-and-w"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: What you've accomplished and "
summary: "You started with two non-Topo, non-Compose projects, made them a standard Compose project, and then converted that Compose project into a Topo Project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#what-you-ve-accomplished-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You started with two non-Topo, non-Compose projects, made them a standard Compose project, and then converted that Compose project into a Topo Project. You created the web app image, added artifact builds for the ExecuTorch `.pte` model and Cortex-M33 ELF, packaged the firmware as a Remoteproc Runtime service, and exposed the build cache inputs as Topo parameters.

Next, you'll prepare the FRDM i.MX 93 target, deploy the project with Topo, and run the image classification application.
