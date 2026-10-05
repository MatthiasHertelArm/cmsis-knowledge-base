---
id: "alp-alif-image-classification-aws-ec2-setup-clone-and-install-executorch"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Clone and install ExecuTorch"
summary: "Clone the ExecuTorch repository and pin it to a known-working commit:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#clone-and-install-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone the ExecuTorch repository and pin it to a known-working commit:

```bash
mkdir -p ~/alif
cd ~/alif
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 40d94b6d62a195a2f46b2baa20383fa4af27f7d4
git submodule update --init --recursive
```

**Note:**
The `git checkout` command pins ExecuTorch to a known-working commit. The Arm backend and Vela toolchain integration can change between commits, so pinning avoids unexpected breakage.


Install the ExecuTorch Python package:

```bash
python -m pip install -e . --no-build-isolation
```
