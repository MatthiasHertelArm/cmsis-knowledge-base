---
id: "alp-alif-image-classification-aws-ec2-setup-why-an-arm-cloud-instance"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Why an Arm cloud instance?"
summary: "ExecuTorch's Arm backend build scripts are designed for native Arm compilation. The Vela compiler, which generates optimized command streams for Ethos-U NPUs, and the CMSIS-NN kernels all target Arm natively."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#why-an-arm-cloud-instance"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch's Arm backend build scripts are designed for native Arm compilation. The Vela compiler, which generates optimized command streams for Ethos-U NPUs, and the CMSIS-NN kernels all target Arm natively. Using an Arm-based EC2 instance avoids the complexity of cross-compilation from x86.

In this section, you launch a Graviton-based EC2 instance, install ExecuTorch, compile a MobileNetV2 model for the Ethos-U85, and build the ExecuTorch static libraries that your firmware links against.
