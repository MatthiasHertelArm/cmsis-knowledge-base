---
id: "alp-alif-image-classification-aws-ec2-setup-launch-an-ec2-instance"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Launch an EC2 instance"
summary: "Create an AWS EC2 instance with the following configuration:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#launch-an-ec2-instance"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create an AWS EC2 instance with the following configuration:

- **Instance type**: `c7g.4xlarge` (Arm Graviton3, 16 vCPUs, 32 GB RAM)
- **OS**: Ubuntu 22.04 LTS
- **Storage**: 50 GB

The 16 cores speed up the ExecuTorch build significantly, and the 50 GB disk accommodates the repository, submodules, and build artifacts.

SSH to the EC2 instance.
