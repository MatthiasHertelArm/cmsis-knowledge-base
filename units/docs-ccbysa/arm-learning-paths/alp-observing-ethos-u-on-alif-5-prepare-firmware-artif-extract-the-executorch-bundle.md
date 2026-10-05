---
id: "alp-observing-ethos-u-on-alif-5-prepare-firmware-artif-extract-the-executorch-bundle"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Prepare the ExecuTorch model and static libraries for the Alif E8 CMSIS project: Extract"
summary: "Extract the ExecuTorch headers (from et_bundle.tar.gz) into the VS Code template project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/#extract-the-executorch-bundle"
license: "CC-BY-SA-4.0"
mode: "V"
---

Extract the ExecuTorch headers (from `et_bundle.tar.gz`) into the VS Code template project:


  **macOS and Linux:**
cd ~/mnist_alif/alif_vscode-template
mkdir -p third_party/executorch
tar -C third_party/executorch -xzf ~/mnist_alif/executorch-alif/output/et_bundle.tar.gz
  

  **Windows (PowerShell):**
cd ~\mnist_alif\alif_vscode-template
New-Item -ItemType Directory -Force -Path .\third_party\executorch
tar -C .\third_party\executorch -xzf "$HOME\mnist_alif\executorch-alif\output\et_bundle.tar.gz"
  


Verify the headers are in place:

```bash
ls third_party/executorch/et_bundle/include/executorch/
```
You should see `runtime/` and other directories.

You're now ready to integrate the model into the VS Code project.
