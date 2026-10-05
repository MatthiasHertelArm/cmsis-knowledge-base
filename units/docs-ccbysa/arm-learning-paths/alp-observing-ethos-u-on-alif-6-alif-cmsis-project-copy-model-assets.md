---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-copy-model-assets"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Create the Alif E8 CMSIS project: Copy model assets"
summary: "Create an assets directory and copy the model header into the project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#copy-model-assets"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create an assets directory and copy the model header into the project:


  **macOS and Linux:**
mkdir -p mnist_executorch/assets
cp ~/mnist_alif/executorch-alif/output/mnist_model_data.h mnist_executorch/assets/
  

  **Windows (PowerShell):**
New-Item -ItemType Directory -Force -Path .\mnist_executorch\assets
Copy-Item ~\mnist_alif\executorch-alif\output\mnist_model_data.h .\mnist_executorch\assets\
