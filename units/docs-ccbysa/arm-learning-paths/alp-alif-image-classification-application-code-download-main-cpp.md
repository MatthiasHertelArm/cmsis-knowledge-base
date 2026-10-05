---
id: "alp-alif-image-classification-application-code-download-main-cpp"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: Download main.cpp"
summary: "Download the working main.cpp from the workshop repository and place it in your project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#download-main-cpp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Download the working `main.cpp` from the workshop repository and place it in your project:

```bash
cd ~/alif/alif_vscode-template/mv2_runner
curl -L -o main.cpp \
  https://raw.githubusercontent.com/ArmDeveloperEcosystem/workshop-ethos-u/refs/heads/main/mv2_runner/main.cpp
```

**Note:**
If you prefer, you can clone the full repository with `git clone https://github.com/ArmDeveloperEcosystem/workshop-ethos-u.git` and copy `main.cpp` from there.


The following sections explain what the code does. The downloaded file is ready to build as-is.
