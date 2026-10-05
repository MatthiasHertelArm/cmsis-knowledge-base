---
id: "alp-observing-ethos-u-on-alif-7-load-test-image-save-your-image"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Process and copy a sample image into the Alif E8 CMSIS project: Save your image"
summary: "Create a directory for the input image and preprocessing script:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image/#save-your-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

Create a directory for the input image and preprocessing script:


  **macOS and Linux:**
mkdir -p ~/mnist_alif/image
cd ~/mnist_alif/image
  

  **Windows (PowerShell):**
New-Item -ItemType Directory -Force -Path ~\mnist_alif\image
cd ~\mnist_alif\image
  


Place a PNG or JPEG image of a handwritten digit in the directory and name it `mnist_image.jpg`.

**Note:**
Use a simple, centered, high-contrast digit image. The script supports black-on-white and white-on-black images, and automatically converts black-on-white images to MNIST-style white-on-black format.

You can use any of the images within the [MNIST dataset on Hugging Face](https://huggingface.co/datasets/ylecun/mnist).
