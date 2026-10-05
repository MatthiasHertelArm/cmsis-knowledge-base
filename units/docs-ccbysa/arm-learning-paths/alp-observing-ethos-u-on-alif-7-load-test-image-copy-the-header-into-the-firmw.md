---
id: "alp-observing-ethos-u-on-alif-7-load-test-image-copy-the-header-into-the-firmw"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Process and copy a sample image into the Alif E8 CMSIS project: Copy the header into the"
summary: "Copy input_mnist.h into the application assets directory:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image/#copy-the-header-into-the-firmware-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Copy `input_mnist.h` into the application assets directory:


  **macOS and Linux:**
cp ~/mnist_alif/image/input_mnist.h ~/mnist_alif/alif_vscode-template/mnist_executorch/assets/
  

  **Windows (PowerShell):**
Copy-Item "$HOME\mnist_alif\image\input_mnist.h" "$HOME\mnist_alif\alif_vscode-template\mnist_executorch\assets\"
  


Verify that both firmware assets are present:


  **macOS and Linux:**
ls -lh ~/mnist_alif/alif_vscode-template/mnist_executorch/assets/
  

  **Windows (PowerShell):**
Get-ChildItem "$HOME\mnist_alif\alif_vscode-template\mnist_executorch\assets"
  


The output is similar to:

```output
input_mnist.h
mnist_model_data.h
```
