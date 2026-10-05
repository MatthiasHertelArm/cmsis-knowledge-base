---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-rename-main-c-to-main-cpp"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Rename main.c to main.cpp"
summary: "ExecuTorch is a C++ library, so the source file needs a .cpp extension."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#rename-main-c-to-main-cpp"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch is a C++ library, so the source file needs a `.cpp` extension.

Update the extension of `main.c`:


  **macOS and Linux:**
mv mnist_executorch/main.c mnist_executorch/main.cpp
  
  **Windows (PowerShell):**
Rename-Item .\mnist_executorch\main.c main.cpp
