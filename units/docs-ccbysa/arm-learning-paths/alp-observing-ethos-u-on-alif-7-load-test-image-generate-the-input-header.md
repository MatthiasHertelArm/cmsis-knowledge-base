---
id: "alp-observing-ethos-u-on-alif-7-load-test-image-generate-the-input-header"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Process and copy a sample image into the Alif E8 CMSIS project: Generate the input heade"
summary: "Open input_mnist.h and look at the generated input_mnist array. This is the numeric pixel data that main.cpp passes into the ExecuTorch runner."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image/#generate-the-input-header"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the preprocessing script:


  **macOS and Linux:**
cd ~/mnist_alif/image
python prepare_mnist_image.py mnist_image.jpg --output input_mnist.h
  

  **Windows (PowerShell):**
cd ~\mnist_alif\image
python .\prepare_mnist_image.py .\mnist_image.jpg --output .\input_mnist.h
  


Verify the generated file:


  **macOS and Linux:**
ls -lh input_mnist.h
head -n 8 input_mnist.h
  

  **Windows (PowerShell):**
Get-Item .\input_mnist.h
Get-Content .\input_mnist.h -TotalCount 8
  


Open `input_mnist.h` and look at the generated `input_mnist` array. This is the numeric pixel data that `main.cpp` passes into the ExecuTorch runner.
