---
id: "alp-observing-ethos-u-on-alif-5-prepare-firmware-artif-before-you-begin"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Prepare the ExecuTorch model and static libraries for the Alif E8 CMSIS project: Before "
summary: "The firmware project needs two artifacts:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/#before-you-begin"
license: "CC-BY-SA-4.0"
mode: "V"
---

The firmware project needs two artifacts:

- `mnist_ethos_u85.pte`: the ExecuTorch model compiled for Ethos-U85
- `et_bundle.tar.gz`: ExecuTorch headers and static libraries for the bare-metal Cortex-M build

If you completed the optional sections to train and export the model yourself, these files are already in `~/mnist_alif/executorch-alif/output/`.

<!-- This is if we provide it as a package instead of separate files -->

If you skipped the optional sections and are using the provided `.pte` file, create the output directory and download the provided artifacts:


  **macOS and Linux:**
mkdir -p ~/mnist_alif/executorch-alif/output
cd ~/mnist_alif/executorch-alif/output
curl -L -o et_bundle.tar.gz https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/et_bundle.tar.gz
curl -L -o mnist_ethos_u85.pte https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_ethos_u85.pte
  

  **Windows (PowerShell):**
New-Item -ItemType Directory -Force -Path "$HOME\mnist_alif\executorch-alif\output"
cd "$HOME\mnist_alif\executorch-alif\output"
curl.exe -L -o et_bundle.tar.gz https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/et_bundle.tar.gz
curl.exe -L -o mnist_ethos_u85.pte https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/main/mnist_ethos_u85.pte
  


Verify all artifacts are present:


  **macOS and Linux:**
ls -lh ~/mnist_alif/executorch-alif/output/mnist_ethos_u85.pte
ls -lh ~/mnist_alif/executorch-alif/output/et_bundle.tar.gz
  

  **Windows (PowerShell):**
Get-Item ~\mnist_alif\executorch-alif\output\mnist_ethos_u85.pte
Get-Item ~\mnist_alif\executorch-alif\output\et_bundle.tar.gz
