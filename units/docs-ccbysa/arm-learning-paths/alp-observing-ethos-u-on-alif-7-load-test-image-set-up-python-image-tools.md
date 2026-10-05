---
id: "alp-observing-ethos-u-on-alif-7-load-test-image-set-up-python-image-tools"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Process and copy a sample image into the Alif E8 CMSIS project: Set up Python image tool"
summary: "You'll convert a handwritten digit image into a C header that the firmware can include at build time."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/7-load-test-image/#set-up-python-image-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll convert a handwritten digit image into a C header that the firmware can include at build time.

To start, create a Python virtual environment for image preprocessing:


  **macOS and Linux:**
  cd ~/mnist_alif
  python3 -m venv venv_image_prep
  source venv_image_prep/bin/activate
  python -m pip install --upgrade pip
  python -m pip install numpy pillow
  

  **Windows (PowerShell):**
  cd ~\mnist_alif
  py -m venv venv_image_prep
  .\venv_image_prep\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  python -m pip install numpy pillow
