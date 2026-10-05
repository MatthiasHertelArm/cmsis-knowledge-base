---
id: "alp-alif-image-classification-aws-ec2-setup-install-system-dependencies"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Install system dependencies"
summary: "Connect to your instance and install the required packages:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#install-system-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

Connect to your instance and install the required packages:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  git \
  cmake \
  ninja-build \
  build-essential \
  python3.10 \
  python3.10-venv \
  python3-pip \
  unzip \
  wget \
  rsync
```

Reboot if the kernel was updated:

```bash
sudo reboot
```

After reconnecting, verify that Python 3.10 is available:

```bash
python3 --version
```

The output is similar to:

```output
Python 3.10.12
```
