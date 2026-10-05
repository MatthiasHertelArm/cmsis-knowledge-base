---
id: "alp-alif-image-classification-aws-ec2-setup-extract-the-header-bundle"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Extract the header bundle"
summary: "On your development machine, extract the ExecuTorch headers into the VS Code template project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#extract-the-header-bundle"
license: "CC-BY-SA-4.0"
mode: "V"
---

On your development machine, extract the ExecuTorch headers into the VS Code template project:

```bash
cd ~/alif/alif_vscode-template
mkdir -p third_party/executorch
tar -C third_party/executorch -xzf ~/alif/models/et_bundle.tar.gz
```

Verify the headers are in place:

```bash
ls third_party/executorch/et_bundle/include/executorch/
```

You should see `runtime/` and other directories.

You now have the compiled model, prebuilt libraries, and headers on your development machine, ready to integrate into the firmware project.
